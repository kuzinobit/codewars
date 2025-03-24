def tower_builder(n_floors):
    floor = "*"
    lst = []
    for i in range(n_floors):
        lst.append(" "*(n_floors-i-1)+floor+" "*(n_floors-i-1))
        floor += "**"
    return lst

print(tower_builder(5))