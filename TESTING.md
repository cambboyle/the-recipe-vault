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

### Mobile (iPhone 12 Pro Max)

| Page | Screenshot |
| --- | --- |

### Tablet (iPad Air)

| Page | Screenshot |
| --- | --- |

</details>

## LIGHTHOUSE TESTING

### Desktop Lighthouse

![Desktop Lighthouse](documentation/other_images/validation/LighthouseDesktop.png)

### Mobile Lighthouse

![Mobile Lighthouse](documentation/other_images/validation/LighthouseMobile.png)

## DEFENSIVE PROGRAMMING

## KNOWN BUGS

No known bugs.

## FIXED BUGS

One bug was fixed in the project, which was a bug in the recipe editing page.

The add ingredient/step button was not creating more ingredients/steps when clicked.

This was fixed in by adding the appropriate JavaScript code from the script.js file to the edit_recipe.html file.

The issue also persisted on the add recipe page, so this was also fixed.
