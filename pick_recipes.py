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
SPECIAL_UNIT_ITEMS = ["eggs", "milk", "ice cream"]
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
            #print(recipe[good])
            if good != "Title":
                if not (good.lower() in lower_list(pantry)):
                    to_buy.append(good)
                    #will give us the cost of the food in this recipe
                    cost += recipe[good]
        if cost < max_cost:
            #add this recipe to matches
            matches.append([recipe, to_buy])
    return matches

#convert raw_list of strings into a list with all lower case values (return new list)
def lower_list(raw_list):
    lower = []
    for elem in raw_list:
        lower.append(elem.lower())
    return lower
"""
    :param recipes: a list of recipes, where is recipe is a dictionary of food:quanity pairs
    NOTE: eggs, milk, and ice cream have special units!!!
"""
def get_prices(recipes, available):
    recipes_costs = []
    for recipe in recipes:
        rec_cost = {}
        for item in recipe:
            #add this item and its price to the recipe price dictionary
            #recipe[item] should be a float representing pounds needed
            rec_cost[item] = recipe[item] * available[item]
        recipes_costs.append(rec_cost)
    return recipes_costs

"""
def special_unit_price(available, item, amount):
    if item == "eggs":
        #num eggs dozens * 12 * egg price
        return
    return 420.0
"""

def make_recipies(path):
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

if __name__ == "__main__":
    #load all recipe files in RECIPE_DIR into some list
    #available = load_available_ingredients("Basic_Ing.csv")
    #print(available)

    #A test: what recipies can we make given this food
    #hardcoding to test stuff out
    my_recps = make_recipies("Recipes_Prices.csv")
    #print(my_recps)
    recipe_list = [{"bread": 1.0, "oil": 4.0, "butter": 17.0}]
    user_pantry = get_user_foods()
    budget = float(input("What's your budget? "))

    matching = match_recipes(user_pantry, my_recps, budget)

    print("YOUR RECIPES ma'am:", matching)
    #print(my_recps)
