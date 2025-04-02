def f(s, ss, t, o):
    u = t[0]*ss[s][0] + t[1]*ss[s][1] + t[2]*ss[s][2]   #81
    i = max(int(u - 40), 0)//10     #41//10 = 4
    return o[i] #B

ss = {"Marko":[60, 70, 90],
      "Ana":[100, 80, 90],
      "Aleksa":[50, 60, 50],
      "Marija":[90, 70, 80]}

o = ("F", "E", "D", "C", "B", "A")
t = (0.4, 0.3, 0.3)

print(f("Marija", ss, t, o))    #stampa - B
