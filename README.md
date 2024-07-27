# [The Recipe Vault](https://flask-cookbook-app-a80af878055f.herokuapp.com)

## Introduction

- The Recipe Vault is a web application that allows users to create, store, and share recipes.
- The application is designed to veer away from physical cookbooks and instead focus on the concept of recipes.
- Users must create an account to access the applications full features.

## Mockup

| Mockup |
| This is a mockup of the Recipe Vault application, showcased using Am I Responsive? |
| --- |
| ![Mockup](documentation/other_images/AmIResponsiveRecipeVault.png) |

## User Experience

### Colour Scheme

| Colour Scheme |
| --- |
| - #D2C0A7 - 'Warm Beige' Used as the primary colour |
| - #F7B65A - 'Muted Copper' Used as the main hover colour |
| - #593D2B - 'Rich Brown' Used as the secondary colour |
| - #F3EAD6 - 'Soft Cream' Used as primary text colour |
| - #36454F - 'Deep Charcoal' Used as secondary text colour |
| - I also used variations of these colours to darken/lighten some elements |

[coolor.co](https://coolors.co/palette/d2c0a7-f7b65a-593d2b-36454f-f3ead6) was used to generate the colour palette.

I swapped the fancier names for colours with more neutral names to make the colour palette more accessible.

```css
:root {
  /* Colours */
  --primary-colour: #D2C0A7; /* Warm Beige */
  --text-colour: #593D2B; /* Rich Brown */
  --hover-colour: #B87333; /* Muted Copper */
  --text-one: #F3EAD6;  /* Soft Cream */
  --text-two: #36454F; /* Deep Charcoal */

}
```

This was my first time using CSS variables, and I'm happy with how they work.

### Typography

I used [Google Fonts](https://fonts.google.com/) to generate the typography for the application.

I used the following font families:

- [Josefin Sans](https://fonts.google.com/specimen/Josefin+Sans) was used as the body font.
- [Outfit](https://fonts.google.com/specimen/Outfit) was used as the heading font.
- [Font Awesome](https://fontawesome.com/) was used for icons.

```html
<link
    href="https://fonts.googleapis.com/css2?
        family=Josefin+Sans:ital,wght@0,100..700;1,100..700
        &family=Outfit:wght@100..900&display=swap"
    rel="stylesheet">
```

### User Stories

#### New User

- As a new user, I want to be able to create an account so that I can access the full features of the application.
- As a new user, I want to be able to create a recipe so that I can store and share my recipes with others.
- As a new user, I want to be able to save other users recipes so that I can access them later.
- As a new user, I want to search for recipes by name, description, ingredients, cuisine and dietary restrictions so that I can find the recipe I am looking for.

#### Returning User

- As a returning user, I want to be able to log in so that I can access the full features of the application.
- As a returning user, I want to be able to create a recipe so that I can store and share my recipes with others.
- As a returning user, I want to be able to save other users recipes so that I can access them later.
- As a returning user, I want to search for recipes by name, description, ingredients, cuisine and dietary restrictions so that I can find the recipe I am looking for.
- As a returning user, I want to be able to edit my profile so that I can update my information.
- As a returning user, I want to be able to edit my recipes.
- As a returning user, I want to be able to delete my recipes.

#### Admin

- As an admin, I want to be able to delete innapropriate recipes so that I can maintain the quality of the application.
- As an admin, I want to be able to edit recipes so that I can maintain the quality of the application.
- As an admin, I want to be able to add/delete categories upon user requests.

### User Feedback

- ADD FEEDBACK

## Wireframes

For help with responsive design and optimal practice, I created wireframes for desktop, tablet, and mobile devices using [Balsamiq](https://balsamiq.com/).

<details>
<summary>Click for wireframes</summary>

### Landing Page

![Landing Page] (documentation/wireframes/Landing-page.png)

### Recipe Search

![Recipe Search] (documentation/wireframes/recipe-search.png)

### Sign Up

![Sign Up] (documentation/wireframes/Signup-page.png)

### Profile

![Profile] (documentation/wireframes/profile-page.png)

</details>

## Features

Here are some of the features that I implemented in the application, took out and planned for future features.

### Existing Features

<details>
<summary>Existing features</summary>

| Feature | Description | Image |
| --- | --- | --- |
| Site Logo |
| Navigation Bar |
| Hero |
| Search Bar |
| Recently Added Recipes |
| How it Works |
| Footer |
| Sign Up |
| Login |
| Profile |
| Bio |
| Profile Picture |
| User Recipes |
| Saved Recipes |
| Add Recipe |
| Recipe Dropdown |


</details>

### Future Features

- Recipe Images: Allow users to upload their own recipe images.
- Recipe ratings and reviews: Allow users to rate recipes and leave reviews.
- Meal planning: Implement a feature that lets users plan their meals for the week using saved recipes.
- Grocery list generator: Create a tool that generates a shopping list based on selected recipes.
- Nutritional information: Add calorie counts and nutritional facts for each recipe.
- Recipe scaling: Allow users to adjust serving sizes and automatically recalculate ingredient quantities.
- Cooking timer: Integrate a timer feature for each step of the recipe.
- Recipe collections or cookbooks: Let users create and share collections of recipes.
- Social sharing: Add buttons to share recipes on social media platforms.
- Ingredient substitutions: Provide suggestions for ingredient substitutions for dietary restrictions or preferences.
- Video tutorials: Include short video clips demonstrating cooking techniques or complex steps.
- Seasonal recipe recommendations: Highlight recipes based on seasonal ingredients or holidays.
- User-generated content: Allow users to submit their own recipes for review and publication.
- Recipe print functionality: Create a printer-friendly version of recipes.
- Advanced search filters: Implement more detailed search options such as cooking time, difficulty level, or dietary restrictions.
- Recipe version control: Allow users to create personal variations of recipes and track changes.

## Technologies

## Database Schema

## Testing

## Deployment

### Heroku

### MongoDB Atlas

### Local

#### Cloning the Repo

#### Forking the Repo

## Credits

### Images

### Content

Tab Structure on Profile Page from <a href="https://mdbootstrap.com/docs/standard/navigation/tabs/">MDB </a>

Flask-Mail Documentation <a href="https://pypi.org/project/Flask-Mail/">Flask-Mail</a>

### Acknowledgements

Example of recipe (used in recipe cards by default) by <a href="https://unsplash.com/@duanemendes?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Duane Mendes</a> on <a href="https://unsplash.com/photos/person-holding-stainless-steel-spoon-JrRoJlGyZwk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  
Testing hero image by <a href="https://unsplash.com/@fsuarez?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Francisco Suarez</a> on <a href="https://unsplash.com/photos/stainless-steel-cooking-pots-on-stove-0EkWTSFXwCc?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  
Hero Image by <a href="https://unsplash.com/@alexkurchev?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Oleksandr Kurchev</a> on <a href="https://unsplash.com/photos/kitchen-filled-with-cooking-pans-and-kitchen-utensils-9gtiGV76NnM?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  