def cakes(recipe, available):
    number_cakes = 0
    for key in recipe.keys():
        if key in available.keys():
            print(True)
        else:
            print(False)
    return number_cakes

cake = cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 500, "sugar": 200, "salt": 1})