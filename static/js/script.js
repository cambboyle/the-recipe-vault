function addIngredient(value = '') {
    const container = document.getElementById('ingredients-container');
    if (!container) return;

    const ingredientCount = container.children.length;
    if (ingredientCount >= 25) {
        alert("You can only add up to 25 ingredients.");
        return;
    }

    const newField = document.createElement('div');
    newField.className = 'ingredient-input mb-2';
    newField.innerHTML = `
        <div class="input-group">
            <input type="text" class="form-control" name="main_ingredients" placeholder="Add Ingredient" value="${value}" required>
            <button class="btn btn-danger remove_ingredient" type="button">Remove</button>
        </div>
    `;
    container.appendChild(newField);
}

function addStep(content = '') {
    const container = document.getElementById('steps-container');
    if (!container) return;

    const stepCount = container.children.length;
    if (stepCount >= 25) {
        alert("You can only add up to 25 steps.");
        return;
    }

    const newField = document.createElement('div');
    newField.className = 'step-input mb-2';
    newField.innerHTML = `
        <div class="input-group">
            <span class="input-group-text">Step ${stepCount + 1}</span>
            <textarea class="form-control" name="recipe_method" rows="2" placeholder="Describe this step" required>${content}</textarea>
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

    console.log('addIngredientButton:', addIngredientButton);
    console.log('addStepButton:', addStepButton);
    console.log('ingredientsContainer:', ingredientsContainer);
    console.log('stepsContainer:', stepsContainer);

    if (addIngredientButton && ingredientsContainer) {
        addIngredientButton.addEventListener('click', () => addIngredient());
        ingredientsContainer.addEventListener('click', removeIngredient);
    }

    if (addStepButton && stepsContainer) {
        addStepButton.addEventListener('click', () => addStep());
        stepsContainer.addEventListener('click', removeStep);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    navbarToggler.addEventListener('click', () => {
      if (navbarCollapse.classList.contains('show')) {
        navbarCollapse.classList.remove('show');
      } else {
        navbarCollapse.classList.add('show');
      }
    });
});

// Ensure the script runs after the DOM content is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM fully loaded');
    initializeRecipeForm();
});