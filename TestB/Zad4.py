e = 1/2 #0.5
t = 1
s = 0
i, j = 1, 1

while t >= e:
    s += t  #s = 1  #s = 1.75  s = 2.25
    i += 2  #i = 3  #i = 5
    j += 1  #j = 2  #j = 3
    t = i / (j ** 2) #t = 0.75  t = 0.55 ~ 0.5

print(s)    #stampa - 2.25