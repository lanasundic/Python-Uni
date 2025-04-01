#torki - zagrada i elemente nabrojimo u toj zagradi, moze da sadrzi brojeve, stringove...
t1 = (2, 5, 3)
t2 = ("A", "B", "C", "D")
t3 = (5, "PMF", False)
#pristupa im se isto kao i listama, u uglastim zagradama

print(t1[0])
print(t2[1])
print(t3[-1])

print(t1.count(3))
#ako je private stavimo __ dvije donje crte
print(t1.index(3))

#mozemo da provjerimo da li je neki broj u torci
print("B" in t2)
print("G" in t2)

#"siromasnija verzija listi"

print(t3[1:4])  #indexiranje isto kao kod listi, unazad...s lijeva... svaki drugi/treci...

#glavna razlika je ta sto su torke immutable strukture, stringovi su isto bili immutable
t2[0] = "A" #nema funkcije za dodavanje, za brisanje el..., ovo kod torkija i stringova ne prolazi
#ako zelimo da dodamo neki el u torku to se radi na sljedeci nacin:
t2 = ("X",) + t2
print(t2)

t2 = ("X",)    #ovo je torka od jednog el, ne bez zareza!

#to sto su torki immutable ima svoje prednosti, zato cemo da ih koristimo bez obzira sto su jako slicni listama

#torke - tuple, rjecnik - dictionary

a = [1, 2, 3, 4]
b = tuple(a)
print(b)    #listu pretvaramo u torku- to moze isto

#u rjecnicima se cuvaju parovi, svaki dio rjecnika je par, jedan dio para se zove kljuc(key) a drugi vrijednost(value)
#vrijednost(value) je ono sto stvarno zelimo da cuvamo u tom rjecniku, a kljucem znamo gdje se to nesto nalazi
#primjer rjecnika - rjecnik rijeci, prevod, rijeci s eng na francuski, ako zelimo takve podatke da cuvamo,
#cuvamo ih u parovima, kljuc je rijec na eng a value na franc
#drugi primjer telefonski imenik kljucevi su imena ljudi a vrijednost je broj telefona
#zasto je ta struktura efikasna? Kljucevi moraju da budu jedinstveni

#Kako se taj rjecnik pravi u pajtonu - u viticastim zagradama,parovi kljuc i vrijednost odvojeni zarezon

imenik = {"Marko": "069595131", "Marija": "098755765", "Ivan":"83738827383"}

print(imenik["Ivan"])   #stampa ivanov broj telefona
imenik["Ivan"] = "06272662" #ako zelimo da mu promijenimo broj tel
print(imenik)

#mozemo i da dodamo novi element
imenik["Bojana"] = "028278173"
print(imenik)

#ako zelimo da obrisemo neki el
del imenik["Marija"]
print(imenik)

#ako bismo u nekom momentu promasili kljuc, ne stavimo Ivan nego Ivana npr. dobijamo gresku
#medjutim mozemo da stavimo provjeru da li se taj kljuc nalazi u rjecnik
print("Ivana" in imenik)       #ovo mozemo samo za kljuceve da radimo ne za vrijednosti
print("062727362" in imenik)     #dobijama false iako je tacna vrijednost, jer samo kljuceve provjerava

#Neke funkcije:
print(imenik.get("Ivan"))  #damo kljuc i on nam da vrijednost
print(imenik.get("Ivana"))  #ako pogrijesimo kljuc ne puca program nego stampa none

v = imenik.pop("Ivan")
imenik.pop("Ivan")      #pop vraca vrijednost Ivanovu
print(imenik)

imenik.pop("Ivana", -1) #"Ako ovoga kljuca nema vrati -1"

#🔹 Koristi get() kada samo želiš da dobiješ vrednost ključa bez rizika od greške.
#🔹 Koristi pop() kada želiš da dobiješ i istovremeno ukloniš ključ iz rečnika, BACA GRESKUUUUUU

#ako zelimo da prodjemo svim el kroz rjecnik
for xovno in imenik:
    print(xovno)
    
for x in imenik.keys():
    print(x)    #prolazi kroz keys
    
for x in imenik.values():
    print(x)    #kroz values
    
for x in imenik.items():
    print(x)    #dobijamo torke, kljuc zarez vrijednost
    
for k, v in imenik.items():
    print("k=",k,"v=",v)     # u k se upisuje kljuc a u v values
    
#sto se tice vrijednosti mozemo bilo sta da sacuvamo, moze da bude lista, string, broj, 
# nema ogranicenja sta moze da bude vrijednost koja se cuva u rjecniku
#a kljuc mogu da budu samo oni objekti nad kojima moze hash da se izracuna a to su immutable(strukture kojima se ne moze promijeniti vrijednost) strukture 
# koje ne mogu da se promijene, string i broj moze, lista ne moze, torka moze, mada najcesce su kljucevi stringovi

rjecnik = {
    4 : [0, 1, 2, 3],    #broj je kljuc, vrijednost je lista
    (5, 7, 8): {        #ovo je tuple
        "abc" : 5,
        "cdf" : 17
    }
}

#kako bismo pristupili 5 u gore primjeru
print(rjecnik[(5, 7, 8)]["abc"])    #od torke - od ljuc pa opet kljuc
#a 2?
print(rjecnik[4][2])   #kljuc nam je 4 pa index napisemo od dvojke

