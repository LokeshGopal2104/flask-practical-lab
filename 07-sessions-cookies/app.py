from flask import Flask, make_response, request, render_template, session

app = Flask(__name__)

app.secret_key = "Hello"


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/set-cookie")
def set_cookie():
    response = make_response("Cookie has been set for one!")
    response.set_cookie("username", "Lokesh", max_age = 3600)
    return response

@app.route("/read-cookie")
def read_cookie():
    username = request.cookies.get("username")

    if username :
        return f"Welcome back, {username}"

    return "No username cookie found"

@app.route("/delete-cookie")
def delete_cookie():
    response = make_response("Username cookie deleted!")
    response.delete_cookie("username")
    return response

@app.route("/set-session")
def set_session():
    session["username"] = "Lokesh"
    return "Username stored in session!"

@app.route("/read-session")
def read_session():
    username = session.get("username")

    if username:
        return f"Welcome back, {username}!"

    return "No username found in session."


@app.route("/delete-session")
def delete_session():
    session.pop("username", None)
    return "Username removed from session!"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()

        if not username:
            return "Username cannot be empty.", 400

        session["username"] = username
        return "Username saved in session! Visit /profile."

    return render_template("home.html")



@app.route("/profile")
def profile():
    username = session.get("username")

    if not username:
        return "Please enter your name first at /login.", 401

    return render_template("profile.html", username=username)


@app.route("/logout")
def logout():
    session.pop("username", None)
    return "You have been logged out."



if __name__ == "__main__":
    app.run(debug=True)