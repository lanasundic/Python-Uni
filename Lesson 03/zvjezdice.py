n = int(input("Unesite N:"))

s = " "*(n-1)+"*" +" "*(n-2)
l, r = n-2, n

lista = []

for i in range[n]:
    lista.append(s)
s = s[:l]+"*"+s[l+1:r]+"*"+s[r+1:]
l-=1
r+=1

for i in range(n):
    print(s)
    s = s[:l]+"*"+s[l+1:r]+"*"+s[r+1:]
    l-=1
    r+=1
    
#da korisnik unese broj i da mi provjerimo da li su brojevi u opadajucem poretku