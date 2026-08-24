# Flask Dynamic Routing — Task 02

## Project Overview

This project is the second task in my practical Flask learning roadmap.

The objective is to convert my theoretical understanding of Flask dynamic routing
into a practical implementation.

The application demonstrates how dynamic route parameters can be captured from
a URL, passed to Flask view functions, and then passed to Jinja templates to
generate dynamic HTML content.

---

## Learning Objectives

- Understand dynamic URL parameters in Flask.
- Understand the relationship between route parameters and view-function parameters.
- Pass dynamic route values from Flask to Jinja templates.
- Understand how the same template can display different content based on URL data.
- Understand required dynamic route parameters.
- Understand Flask route converters.
- Use the `int` route converter.
- Understand the `float` route converter.
- Understand the `path` route converter.
- Understand how route converters affect URL matching.
- Understand basic resource-oriented route design.
- Test dynamic routes with valid and invalid inputs.

---

## Features

- Dynamic profile routes using usernames.
- Dynamic product routes using integer product IDs.
- Search route using Flask's `path` converter.
- Dynamic content rendered using Jinja.
- Integer route validation using `<int:product_id>`.
- Multiple dynamic URL values handled by the same route.
- Invalid route values resulting in 404 responses.

---

## Project Structure

```text
02-dynamic-routing/
│
├── app.py
│
├── templates/
│   ├── profile.html
│   ├── product.html
│   └── search.html
│
└── README.md