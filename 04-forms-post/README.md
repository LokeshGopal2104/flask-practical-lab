# Flask Forms and POST — Task 04

## Project Overview

This project is the fourth task in my practical Flask learning roadmap.

The objective is to understand how HTML forms submit user input to Flask using the POST method, how Flask retrieves submitted form data using `request.form`, and how user input can be validated before being rendered using Jinja templates.

The application implements a simple greeting form that accepts a user's name and age.

---

## Learning Objectives

- Understand HTML forms.
- Understand the `form` element.
- Understand the `action` attribute.
- Understand the `method` attribute.
- Understand the POST method.
- Understand the `name` attribute of form inputs.
- Understand Flask's `request.form`.
- Retrieve multiple form fields.
- Normalize input using `.strip()`.
- Validate missing and empty input.
- Convert string input to integers using `int()`.
- Handle invalid integer conversion using `try/except`.
- Validate age using a numerical range.
- Understand client-side and server-side validation.
- Understand the difference between GET and POST.
- Understand `request.args` versus `request.form`.

---

## Features

- HTML form for collecting name and age.
- Form submission using POST.
- Dynamic greeting using Jinja.
- Name input normalization.
- Name validation.
- Age validation.
- String-to-integer conversion.
- Invalid age handling.
- Age range validation from 1 to 120.
- GET versus POST experimentation.

---

## Project Structure

```text
04-forms-post/
│
├── app.py
│
├── templates/
│   └── greet.html
│
└── README.md