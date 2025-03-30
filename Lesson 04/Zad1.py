#da se dati imenik izmijeni tako da se na pocetku svakog broja telefona doda +382 a da se 0 izbrise

imenik = {"Marko": "069595131", "Marija": "098755765", "Ivan":"83738827383"}

#for v in imenik.values():   #ove vrijedosti su kopije vrijednosti iz rjecnika pa ne moze ovo
#moramo pom kljucu da idemo



#4. aprila prvi test na papiru, da kod i sta radi, testovi nose po 30, drugi ce da poveca na 40 bodova


for key in imenik.keys():
    if imenik[key][0] == "0":   #ako je prvi karakter 0
        imenik[key] = "+382" + imenik[key][1:]   

#ovo bi mogao da bude jedan zadatak na kolokvijumu

#najbitnija je stvar sto smo po kljucevim amoranmi da idemo, petlja po vrijednosti ne funkcionise jer to ne bi
#promijenilo imenik
