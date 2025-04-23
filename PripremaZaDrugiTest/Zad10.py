#10. Napisati program koji broji koliko puta se svaki karakter javlja u datom stringu.

string = input("Unesite string: ")
brojac = {}

for karakter in string:
    if karakter in brojac:
        brojac[karakter] += 1
    else:
        brojac[karakter] = 1

