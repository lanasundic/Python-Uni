e = 0.5
t = 1
s = 0
i, j = 1, 1

while t >= e:   #jer je >= petlja ce da se odradi 2 puta
    s += t  #s = 1  s = 1.75
    i += 2  #i = 3  i = 5
    j += 1  #j = 2  j = 3
    t = i / (j ** 2)    #t = 3 / (klas. mat dijeljenje) 4 - 0.75    

print(s)    #stampa - 1.75