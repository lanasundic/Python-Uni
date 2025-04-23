#11. Napisati program koji provjerava da li je unijeti string palindrom.

tekst = input("Unesite string: ")

if tekst == tekst[::-1]:
    print("Uneseni string je palindrom.")
else:
    print("Uneseni string nije palindrom.")

