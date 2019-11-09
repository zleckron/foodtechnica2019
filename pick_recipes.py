"""
    Updated November 9th 2019
    Author: Zoee Leckron (github.com/zleckron)
    Run with python3 pick_recipes.com
"""
RECIPE_DIR = "./recipes/"
COMMA = ','
INGREDIENT_INDEX = 0
PRICE_INDEX = 1
QUIT = "QUIT"
MAX_PRICE_HARDCODE = 15.0
"""
    load_available_ingredients(path)
    :params: path -- a string specifying relative path to the file
    :return: dictionary of strings with ingredient:price
    #special case for eggs (per dozen), milk per gallon, ice cream per gallon
"""
def load_available_ingredients(path):
    ingredients = {}
    ingredientfp = open(path, "r")
    ingredient_lines = ingredientfp.readlines()
    ingredientfp.close()
    #each line has ingredient, price per pound
    for line in ingredient_lines:
        #print(line)
        line_data = line.split(COMMA)
        ingredients[line_data[INGREDIENT_INDEX]] = line_data[PRICE_INDEX]
    return ingredients

"""
    CN: THIS WILL CHANGE, just here for testing
"""
def get_user_foods():
    pantry = []
    food_item = input("Enter a food, \"QUIT\" to exit")
    while food_item != QUIT:
        pantry.append(food_item)
    return pantry

if __name__ == "__main__":
    #load all recipe files in RECIPE_DIR into some list
    available = load_available_ingredients("Basic_Ing.csv")
    print(available)
    pantry = get_user_foods

    #A test: what recipies can we make given this food
