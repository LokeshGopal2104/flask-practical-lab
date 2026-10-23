from flask import Flask, render_template, flash, redirect, url_for


app = Flask(__name__)
app.secret_key = "secretKey"


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/success")
def success():
    flash("Your action was completed successfully!", "success")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)