# Task 06: Flask Static Files and CSS

## Objective
Learn how to serve static files in Flask, connect an external CSS stylesheet to HTML templates, and reuse common styling across multiple pages using Jinja template inheritance.

## Concepts Learned
- Flask's `static` directory
- Serving CSS files
- Using `url_for('static', filename='css/style.css')`
- Linking external CSS with the HTML `<link>` element
- Template inheritance using `{% extends %}` and `{% block %}`
- Shared layouts using `base.html`
- Multiple Flask routes and navigation using `url_for()`
- Page-specific browser titles

## Project Structure
```text
06-static-files-css/
├── app.py
├── README.md
├── templates/
│   ├── base.html
│   ├── home.html
│   └── about.html
└── static/
    └── css/
        └── style.css
```

## How It Works
1. `app.py` defines the Home and About routes.
2. Flask renders the corresponding HTML templates.
3. `base.html` contains the shared HTML layout, navigation, and CSS link.
4. `home.html` and `about.html` extend `base.html` and provide page-specific content.
5. `style.css` controls the appearance of both pages.
6. `url_for()` generates URLs for routes and static files.

## How to Run
From the repository root, run:

```powershell
python .\06-static-files-css\app.py
```

Open these URLs in your browser:

- Home: `http://127.0.0.1:5000/`
- About: `http://127.0.0.1:5000/about`

## Key Takeaway
Flask's static-file support lets us keep CSS separate from HTML. Combined with Jinja template inheritance, it allows multiple pages to share the same stylesheet and layout without unnecessary duplication.