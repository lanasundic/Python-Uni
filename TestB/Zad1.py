a = [1, 2, 3, 4]
b = []
for e in a:
    if e%2 == 0:    #2, 4
        b.append(e)
    b.append(e)

print(b)    #stampa - [1, 2, 2, 3, 4, 4]