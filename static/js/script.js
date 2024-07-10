// Initialization for ES Users
 // import { Modal, Button, Ripple, initMDB } from "mdb-ui-kit";

// initMDB({ Modal, Button, Ripple });


// Recipe Form

function addIngredient() {
    const container = document.getElementById('ingredients-container');
    if (!container) return;

    const newField = document.createElement('div');
    newField.className = 'ingredient-input mb-2';
    newField.innerHTML = `
        <div class="input-group">
            <input type="text" class="form-control" name="ingredients[]" placeholder="Add Ingredient" required>
            <button class="btn btn-outline-secondary remove-ingredient" type="button">Remove</button>
        </div>
    `;
    container.appendChild(newField);
}

function addStep() {
    const container = document.getElementById('steps-container');
    if (!container) return;

    const stepCount = container.children.length + 1;
    const newField = document.createElement('div');
    newField.className = 'step-input mb-2';
    newField.innerHTML = `
        <div class="input-group">
            <span class="input-group-text">Step ${stepCount}</span>
            <textarea class="form-control" name="steps[]" rows="2" placeholder="Describe this step" required></textarea>
            <button class="btn btn-outline-secondary remove-step" type="button">Remove</button>
        </div>
    `;
    container.appendChild(newField);
}

function removeIngredient(event) {
    if (event.target.classList.contains('remove-ingredient')) {
        event.target.closest('.ingredient-input').remove();
    }
}

function removeStep(event) {
    if (event.target.classList.contains('remove-step')) {
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
    const addIngredientButton = document.getElementById('add-ingredient');
    const addStepButton = document.getElementById('add-step');
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
}

// Call initializeRecipeForm when the DOM is loaded
document.addEventListener('DOMContentLoaded', initializeRecipeForm);