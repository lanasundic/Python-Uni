#da korisnik unese broj i da mi provjerimo da li su brojevi u opadajucem poretku

broj = int(input("Unesite broj:"))
s = str(broj)
l = list(s)
l.sort(reverse = True)
t = "".join(l)
print(s==t)

#pretvorimo bbroj u string string u lustu joinujemo...