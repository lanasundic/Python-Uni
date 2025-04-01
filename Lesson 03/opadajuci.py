#da korisnik unese broj i da mi provjerimo da li su brojevi u opadajucem poretku

broj = int(input("Unesite broj:"))  #koristnik unosi broj - npr. 54321
s = str(broj)   #pretvaramo broj u string kako bismo mogli obraditi svaku cifru - "54321"
l = list(s)     #pretvaramo string u listu karaktera - l = ['5', '4', '3', '2', '1']
l.sort(reverse = True)  #sortiramo listu u opadajucem poretku
t = "".join(l)      #spajamo sortirane cifre nazad u string
print(s==t)     #uporedjujemo originalni broj i sortiranu verziju

#pretvorimo broj u string, string u listu joinamo...