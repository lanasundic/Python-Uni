a = [1, 2, 3, 4]
b = []
for e in a:
    if e%2 == 1:    #ako je broj neparan - 1 3
        b.append(e) #onda na skup b dodaj taj broj
    b.append(e) #opet dodaj u skup taj broj??? 

print(b) # stampa se [1, 1, 2, 3, 3, 4]

