import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for, jsonify, current_app)
from flask_pymongo import PyMongo
from flask_mail import Mail, Message
from pymongo import DESCENDING
from bson.objectid import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from functools import wraps
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["UPLOAD_FOLDER"] = os.path.join('static', 'uploads', 'profile_pictures')
app.config["ALLOWED_EXTENSIONS"] = {'png', 'jpg', 'jpeg'}
app.secret_key = os.environ.get("SECRET_KEY")

# Mail Config
app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")


print("MAIL_USERNAME", os.environ.get("MAIL_USERNAME"))
print("MAIL_PASSWORD", os.environ.get("MAIL_PASSWORD"))


mail = Mail(app)
mongo = PyMongo(app)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            flash("Please log in to access this page")
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# Get Recipes
@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find().sort("created_at", DESCENDING).limit(6))
    return render_template("recipes.html", recipes=recipes)


# All Recipes
@app.route("/all_recipes")
def all_recipes():
    recipes = list(mongo.db.recipes.find().sort("created_at", DESCENDING))
    return render_template("all_recipes.html", recipes=recipes)

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Does username already exist?
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        # Does email already exist?
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email")})

        if existing_user:
            flash("Email already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put user in session
        session["user"] = request.form.get("username").lower()
        flash("Registered successfully")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Does username already exist?
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Does password match?
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    # put user in session
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome back {}!".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # Incorrect password
                flash("Incorrect username or password")
                return redirect(url_for("login"))

        else:
            # Incorrect username
            flash("Incorrect username or password")
            return redirect(url_for("login"))
        
        if login_successful:
            next_page = request.args.get('next')
            return redirect(next_page or url_for('get_recipes'))

    return render_template("login.html")


# Profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Check if the user is in session
    if "user" not in session:
        flash("Please log in to view your profile")
        return redirect(url_for("login"))

    # Fetch the user from the database
    user = mongo.db.users.find_one({"username": session["user"]})
    if not user:
        flash("User not found")
        return redirect(url_for("login"))

    if request.method == "POST":
        # Update Bio
        new_bio = request.form.get("bio")
        mongo.db.users.update_one({"username": user["username"]}, {"$set": {"bio": new_bio}})
        flash("Bio updated successfully")
        # Refresh user data after update
        user = mongo.db.users.find_one({"username": session["user"]})

    # Fetch user's recipes
    user_recipes = list(mongo.db.recipes.find({"created_by": user["username"]}))

    # Fetch user's saved recipes
    saved_recipes = list(mongo.db.saved_recipes.aggregate([
        {"$match": {"user": user["username"]}},
        {"$lookup": {
            "from": "recipes",
            "localField": "recipe_id",
            "foreignField": "_id",
            "as": "recipe"
        }},
        {"$unwind": "$recipe"}
    ]))

    # Get the profile picture URL
    profile_picture = user.get("profile_picture")
    if profile_picture:
        profile_picture = url_for('static', filename=profile_picture.replace('static/', '', 1))
    else:
        profile_picture = url_for('static', filename='images/default_profile.jpg')

    return render_template("profile.html", 
                           username=user["username"], 
                           recipes=user_recipes, 
                           saved_recipes=saved_recipes, 
                           profile_picture=profile_picture, 
                           user_bio=user.get("bio", ""))

    return redirect(url_for("login"))


# Update Bio
@app.route("/update_bio", methods=["POST"])
@login_required
def update_bio():
    username = session["user"]
    new_bio = request.form.get("bio")
    mongo.db.users.update_one({"username": username}, {"$set": {"bio": new_bio}})
    flash("Bio updated successfully")
    return redirect(url_for("profile", username=username))


# Allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in current_app.config["ALLOWED_EXTENSIONS"]

# Profile Picture
@app.route("/upload_profile_picture", methods=["POST"])
@login_required
def upload_profile_picture():
    if 'profile_picture' not in request.files:
        flash("No file part")
        return redirect(url_for("profile", username=session["user"]))

    file = request.files['profile_picture']

    if file.filename == '':
        flash("No selected file")
        return redirect(url_for("profile", username=session["user"]))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        username = session["user"]

        # Create a unique filename for the profile picture
        _, file_extension = os.path.splitext(filename)
        new_filename = f"{username}_profile{file_extension}"

        # Make sure folder exists
        upload_folder = os.path.join('static', 'uploads', 'profile_pictures')
        os.makedirs(upload_folder, exist_ok=True)

        file_path = os.path.join(upload_folder, new_filename)
        file.save(file_path)
        
        # Update the user's profile picture
        db_file_path = os.path.join('uploads', 'profile_pictures', new_filename)
        mongo.db.users.update_one(
            {"username": username}, 
            {"$set": {"profile_picture": db_file_path}}
        )

        flash("Profile picture updated successfully")
    else:
        flash("Invalid file type. Please upload a .png, .jpg, or .jpeg file.")

    return redirect(url_for("profile", username=session["user"]))



# Logout
@app.route("/logout")
def logout():
    # remove user from session
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Add Recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "recipe_description": request.form.get("recipe_description"),
            "serving_size": request.form.get("serving_size"),
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "dietary": request.form.get("dietary"),
            "meal_type": request.form.get("meal_type"),
            "main_ingredients": request.form.getlist("main_ingredients"),
            "recipe_method": request.form.getlist("recipe_method"),
            "likes": 0,
            "created_by": session["user"],
            "created_at": datetime.now().strftime("%d/%m/%Y")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe added successfully")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    meals = mongo.db.meal_type.find().sort("meal_type", 1)
    dietaries = mongo.db.dietary_requirements.find().sort("dietary_name", 1)
    return render_template("add_recipe.html", categories=categories, meals=meals, dietaries=dietaries)



# View Recipe
@app.route("/recipe/<recipe_id>")
def view_recipe(recipe_id):
    if "user" not in session:
        flash("You must be logged in to view recipes")
        return redirect(url_for("login"))
    
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if recipe:
        # Check if the user has saved the recipe
        is_saved = mongo.db.saved_recipes.find_one({
            "user": session["user"], 
            "_id": ObjectId(recipe_id)
        }) is not None

        return render_template("recipe.html", recipe=recipe, is_saved=is_saved)
    else:
        flash("Recipe not found")
        return redirect(url_for("get_recipes"))

# Edit Recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if "user" not in session:
        flash("Please log in to edit recipes")
        return redirect(url_for("login"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    if not recipe:
        flash("Recipe not found")
        return redirect(url_for("get_recipes"))

    if session["user"] != recipe["created_by"]:
        flash("You can only edit your own recipes")
        return redirect(url_for("view_recipe", recipe_id=recipe_id))

    
    if request.method == "POST":
        updated_recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "recipe_description": request.form.get("recipe_description"),
            "serving_size": request.form.get("serving_size"),
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "dietary": request.form.get("dietary"),
            "meal_type": request.form.get("meal_type"),
            "main_ingredients": request.form.getlist("main_ingredients"),
            "recipe_method": request.form.getlist("recipe_method"),
            "created_by": session["user"],
            "created_at": datetime.now().strftime("%d/%m/%Y")
        }
        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {"$set": updated_recipe})
        flash("Recipe Updated Successfully")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    meals = mongo.db.meal_type.find().sort("meal_type", 1)
    dietaries = mongo.db.dietary_requirements.find().sort("dietary_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, categories=categories, meals=meals, dietaries=dietaries)


# Delete Recipe
@app.route("/delete_recipe/<recipe_id>", methods=["GET","POST"])
def delete_recipe(recipe_id):
    try:
        # Check if the user is logged in
        if "user" not in session:
            flash("Please log in to delete recipes")
            return redirect(url_for("login"))
            return jsonify({"error": "User not logged in"}), 401
        # Find the recipe
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        # Check if the recipe exists
        if not recipe:
            return jsonify({"error": "Recipe not found"}), 404
        # Check if the logged-in user is the creator of the recipe
        if session["user"] != recipe["created_by"]:
            return jsonify({"error": "You can only delete your own recipes"}), 403
        # Delete the recipe
        result = mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
        if result.deleted_count == 1:
            flash("Recipe deleted successfully")
            return jsonify({"success": True, "redirect": url_for("get_recipes")})
        else:
            return jsonify({"error": "Failed to delete recipe"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Get Categories
@app.route("/get_categories")
def get_categories():
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("categories.html", categories=categories)

# Add Category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # Check if category exists
    if mongo.db.categories.find_one({"category_name": request.form.get("category_name")}):
        flash("Category already exists")
        return redirect(url_for("get_categories"))  
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("Category added successfully")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# Edit Category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submitted_category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update_one({"_id": ObjectId(category_id)}, ( {"$set": submitted_category}))
        flash("Category updated successfully")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# Delete Category
@app.route("/delete_category/<category_id>", methods=["GET","POST"])
def delete_category(category_id):
    try:
        # Check if the user is logged in
        if "user" not in session:
            flash("Please log in to delete categories")
            return redirect(url_for("login"))
            return jsonify({"error": "User not logged in"}), 401
        # Find the category
        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
        # Check if the category exists
        if not category:
            return jsonify({"error": "Category not found"}), 404
        # Delete the category
        result = mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
        if result.deleted_count == 1:
            flash("Category deleted successfully")
            return jsonify({"success": True, "redirect": url_for("get_categories")})
        else:
            return jsonify({"error": "Failed to delete category"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Search Recipes
@app.route("/search_recipes")
def search_recipes():
    search = request.args.get("search")
    if search:
        pipeline = [
            {
                "$search": {
                    "index": "default",  # Use the name of your search index
                    "text": {
                        "query": search,
                        "path": [
                            "recipe_name", 
                            "recipe_description", 
                            "main_ingredients",
                            "category_name",
                            "dietary"]
                    }
                }
            },
            {
                "$limit": 10  # Limit the number of results
            }
        ]
        recipes = list(mongo.db.recipes.aggregate(pipeline))
    else:
        recipes = list(mongo.db.recipes.find())
    
    return render_template("recipes.html", recipes=recipes, search=search)


# Like Recipe
@app.route("/like_recipe/<recipe_id>", methods=["POST"])
@login_required
def like_recipe(recipe_id):
    user = session["user"]
    
    # Check if the recipe exists
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404
    
    if user in recipe.get("liked_by", []):
        # User has already liked the recipe, so remove their like
        mongo.db.recipes.update_one(
            {"_id": ObjectId(recipe_id)},
            {"$pull": {"liked_by": user}, "$inc": {"likes": -1}}
        )
        action = "removed"
    else:
        # User has not liked the recipe yet, so add their like
        mongo.db.recipes.update_one(
            {"_id": ObjectId(recipe_id)},
            {"$addToSet": {"liked_by": user}, "$inc": {"likes": 1}}
        )
        action = "added"
    
    # Fetch the updated like count
    updated_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    
    return jsonify({"success": True, "action": action, "likes": updated_recipe["likes"]})


# Save Recipe
@app.route("/save_recipe/<recipe_id>", methods=["POST"])
@login_required
def save_recipe(recipe_id):
    if "user" not in session:
        return jsonify({"error": "User not logged in"}), 401

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404

    # Check if the recipe has been saved by the user
    saved_recipe = mongo.db.saved_recipes.find_one({
        "user": session["user"],
        "recipe_id": ObjectId(recipe_id)
    })

    if saved_recipe:
        # If saved_recipe exists, remove it
        mongo.db.saved_recipes.delete_one({"_id": saved_recipe["_id"]})
        action = "unsaved"
    else:
        # If not saved, save it
        save = {
            "user": session["user"],
            "recipe_id": ObjectId(recipe_id),
            "saved_at": datetime.now().strftime("%d/%m/%Y")
        }
        mongo.db.saved_recipes.insert_one(save)
        action = "saved"

    return jsonify({"success": True, "action": action})


# Contact Form
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        msg= Message(subject=f'New Contact Form Submission: {subject}',
                    sender=app.config["MAIL_USERNAME"],
                    recipients=["cambboyle@gmail.com"])
        msg.body = f'From: {name} <{email}>\n\n{message}'

        try:
            mail.send(msg)
            flash("Message sent successfully, We will get back to you soon", "success")
        except Exception as e:
            flash("Message could not be sent. Please try again later", "danger")
            print(e)

        return redirect(url_for("contact"))

    return render_template("contact-form.html")
        

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)