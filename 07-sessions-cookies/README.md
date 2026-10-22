# Task 07 — Sessions and Cookies

## Objective
Understand how cookies and Flask sessions preserve information across HTTP requests.

## Concepts Learned
- Creating cookies with `response.set_cookie()`
- Reading cookies with `request.cookies.get()`
- Setting cookie expiration with `max_age`
- Deleting cookies with `response.delete_cookie()`
- Configuring Flask's `secret_key`
- Storing and reading session data
- Removing individual session values using `session.pop()`
- Handling forms with GET and POST
- Using sessions to remember a username across routes
- Removing session data during logout

## Project Structure

```text
07-sessions-cookies/
├── app.py
├── README.md
└── templates/
    ├── home.html
    └── profile.html
```

## Routes

| Route | Purpose |
|---|---|
| `/` | Displays the cookie demonstration home page |
| `/set-cookie` | Creates a username cookie |
| `/read-cookie` | Reads the username cookie |
| `/delete-cookie` | Deletes the username cookie |
| `/set-session` | Stores a username in the session |
| `/read-session` | Reads the session username |
| `/delete-session` | Removes the username from the session |
| `/login` | Displays the form and stores the submitted username |
| `/profile` | Displays the username stored in the session |
| `/logout` | Removes the username from the session |

## How to Run

From the repository root:

```powershell
python .\07-sessions-cookies\app.py
```

Open `http://127.0.0.1:5000/login` to test the username form and session-based profile.

## Security Notes
- Flask's default session mechanism stores session data in a signed cookie.
- A signature helps detect tampering but does not encrypt the session contents.
- Use a strong, unpredictable secret key and store it in an environment variable in real applications.
- Never store passwords or sensitive secrets in Flask's default session cookie.
- Validate user input on the server.

## Key Takeaway
Cookies are browser-stored data sent with matching requests. Flask sessions provide a convenient interface for remembering small pieces of user-specific data across requests.