e = 0.5
t = 1
s = 0
i, j = 1, 1

while t >= e:   
    s += t  #s = 1  s = 1.75    s = 1.75+0.55 = 2.3
    i += 2  #i = 3  i = 5   i = 7
    j += 1  #j = 2  j = 3   j = 5
    t = i / (j ** 2)    #t = 3 / (klas. mat dijeljenje) 4 = 0.75    t = 5 / 9 = 0.55    t = 0.28

print(s)    #stampa - 2.3