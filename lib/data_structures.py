import ipdb 

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return([i["name"] for i in spicy_foods])

    #Non-list comprehension way 
    # spicy_foods_names = []
    # for i in spicy_foods: 
    #     spicy_foods_names.append(i["name"])
    # return spicy_foods_names
    
def get_spiciest_foods(spicy_foods):
    return([i for i in spicy_foods if i["heat_level"] > 5])

def print_spicy_foods(spicy_foods):
    for i in spicy_foods:
        print(f'{i["name"]} ({i["cuisine"]}) | Heat Level: {i["heat_level"] * "🌶"}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for i in spicy_foods: 
        if i["cuisine"] == cuisine: 
            return i 

    #This list comprehension method works but isn't accepted by the test.   
    # return([i for i in spicy_foods if i["cuisine"] == cuisine])

def print_spiciest_foods(spicy_foods):
    for i in spicy_foods:
        if i["heat_level"] > 5:
            print(f'{i["name"]} ({i["cuisine"]}) | Heat Level: {i["heat_level"] * "🌶"}')

def get_average_heat_level(spicy_foods):
    total_heat_level = sum([i["heat_level"] for i in spicy_foods])
    av_heat_level = total_heat_level / len(spicy_foods)
    return av_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
