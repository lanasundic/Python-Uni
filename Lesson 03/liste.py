lista1 = [1, 2, 3, 4, 5]  #lista brojeva od 1 do 5
lista2 = ["Marko", "Kosta", "Milica", "Ana"]

		#lista je homogena struktura podataka
lista3 = [2, 3.5, ]

print(lista1[0])
print(lista2[2])
print(lista2[-1])   #printuje samo posljednji karakter(Ana)

print(lista1[1:4])  #ukljucuje od a ne do - stampa 2 3 4
print(lista1[1:4:2])    #od pocetka se gleda ovo svaki drugi
print(lista1[-1:-2:-1]) #opet ukljucuje od a ne do - stampa 5

lista1[0] = 10
print(lista1)

lista1[1:3] = [15, 10]
print(lista1)

#lista1[1:3] = []
#print(lista1)

lista1[1:3] = [2, 5, 8, 9, 7]   #15 i 10 ce da budu zamijenjeni vljd, elemente koje nismo obuhvatili indeksiranjem nece da dira
print(lista1)

#FUNKCIJE
print(len(lista1))   #govori koliko ima lista elemenata

lista1.append(12)  #dodaje jedan element na kraju liste
print(lista1)

lista1.insert(3, 20)  #na indeksu 3 ce da bude 20
print(lista1)

lista1.extend([2, 4, 6, 8])  #nadovezuje citavu listu jednu na drugu, odnosno dodaje ove elemente na kraju liste
print(lista1)

lista1.append([2, 4, 6 ,8]) #stampa - [2, 4, 6, 8] sa sve zagradama, jer append prima samo 1 element
print(lista1)

lista1 = lista1 + [10, 12, 14]  # + je isto sto i ekstend samo sto ce se napravit nova lista
print(lista1)

#TO BI BILE FUNKCIJA ZA DODAVANJE

#FUNKCIJE ZA BRISANJE
lista1.clear()  #sve obrise - dobijamo praznu listu
print(lista1)

lista1.pop()  #moze da se pozove sa jednim arg ili bez argumenata, kada je bez obrisace poslednji el u nizu
print(lista1)

a = lista1.pop() # sa a je ako hocemo da vidimo sta smo obrisali
print(a)
print(lista1)

lista1.pop(4)  #cetvrti element ce da bude obrisan

b = lista1.pop(4)   #u b cuvamo samo obrisani element i on ce da se stampa
print(b)
print(lista1)

lista1.remove(12)  #predajemo vrijednost koju zelimo da se obrise, brise prvo pojavljivanje 12
print(lista1)

c = lista1.count(10)   #broji koliko se neki element javlja 
print(c)

d = lista1.index(4, 7, 9)  #.index(x, start, end) pronalazi prvi indeks na kojem se nalazi vrijednost x u listi između indeksa start i end-1.
print(d)

print(14 in lista1)
print(10 in lista1)  #sa in provjeravamo da li se to nesto nalazi u strukturi ili ne nalazi

print("r" in "programiranje")  #recice true
print("rar" in "programiranje")  #recice false

del lista1[3:5]  #del = delete, 3 do 5
print(lista1)

del lista1[2]   #brise samo sl na index-u 2
print(lista1)

s1 = "danas ucimo o listama i drugim strukturama podataka"
l1 = s1.split()  #string "danas ucimo o listama i drugim strukturama podataka" je podijeljen na listu riječi, gdje je svaki element lista pojedinačna riječ. - Svaka reč iz stringa postaje zaseban element liste.
print(l1)

s2 = "7/3/2015"
l2 = s2.split("/")
print(l2)

s3 = "7.3.2015"
l3 = s3.split(".")
print(l2)

#kad imamo listu ali zelimo da je spojimo u string = suprotno od split
l4 = ["pmf", "d", "smjer", "python"]
s4 = " ".join(l4)  #" " i "" nije isto - bez blanka dobijamo pmfdsmjerpython ---> "elemente liste spoji razmakom"
print(s4)

listaBrojeva = ["1", "2", "3", "4"]
rezultat = "-".join(listaBrojeva)   # "elemente listespoji crticom -"
print(rezultat)     #stampa 1-2-3-4

l5 = ["7", "3", "2025"]
s5 = "/".join(l5)
print(s5)

#join() može da radi samo sa stringovima! Ako lista sadrži brojeve (int), prvo ih treba pretvoriti u stringove:
brojevi = [1, 2, 3, 4]
rezultat = "-".join

#DOMACI(bio na proslom kolokvijumu dje smo mi kucali kodove): Da korisnik unese datum i mi uzmemo taj datum i 
# odstampamo koji ce datum da bude nakon nekih k dana koje korisnik unese

print(lista1)
lista1.reverse()  #okrenuce listu
print(lista1)

lista1.sort()  #sortira listu po defaulty u rastuci poredak
print(lista1)

print(lista2)
lista2.sort()
print(lista2)  #dobicemo stringove sortirane po abecednom redosljedu, prvo Ana pa KOsta pa ....

lista1.sort(reverse = True)  #sortiranje u opadajucem poretku, okrene redosljed sortiranja
print(lista1)

lista2.sort(reverse = True)
print(lista2)

#sa key mozemo da zadamo nas nacin kako zelimo da sortiramo
def fun1(x):
    return len(x)  #preslikali smo string u broj a taj broj je duzina od stringa
                    #po duzini ce da sortira
lista2.extend(["Aleksandar", "Masa"])
lista2.sort(key = fun1)
print(lista2)
#key = fun1 znači da se sortiranje vrši prema dužini stringova (pošto fun1 vraća len(x)).

def fun2(x):
    return x%5  #sortira brojeve koji imaju ostatak 5 od najmanjeg do najveceg

lista1.sort(key = fun2) #zasto ovo nece?
print(lista1)

def fun3(x):
    return x%5, x%3

lista1.sort(key = fun3)
print(lista1)

#4. aprila 1. test - dobijemo kod i napisemo sta se radi, sta kod stampa, 25. gdje mi pisemo kodove

#TO JE TO O LISTAMA

#FOR PETLJA:
for x in lista1:
    print(x)  #petlja koja prodje listom1 i odstampa sve elemente
    
#for + promjenljiva + in + kolekcija koja nas zanima

print("Imitacija petlje iz C-a")
for i in range(10):  #od 0 do 9 (10 nije ukljuceno)
    print(i)
    
for i in range (5, 10):  #5, 6, 7, 8, 9
    print(i)
    
for i in range(5, 10, 2):  #od 5 do 10 ali svaki drugi broj
    print(i)
    
for c in "programiranje":
    print(c)  #dobijamo 1 po 1 karakter
    
for ind, val in enumerate(lista1):  # enumerate - vraca index elementa i njegovu vrijednost
    print(ind, val)  #ne moramo mi da dodajemo i++, nego sa enumerate dobijamo i index i val odjednom
    
for ind, val in enumerate(lista1):
    lista1[ind] = val + 1  
    #v = v+1
    
