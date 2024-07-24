import { Modal, Button, Ripple, initMDB, Tab } from "mdb-ui-kit";

initMDB({ Modal, Button, Ripple, Tab });

// Recipe Form

// Populate existing ingredients and steps
function populateExistingFields() {
    const ingredientsContainer = document.getElementById('ingredients-container');
    const stepsContainer = document.getElementById('steps-container');

    // Clear existing fields
    ingredientsContainer.innerHTML = '';
    stepsContainer.innerHTML = '';

    // Populate ingredients
    const ingredients = Array.from(document.getElementsByName('main_ingredients')).map(input => input.value);
    ingredients.forEach(ingredient => addIngredient(ingredient));

    // Populate steps
    const steps = Array.from(document.getElementsByName('recipe_method')).map(textarea => textarea.value);
    steps.forEach((step, index) => addStep(step, index + 1));
}

function addIngredient() {
    const container = document.getElementById('ingredients-container');
    if (!container) return;

    const newField = document.createElement('div');
    newField.className = 'ingredient-input mb-2';
    newField.innerHTML = `
        <div class="input-group">
            <input type="text" class="form-control" name="main_ingredients" placeholder="Add Ingredient" required>
            <button class="btn btn-danger  remove_ingredient" type="button">Remove</button>
        </div>
    `;
    container.appendChild(newField);
}

function addStep(content='', stepNumber=null) {
    const container = document.getElementById('steps-container');
    if (!container) return;

    const stepCount =  stepNumber || container.children.length + 1;
    const newField = document.createElement('div');
    newField.className = 'step-input mb-2';
    newField.innerHTML = `
        <div class="input-group">
            <span class="input-group-text">Step ${stepCount}</span>
            <textarea class="form-control" name="recipe_method" rows="2" placeholder="Describe this step" required></textarea>
            <button class="btn btn-danger remove_step" type="button">Remove</button>
        </div>
    `;
    container.appendChild(newField);
}

function removeIngredient(event) {
    if (event.target.classList.contains('remove_ingredient')) {
        event.target.closest('.ingredient-input').remove();
    }
}

function removeStep(event) {
    if (event.target.classList.contains('remove_step')) {
        event.target.closest('.step-input').remove();
        updateStepNumbers();
    }
}

function updateStepNumbers() {
    const steps = document.querySelectorAll('#steps-container .step-input');
    steps.forEach((step, index) => {
        const stepLabel = step.querySelector('.input-group-text');
        stepLabel.textContent = `Step ${index + 1}`;
    });
}

function initializeRecipeForm() {
    const addIngredientButton = document.getElementById('add_ingredient');
    const addStepButton = document.getElementById('add_step');
    const ingredientsContainer = document.getElementById('ingredients-container');
    const stepsContainer = document.getElementById('steps-container');
    
    if (addIngredientButton && ingredientsContainer) {
        addIngredientButton.addEventListener('click', addIngredient);
        ingredientsContainer.addEventListener('click', removeIngredient);
    }

    if (addStepButton && stepsContainer) {
        addStepButton.addEventListener('click', addStep);
        stepsContainer.addEventListener('click', removeStep);
    }

    populateExistingFields();
}

// Delete recipe function
function confirmDelete(recipeId, recipeName) {
    if (confirm(`Are you sure you want to delete the recipe "${recipeName}"?`)) {
        fetch(`/delete_recipe/${recipeId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("Recipe deleted successfully");
                window.location.href = data.redirect;  // Redirect to the recipes page
            } else {
                alert(data.error || "An error occurred while deleting the recipe");
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('An error occurred while deleting the recipe');
        });
    }
}

// Delete category function (admin only)
function confirmDeleteCategory(categoryId, categoryName) {
    if (confirm(`Are you sure you want to delete the category "${categoryName}"?`)) {
        fetch(`/delete_category/${categoryId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("Category deleted successfully");
                window.location.href = data.redirect;  // Redirect to the categories page
            } else {
                alert(data.error || "An error occurred while deleting the category");
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('An error occurred while deleting the category');
        });
    }
}

window.addEventListener('scroll', function() {
    var navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
      navbar.classList.add('navbar-scrolled');
    } else {
      navbar.classList.remove('navbar-scrolled');
    }
  });


// check if DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM fully loaded");
    
    document.getElementById('add_ingredient')?.addEventListener('click', function() {
        console.log("Add ingredient clicked");
        addIngredient();
    });

    document.getElementById('add_step')?.addEventListener('click', function() {
        console.log("Add step clicked");
        addStep();
    });

    document.getElementById('ingredients-container')?.addEventListener('click', removeIngredient);
    document.getElementById('steps-container')?.addEventListener('click', removeStep);
});