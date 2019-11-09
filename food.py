from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["get","post"])
def home():
    return render_template('index.html')

@app.route("/recipe", methods=["get","post"])
def display_recipe():

    ing = request.form.getlist["ingredients"]

    return "Ingredients: " + str(ing)# + ing1 + ", " + ing2 + ", " + ing3

if __name__ == "__main__":
    app.run()
