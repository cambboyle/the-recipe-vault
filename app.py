import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


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
    # grab the username from the session
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        # Fetch user's recipes
        user_recipes = list(mongo.db.recipes.find({"created_by": username}))
        return render_template("profile.html", username=username, recipes=user_recipes)

    return redirect(url_for("login"))


# Logout
@app.route("/logout")
def logout():
    # remove user from session
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


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
            "created_by": session["user"],
            "created_at": datetime.now().strftime("%d-%m-%Y at %H:%M")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe added successfully")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    meals = mongo.db.meal_type.find().sort("meal_type", 1)
    dietaries = mongo.db.dietary_requirements.find().sort("dietary_name", 1)
    return render_template("add_recipe.html", categories=categories, meals=meals, dietaries=dietaries)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            flash("Please log in to access this page")
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/recipe/<recipe_id>")
def view_recipe(recipe_id):
    if "user" not in session:
        flash("You must be logged in to view recipes")
        return redirect(url_for("login"))
        
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if recipe:
        return render_template("recipe.html", recipe=recipe)
    else:
        flash("Recipe not found")
        return redirect(url_for("get_recipes"))


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
            "created_at": datetime.now().strftime("%d-%m-%Y at %H:%M")
        }
        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {"$set": updated_recipe})
        flash("Recipe Updated Successfully")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    meals = mongo.db.meal_type.find().sort("meal_type", 1)
    dietaries = mongo.db.dietary_requirements.find().sort("dietary_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, categories=categories, meals=meals, dietaries=dietaries)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe deleted successfully")
    return redirect(url_for("get_recipes"))



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)