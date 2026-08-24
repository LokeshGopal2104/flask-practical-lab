from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/greet")
def greet():


    name = request.args.get("name")

    if name is not None:
        name = name.strip()

    if(not name):
        return render_template(
            "greet.html",
            name = "Please provide your name"
        )
    
    return render_template(
        "greet.html",
        name = name
    )

if __name__ == "__main__":
    app.run(debug=True)
