from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "greet.html"
    )

@app.route("/greet", methods = ["POST"])
def greet():
    name = request.form.get("name")

    if name is not None:
        name = name.strip()
    if not name :
        return render_template(
            "greet.html",
            name = "Please provide your name"
        )
    

    # print(repr(name))

    age = request.form.get("age")

    if not age:
        return render_template(
            "greet.html",
            name=name,
            age="Please provide your age"
        )

    try:
        age = int(age)
    except ValueError:
        return render_template(
            "greet.html",
            name=name,
            age="Please provide a valid age"
        )

    if age < 1 or age > 120:
        return render_template(
            "greet.html",
            name=name,
            age="Please provide a valid age from 1 to 120"
        )

    return render_template(
        "greet.html",
        name = name,
        age = age
    )


if __name__ == "__main__":
    app.run(debug=True)
