s1 = "bcae"
s2 = "cdba"
st1 = set(s1)   #{'b', 'c', 'a', 'e'}
st2 = set(s2)   #{'c', 'd', 'b', 'a'}
print(st1 ^ st2)    #stampa - {'e', 'd'}