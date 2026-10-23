# Task 10 — Flask Project Structure

## Objective
Learn how to organize a Flask application into separate Python modules.

## Concepts Covered
- Python modules and packages
- Importing functions between files
- Separating application setup from routes
- Registering routes using a function
- Flask template organization
- Organizing static files

## Project Structure
- `app.py` — Creates and runs the Flask application.
- `routes/main.py` — Defines and registers the home and about routes.
- `routes/__init__.py` — Marks the routes directory as a Python package.
- `templates/home.html` — Contains the home page HTML.
- `static/` — Stores static assets such as CSS, JavaScript, and images.

## Routes
- `/` — Displays the home page.
- `/about` — Displays the About page.

## Key Learning
Separating routes from application setup makes a Flask application easier to read, maintain, and extend as it grows.

## Run the Application
From the repository root:

```bash
python 10-project-structure/app.py
```

Open `http://127.0.0.1:5000/` in your browser.
