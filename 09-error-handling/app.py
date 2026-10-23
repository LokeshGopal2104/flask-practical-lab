from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Error Handling Lab!"


@app.route("/page")
def page():
    return "This page exists!"


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500

@app.route("/test-error")
def test_error():
    raise RuntimeError("Testing the 500 error handler")

if __name__ == "__main__":
    app.run(debug=False)