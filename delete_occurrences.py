def delete_nth(order,max_e):
    count = {}
    result = []
    for i in order:
        if i not in count:
            count[i] = 0
        count[i] += 1
        if count[i] <= max_e:
            result.append(i)
    return result

print(delete_nth([20,37,20,21], 1))
print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))