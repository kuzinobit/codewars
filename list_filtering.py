def filter_list(l):
    new_l = []
    for element in l:
        if type(element) is int and element >= 0:
            new_l.append(element)
    return new_l

print(filter_list([1,2,'a','b']))