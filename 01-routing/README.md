# Flask Routing — Task 01

## Project Overview

This project is the first task in my practical Flask learning roadmap.

The goal of this project is to convert my theoretical understanding of Flask routing, templates, navigation, static files, and Jinja into practical implementation.

The application is a simple multi-page personal portfolio website built using Flask, HTML, and CSS.

## Learning Objectives

- Understand how Flask maps URLs to Python functions.
- Implement multiple routes in a Flask application.
- Understand Flask view functions and HTTP responses.
- Handle 404 errors caused by undefined routes.
- Understand trailing slash behavior in routes.
- Render HTML pages using `render_template()`.
- Understand the role of the `templates/` directory.
- Implement navigation between multiple pages.
- Generate dynamic URLs using Flask's `url_for()`.
- Understand basic Jinja template expressions.
- Serve CSS using Flask's `static/` directory.
- Use Flexbox for basic page navigation styling.
- Practice debugging Flask template errors.

## Features

- Multi-page Flask application.
- Home, About, Skills, Projects, and Contact pages.
- Flask routing for each page.
- HTML templates rendered using `render_template()`.
- Navigation bar available on all pages.
- Dynamic URL generation using `url_for()`.
- Shared CSS stylesheet served from the `static/` directory.
- Basic Flexbox-based navigation styling.
- Flask development server with debug mode.
- Basic error handling and debugging practice.

## Project Structure

```text
01-routing/
│
├── app.py
├── README.md
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── skills.html
│   ├── projects.html
│   └── contact.html
│
└── static/
    └── style.css