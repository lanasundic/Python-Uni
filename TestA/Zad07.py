s1 = "abaad"
s2 = "bacab"
st1 = set(s1)   # abd
st2 = set(s2)   # bac

print(st1 ^ st2)    #svi elementi koji nisu zajednicki - stampa - {'d', 'c'}
