#dat je dictionary u kom su imena ljudi sa rodjendanima - za vjezbu
'''
Rodjendani = {
    "Marko": "5.8.2005"
    i tako sve
    
}
treba da se istampa mjesec u kom ima najvise rodjendana- slovima da napisemo, npr. April
'''

#Izracunati koliko bi sve ovo trebalo da se plati - cijenu porudzbina
katalog = {
    "laptop": 1299.99,
    "slusalice": 49.99,
    "tastatura": 75.00,
    "desktop racunar": 2100.00
}
porudzbina = {
    "laptop": 3,
    "slusalice": 10,  #komada
    "tastatura": 5,
}

cijena = 0
for artikal in porudzbina.keys():       #opet idemo preko keysa a ne preko valuesa to je isto bitno
    cijena += (porudzbina[artikal]*katalog[artikal])
    
print(cijena)