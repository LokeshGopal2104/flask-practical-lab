from flask import render_template


def register_routes(app):

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/about")
    def about():
        return "This is the About page."