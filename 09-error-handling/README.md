# Task 09 — Error Handling

## Objective
Learn how to handle common HTTP errors in Flask and display custom error pages.

## Concepts Covered
- HTTP 404 — Not Found
- HTTP 500 — Internal Server Error
- Flask `@app.errorhandler()` decorator
- Custom error templates
- Jinja template inheritance
- HTTP response status codes

## Routes
- `/` — Displays the home page.
- `/page` — Displays an existing page.
- Unmatched URLs — Display the custom 404 page.
- `/test-error` — Temporary route used to test the 500 handler; remove after testing.

## Error Handlers
- `@app.errorhandler(404)` renders `404.html` with status code 404.
- `@app.errorhandler(500)` renders `500.html` with status code 500.

## Key Learning
Custom error pages improve the user experience by providing clear messages instead of generic error pages. They should not expose sensitive internal details.

## Run the Application
From the repository root:

```bash
python 09-error-handling/app.py
```

Open `http://127.0.0.1:5000/`.

## Development Note
Debug mode is useful during development but should not be enabled in production. Use a production-ready server and configuration when deploying.
