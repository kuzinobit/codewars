def cakes(recipe, available):
    number_cakes = 0
    number_available = []
    for key_r in recipe.keys():
        if key_r in available.keys():
            print(key_r)
            number_available.append(available.get(key_r) // recipe.get(key_r))
        else:
            return number_cakes
    number_cakes = min(number_available)
    return number_cakes

cake = cakes({'flour': 200, 'sugar': 200},
             {'flour': 1200, 'eggs': 5, 'milk': 200})

print(cake)