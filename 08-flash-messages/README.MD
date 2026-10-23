# Task 08 — Flash Messages

## Objective
Learn how to display temporary messages in a Flask application using flash messages and redirects.

## Concepts Covered
- Flask `flash()` function
- Displaying messages using `get_flashed_messages()`
- Flash message categories
- Redirecting using `redirect()` and `url_for()`
- Template inheritance using Jinja
- Flask secret key requirement

## Routes
- `/` — Displays the home page and any pending flash messages.
- `/success` — Creates a success flash message and redirects to the home page.

## How It Works
1. The user visits the success route.
2. Flask creates a temporary flash message.
3. Flask redirects the browser to the home route.
4. The home page retrieves and displays the message.
5. The message is consumed after retrieval.

## Key Learning
Flash messages are useful for providing temporary feedback after actions such as form submissions, registration, login, and data updates.

Redirecting after an action also helps prevent accidental repetition of the original request when the user refreshes the destination page.

## Run the Application
From the repository root, run:

```bash
python 08-flash-messages/app.py
```

Open `http://127.0.0.1:5000/` in your browser.

## Security Note
The application uses a development-only secret key. A real application should use a strong secret key stored securely in an environment variable.
