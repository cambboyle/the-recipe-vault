# TESTING

Click here to return to the [README.md](README.md) file.

## Table of Contents

- [VALIDATION](#validation)
- [RESPONSIVE DESIGN](#responsive-design)
- [LIGHTHOUSE TESTING](#lighthouse-testing)
- [DEFENSIVE PROGRAMMING](#defensive-programming)
- [KNOWN BUGS](#known-bugs)
- [FIXED BUGS](#fixed-bugs)

## VALIDATION

The validation for the project was done using the following tools:

### Python Validation (PEP8)

![Python Validation](documentation/other_images/validation/PEP8Validator.png)

### JavaScript Validation (JSHint)

![JavaScript Validation](documentation/other_images/validation/JSHintValidation.png)

### CSS Validation (W3C CSS Validator)

![CSS Validation](documentation/other_images/validation/CSSValidation.png)

The errors are not critical, but it is good to know that they are there.

### HTML Validation (W3C HTML Validator)

![HTML Validation](documentation/other_images/validation/HTMLValidation.png)

The errors here are only appearing because there are multiples recipes on the page, they are not real duplicate errors. They are being utlised using jinja2 templating.

## RESPONSIVE DESIGN

The project was tested on multiple devices and screen sizes to ensure that it is responsive and looks good on all devices.

<details>
<summary>Click for device testing</summary>

### Desktop 1920x1080

| Page | Screenshot |
| --- | --- |
| Landing Page (Hero) | ![Hero](documentation/responsive_images/desktop/hero_desktop.jpg) |
| Recipe Search | ![Recipe Search](documentation/responsive_images/desktop/recipes_desktop.png) |
| How it Works | ![How it Works](documentation/responsive_images/desktop/how_desktop.png) |
| Profile | ![Profile](documentation/responsive_images/desktop/profile_desktop.png) |
| Add Recipe | ![Add Recipe](documentation/responsive_images/desktop/add_recipe_desktop.png) |
| Edit Recipe | ![Edit Recipe](documentation/responsive_images/desktop/edit_recipe_desktop.png) |
| Contact | ![Contact](documentation/responsive_images/desktop/contact_desktop.jpg) |
| Login | ![Login](documentation/responsive_images/desktop/login_desktop.jpg) |
| Register | ![Register](documentation/responsive_images/desktop/register_desktop.jpg) |
| Categories | ![Categories](documentation/responsive_images/desktop/categories_desktop.png) |
| All Recipes | ![All Recipes](documentation/responsive_images/desktop/all_recipes_desktop.png) |
| View Recipe | ![View Recipe](documentation/responsive_images/desktop/recipe_desktop.png) |

### Mobile (iPhone 14 Pro Max)

| Page | Screenshot |
| --- | --- |
| Landing Page (Hero) | ![Hero](documentation/responsive_images/mobile/hero_mobile.png) |
| Recipe Search | ![Recipe Search](documentation/responsive_images/mobile/recipes_mobile.png) |
| How it Works | ![How it Works](documentation/responsive_images/mobile/how_2_mobile.png) |
| How it Works & Footer | ![How it Works & Footer](documentation/responsive_images/mobile/how_mobile.png) |
| Profile | ![Profile](documentation/responsive_images/mobile/profile_mobile.png) |
| Add Recipe | ![Add Recipe](documentation/responsive_images/mobile/add_recipe_mobile.png) |
| Edit Recipe | ![Edit Recipe](documentation/responsive_images/mobile/edit_recipe_mobile.png) |
| Contact | ![Contact](documentation/responsive_images/mobile/contact_mobile.png) |
| Login | ![Login](documentation/responsive_images/mobile/login_mobile.png) |
| Register | ![Register](documentation/responsive_images/mobile/register_mobile.png) |
| Categories | ![Categories](documentation/responsive_images/mobile/categories_mobile.png) |
| All Recipes | ![All Recipes](documentation/responsive_images/mobile/all_recipes_mobile.png) |

### Tablet (iPad Air)

| Page | Screenshot |
| --- | --- |
| Landing Page (Hero) | ![Hero](documentation/responsive_images/tablet/hero_tablet.png) |
| Recipe Search | ![Recipe Search](documentation/responsive_images/tablet/recipes_tablet.png) |
| How it Works | ![How it Works](documentation/responsive_images/tablet/how_tablet.png) |
| Profile | ![Profile](documentation/responsive_images/tablet/profile_tablet.png) |
| Add Recipe | ![Add Recipe](documentation/responsive_images/tablet/add_recipe_tablet.png) |
| Edit Recipe | ![Edit Recipe](documentation/responsive_images/tablet/edit_recipe_tablet.png) |
| Contact | ![Contact](documentation/responsive_images/tablet/contact_tablet.png) |
| Login | ![Login](documentation/responsive_images/tablet/login_tablet.png) |
| Register | ![Register](documentation/responsive_images/tablet/register_tablet.png) |
| Categories | ![Categories](documentation/responsive_images/tablet/categories_tablet.png) |
| All Recipes | ![All Recipes](documentation/responsive_images/tablet/all_recipes_tablet.png) |

</details>

## LIGHTHOUSE TESTING

### Desktop Lighthouse

![Desktop Lighthouse](documentation/other_images/validation/LighthouseDesktop.png)

### Mobile Lighthouse

![Mobile Lighthouse](documentation/other_images/validation/LighthouseMobile.png)

## DEFENSIVE PROGRAMMING

Defensive Programming was tested manually, and the results were as follows:

<details>
<summary>Click for defensive programming testing</summary>

| | Expected Behavior | Test | Actual Behavior |
| --- | --- | --- | --- |
| **General** | | | |
| Text Boxes | Minimum & Maximum lenght on input boxes | Tested by typing characters in a text box that exceeds the minimum or maximum length | When form is submitted, validation message is displayed |
| Password Regex | Expected to only accept characters in the regex | Tested by typing characters that do not match the regex | When form is submitted, validation message is displayed |
| URL change | Redirect user to login page if URL is changed | Tested by changing the URL in the browser | Redirected to the login page |
| **Non-logged in users** | | | |
| Home Button | Expected to redirect to the home page | Tested by clicking the button | Redirected to the home page |
| Login Button | Expected to redirect to the login page | Tested by clicking the button | Redirected to the login page |
| Register Button | Expected to redirect to the register page | Tested by clicking the button | Redirected to the register page |
| Search Function | Expected to search through the user's query | Tested by typing a query in the search bar | Searched through the user's query |
| Recipe Card | Expected to redirect to the single recipe page | Tested by clicking the card | Redirected to the single recipe page |
| **Logged in users** | | | |
| Home Button | Expected to redirect to the home page | Tested by clicking the button | Redirected to the home page |
| Profile Button | Expected to redirect to the profile page | Tested by clicking the button | Redirected to the profile page |
| All Recipes Button | Expected to redirect to the all recipes page | Tested by clicking the button | Redirected to the all recipes page |
| Add Recipe Button | Expected to redirect to the add recipe page | Tested by clicking the button | Redirected to the add recipe page |
| Contact Button | Expected to redirect to the contact page | Tested by clicking the button | Redirected to the contact page |
| Contact Form | Expected to a message to the default email address | Tested by filling out the form | A message was sent to the default email address |
| Logout Button | Expected to redirect to the login page and log the user out | Tested by clicking the button | Redirected to the login page and successfully logged out the user |
| Search Function | Expected to search through the user's query | Tested by typing a query in the search bar | Searched through the user's query |
| Recipe Card | Expected to redirect to the single recipe page | Tested by clicking the card | Redirected to the single recipe page |
| Edit Recipe Button | Expected to redirect to the edit recipe page | Tested by clicking the button | Redirected to the edit recipe page |
| Delete Recipe Button | Expected to delete the recipe | Tested by clicking the button | Deleted the recipe |
| Save Recipe Button | Expected to save the recipe to the user's saved recipes | Tested by clicking the button | Saved the recipe to the user's saved recipes |
| Like Recipe Button | Expected to like the recipe and increment the like count | Tested by clicking the button | Liked the recipe and incremented the like count |
| **Admin Only** | | | |
| Categories Button | Expected to redirect to the categories page | Tested by clicking the button | Redirected to the categories page |
| Add Category Button | Expected to redirect to the add category page | Tested by clicking the button | Redirected to the add category page |
| Edit Category Button | Expected to redirect to the edit category page | Tested by clicking the button | Redirected to the edit category page |
| Delete Category Button | Expected to delete the category | Tested by clicking the button | Deleted the category |

</details>

## KNOWN BUGS

Encountered a bug where the profile picture was not being stored in the database, I tried fixing this by creating a S3 bucket and using the AWS SDK to upload the file to the bucket, but I was unable to get it to work. As I don't have enough experience with AWS, I decided to leave it as is.

I can upload pictures from my IDE and on localhost, but when I try to upload them from Heroku, they are not uploaded.

I have removed the ability to upload profile pictures from the project, as I was unable to get it to work with Heroku.

## FIXED BUGS

### Bug 1

One bug was fixed in the project, which was a bug in the recipe editing page.

The add ingredient/step button was not creating more ingredients/steps when clicked.

This was fixed in by adding the appropriate JavaScript code from the script.js file to the edit_recipe.html file.

The issue also persisted on the add recipe page, so this was also fixed.

### Bug 2

I encountered a bug when deleting a recipe, after clicking the delete button, the user was redirected to a black page, with one line of JSON in it. 
