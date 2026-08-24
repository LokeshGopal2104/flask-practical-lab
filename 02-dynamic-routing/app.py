from flask import Flask, render_template

app = Flask(__name__)

@app.route("/profile/<username>")
def profile(username):
    return render_template(
        "profile.html",
        username = username
    )

@app.route("/product/<int:product_id>")
def product(product_id):
    return render_template(
        "product.html",
        product_id = product_id
    )

@app.route("/search/<path:query>")
def search(query):
    return render_template(
        "search.html",
        query = query.split("/")
    )

if __name__ == '__main__':
    app.run( debug= True)