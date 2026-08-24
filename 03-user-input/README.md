# Flask User Input — Task 03

## Project Overview

This project is the third task in my practical Flask learning roadmap.

The objective is to understand how Flask receives user input through URL query
parameters, retrieves the input from the request object, validates and
normalizes the value, and passes it to a Jinja template for dynamic rendering.

The application implements a simple greeting system where a user provides their
name through a query parameter.

---

## Learning Objectives

- Understand URL query parameters.
- Understand the difference between path parameters and query parameters.
- Understand Flask's `request` object.
- Access query parameters using `request.args`.
- Retrieve query parameter values using `request.args.get()`.
- Handle missing query parameters.
- Handle empty query parameter values.
- Normalize user input using `.strip()`.
- Validate user input using Python truthiness.
- Pass request data from Flask to Jinja templates.
- Understand that query parameter values are received as strings.
- Understand multiple query parameters.
- Understand repeated query parameters.
- Understand `request.args.getlist()` conceptually.

---

## Features

- Accepts a user's name through a URL query parameter.
- Dynamically displays the provided name.
- Handles missing name input.
- Handles empty name input.
- Removes leading and trailing whitespace from input.
- Validates the cleaned input before rendering.
- Displays a meaningful message when a usable name is not provided.
- Supports multiple query parameters.
- Demonstrates repeated query parameter behavior.

---

## Project Structure

```text
03-user-input/
│
├── app.py
│
├── templates/
│   └── greet.html
│
└── README.md