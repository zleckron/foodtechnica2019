from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():

        return render_template('index.html')

@app.route("/recipe", methods=["get", "post"])
def recipe():

    if request.method == 'POST':
        #return request.form
        ing1 = request.form["ing1"]
        ing2 = request.form["ing2"]
        ing3 = request.form["ing3"]

        return "Ingredients: " + str(ing1) + ing2 + ing3

    else:
        print(request.method)
        return ("fuck me")


if __name__ == "__main__":
    app.run()
