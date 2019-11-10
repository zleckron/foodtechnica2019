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

def make_recipes(path):
    recipes = []
    recipefp = open(path, "r")
    recipes_lines = recipefp.readlines()
    recipefp.close()
    #for each line, first item is the title
    for raw_line in recipes_lines:
        line = raw_line.strip()
        new_recipe = {}
        line_data = line.split(COMMA)
        #print(line_data)
        #remember that the first
        new_recipe["Title"] = line_data[0]
        for i in range(1, len(line_data) - 2, 2):
            new_recipe[line_data[i]] = float(line_data[i+1])
        recipes.append(new_recipe)
    return recipes

def give_recipes(user_ingredients):
    #cut off the last value in the dict (it's the budget)
    matching = match_recipes(dict.values()[:-1], make_recipes("Recipes_Prices.csv"), budget[-1])
    return render_template('results.html', ingredients_list=ingredients)

if __name__ == "__main__":
    app.run()
