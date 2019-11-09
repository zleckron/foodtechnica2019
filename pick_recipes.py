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
    food_item = input("Enter a food, \"QUIT\" to exit: ")
    while food_item != QUIT:
        pantry.append(food_item)
        food_item = input("Enter a food, \"QUIT\" to exit: " )
    return pantry

"""
    CN: Reconsier recipe structure -- should hold quantity of each item
    Can write a file for content to cost conversion
    assuming recipes is a list of dictionaries (we will worry later about storing the instructions)
    the dictionary holds "ingredient":price pairs
    will return a 3D list holding [recipe, []] <-- with the second element as a list of to_buy goods
"""
def match_recipes(pantry, recipes, max_cost):
    matches = []
    #for every recipe, get the price difference we would need to complete it
    #CN: ASSUMING 1 POUND/DOZEN/GALLON OF EVERYTHING NEEDED
    for recipe in recipes:
        cost = 0.0
        to_buy = []
        needed_goods = recipe.keys()
        #for each ingredient required, we only care if we don't already have it
        #TODO: let user indicate quantity of ingredients that they have
        for good in needed_goods:
            if not (good in pantry):
                to_buy.append(good)
                #will give us the cost of the food in this recipe
                cost += recipe[good]
        if cost < max_cost:
            #add this recipe to matches
            matches.append([recipe, to_buy])
    return matches

if __name__ == "__main__":
    #load all recipe files in RECIPE_DIR into some list
    #available = load_available_ingredients("Basic_Ing.csv")
    #print(available)
    user_pantry = get_user_foods()

    #A test: what recipies can we make given this food
    #hardcoding to test stuff out
    recipe_list = [{"eggs": 1.0, "milk": 4.0, "butter": 17.0}]

    matching = match_recipes(user_pantry, recipe_list, MAX_PRICE_HARDCODE)

    print(matching)
