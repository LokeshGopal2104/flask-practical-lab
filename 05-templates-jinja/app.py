from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "home.html",
        users=[
            {"name": "lokesh", "age": 22},
            {"name": "rahul", "age": 16},
            {"name": "arun", "age": 25}
        ]
    )


if __name__ == "__main__":
    app.run(debug=True)