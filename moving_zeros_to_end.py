def move_zeros(lst):
    lst_one = []
    lst_two = []
    for element in lst:
        if element == 0:
            lst_two.append(element)
        else:
            lst_one.append(element)
    lst = lst_one + lst_two
    return lst

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))