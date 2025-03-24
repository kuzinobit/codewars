def order(sentence):
    words = sentence.split()
    return ' '.join(sorted(words, key=lambda word: int([int(c) for c in word if c.isdigit()][0])))

print(order("is2 Thi1s T4est 3a"))
print(order(""))