from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return "About Me"

@app.route("/skills")
def skills():
    return "My skills"

@app.route("/projects")
def projects():
    return "My projects"

@app.route("/contact")
def contact():
    return "My Contact"


if __name__ == "__main__":
    print(__name__)
    app.run( debug = True )
    
