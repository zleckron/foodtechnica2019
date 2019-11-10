from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():

    ingredients = ["White Flour","White Rice","Pasta","Bread","Chocolate Chip Cookies","Uncooked Ground Beef",
        "Uncooked Beef Roasts","Uncooked Beef Steaks","Bacon","Pork Chops","Ham","Bologna","Chicken Breast","Chicken Leg",
        "Turkey","Eggs","Milk","Cheddar Cheese","Ice Cream","Bananas","Oranges","Grapes","Lemons","Peaches","White Potatoes",
        "Iceberg Lettuce","Tomatoes","Broccoli","Sweet Peppers","Orange Juice","Beans","White Sugar","Margarine"]

    return render_template('index.html', ingredients_list=ingredients)

@app.route("/recipe", methods=["get", "post"])
def recipe():

    if request.method == 'POST':

        #return "Ingredients: " + ing1 + ing2 + ing3

        return request.form

    else:
        print(request.method)
        return ("oh no")

if __name__ == "__main__":
    app.run()
