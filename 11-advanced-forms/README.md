
# Task 11 — Advanced Forms

## Overview
A student registration application built using Flask, HTML, CSS,
and Jinja. This project demonstrates how to collect, validate,
process, and display multiple form fields.

## Learning Objectives
- Handle multiple HTML form inputs.
- Use dropdowns, radio buttons, and checkboxes.
- Understand required and optional fields.
- Retrieve submitted values using Flask request.form.
- Retrieve multiple checkbox values using request.form.getlist().
- Implement basic server-side validation.
- Pass Python variables to Jinja templates.
- Use Jinja variables, conditions, and loops.
- Organize templates and static CSS files.

## Features
- Student name, email, age, and optional phone number.
- Course selection using a dropdown.
- Study mode selection using radio buttons.
- Multiple skill selection using checkboxes.
- Required-field and age validation.
- Registration summary rendered using Jinja.
- Responsive CSS styling.

## Project Structure
11-advanced-forms/
├── app.py
├── README.md
├── static/
│   └── style.css
└── templates/
    ├── register.html
    └── result.html

## Technologies
- Python
- Flask
- HTML5
- CSS3
- Jinja

## How to Run
1. Activate your existing virtual environment, if applicable.
2. Install Flask if it is not already installed:
   pip install flask
3. Navigate to the task directory:
   cd 11-advanced-forms
4. Run the application:
   python app.py
5. Open http://127.0.0.1:5000/ in your browser.

## Key Concepts
- GET and POST methods
- request.form.get()
- request.form.getlist()
- Server-side validation
- render_template()
- Jinja variables, conditions, and loops
- url_for() for static CSS files

## Limitations
- Submitted data is displayed but not saved to a database.
- Authentication and persistent student records are not implemented.
- Production applications require stronger input validation and security.

## Status
Completed after implementation and testing.
