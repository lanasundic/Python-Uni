#6. Napisati program koji za unijeti datum i mjesec rođenja štampa horoskopski znak osobe. 

dan = input("Unesite dan rodjenja: ")
mjesec = input("Unesite mjesec rodjenja: ")

granice = [
    "01-20",
    "02-19",
    "03-21",
    "04-20",
    "05-21",
]
znaci = ["vodolija", "ribe", "ovan", "bik", "blizanci"]
for i in range(4, -1, -1):
    spojeni_dan = mjesec + "-" + dan
    if (spojeni_dan >= granice[i]):
        print(znaci[i])
        break



# if (mjesec == 1 and dan >= 20) or (mjesec == 2 and dan <= 18):
#     znak = "Vodolija"
# elif (mjesec == 2 and dan >= 19) or (mjesec == 3 and dan <= 20):
#     znak = "Ribe"
# elif (mjesec == 3 and dan >= 21) or (mjesec == 4 and dan <= 19):
#     znak = "Ovan"
# elif (mjesec == 4 and dan >= 20) or (mjesec == 5 and dan <= 20):
#     znak = "Bik"
# elif (mjesec == 5 and dan >= 21) or (mjesec == 6 and dan <= 20):
#     znak = "Blizanci"
# elif (mjesec == 6 and dan >= 21) or (mjesec == 7 and dan <= 22):
#     znak = "Rak"
# elif (mjesec == 7 and dan >= 23) or (mjesec == 8 and dan <= 22):
#     znak = "Lav"
# elif (mjesec == 8 and dan >= 23) or (mjesec == 9 and dan <= 22):
#     znak = "Djevica"
# elif (mjesec == 9 and dan >= 23) or (mjesec == 10 and dan <= 22):
#     znak = "Vaga"
# elif (mjesec == 10 and dan >= 23) or (mjesec == 11 and dan <= 21):
#     znak = "Skorpija"
# elif (mjesec == 11 and dan >= 22) or (mjesec == 12 and dan <= 21):
#     znak = "Strijelac"
# elif (mjesec == 12 and dan >= 22) or (mjesec == 1 and dan <= 19):
#     znak = "Jarac"
# else:
#     znak = "Nepoznat datum, provjeri unos."

# print("Vas znak je: ", znak)