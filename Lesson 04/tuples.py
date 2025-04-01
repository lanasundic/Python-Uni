rjecnik = {
    4 : [0, 1, 2, 3],    #broj je kljuc, vrijednost je lista
    (5, 7, 8): {         #tuple je kljuc, a vrijednost je novi mali dictionary
        "abc" : 5,       # sa svojim kljucem "abc" i vrij. 5
        "cdf" : 17       # sa svojim kljucem "cdf" i vroj. 17
    }                    # (znamo da je dictionary po viticastim zagradama)
}

print(rjecnik[(5, 7, 8)]["cdf"])

# ili na duzi nacin:
maliDictionary = rjecnik[(5, 7, 8)]
vrijDrugogElMalogDicta = maliDictionary["cdf"]
print(vrijDrugogElMalogDicta)
