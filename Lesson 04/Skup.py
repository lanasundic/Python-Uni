#posljednje gradivo koje ce da bude na testu je skup/set na eng
#kolekcija el gdje jedan el moze da se pojavi jednom

s1 = set([2, 3, 4, 5, 2, 3, 4, 6])  #mozemo listu da ubacimo i sad ce nam on napraviti set
#bice samo 2 3 4 5 6, brojevi nece da se ponavljaju

s2 = set("programiranje")   #svako pokretanje dobije razlicit redosljed
print(s2)   #dobicemo skup svih slova u tom stringu

s3 = set([])    #ako hocemo prazan skup
print(s3)

#ako zelimo da provjerimo da li se nalazi neki el u skupu koristimo in
if 4 in s1:
    print("El je u skupu")
else:
    print("El nije u skupu")
    
    
s4 = set([2, 4, 6, 8 ,10])

#operacije sa skupovima:
print(s1 & s4)  #presjek 2 skupa (zajednicki elementi)
print(s1 | s4)  #unija (svi elementi) - od najmanjeg ka najveceg
print(s1 ^ s4)  #simetricna razlika, kao unija pa minus presjek {3, 5, 8, 10} - se dobije
                #svi koji nisu zajednicki

#neke funkcije:
s1.add(7)   #dodaje el u skup, ako vec postoji nece se nista promijenit
print(s1)

s1.remove(5)    #el koji zelimo da obrisemo
print(s1)

v = s1.pop()    #pop brise i vrati prvi el koji smo dodali u skup
print(v, s1)
v = s1.pop()
print(v, s1)

print(s1.intersection(s4))  #presjek (zajednicki elementi)
print(s1.union(s4))     #unija (svi elementi)
print(s1.symmetric_difference(s4))  #sim razlika (svi el koji nisu zajednicku)
print(s1.difference(s4))    #razlika (elementi koji su SAMO u s1, ZNACI NE U S4)

print(s1.isdisjoint(s4))   #nemaju zajednickih elemenata - disjunktni skupovi - presjek im je prazan
print(s1.isdisjoint(s2))    #ako nemaju zaj el onda jesu disjunktni

print(s1.issubset(s4))  #podskup (svi iz s1 su u s4)
print(s1.issuperset(s4))    #nadskup (ukoliko s1 sadrzi sve iz s4)
