#Stringove u Pythonu možemo kreirati koristeći jednostruke (') ili duple navodnike (").
#a = "Hello.", a = 'Hello.'  ---> ovo dvoje je isto

a = "\"Python\""    #unutar navodnika dodajemo \" da bi dobili rijec sa navodnicima
b = '"Python"'
print(a, b)

#Na kolokvijumu: da nam neki string ---> nagadjaj sta ce da bude odstampano, nesto ovakvog tipa (indexiranje stringova)
print(a[0])     #odstampace se prvo slovo
print(type(a[0]))   #type(a[0]) - odredjuje koji je tip prvi karakter (int/string...)
print(a[1])     #stampa drugo slovo (y)

print(a[-1])    #stampa poslednji karakter stringa
print(a[-2])    #stampa drugi karakter stringa od pozadi

print(a[1:5:2])     #stampa svaki drugi karakter od 1. do 5.
print(a[:6:3])      #stampa svaki treci karakter od karaktera sa indexom 0 do 6
print(a[5::-1])     #stampa svaki kar krecuci se unazad, od 5. kar do pocetka stringa(jer nije navedeno)
print(a[5::-2])     #stampa svaki drugi kar unazad, od 5. kar do pocetka stringa
print(a[:2:-1])     #stampa svaki kar unazad, ide do 2. kar
print(a[::-1])      #stampa unazad samo
print(a[2::])       #stampa od drugog karaktera i ide do kraja
print(a[:5:])       #stampa prvih 5 kar stringa
print(a[:5])        #stampa prvih 5 kar stringa

a[0] = 'c' #Ovo ne moze, ali kod lista moze. ALI STA MOZE - mozemo da odstampamo od prvog kar do kraja
           #i nadovezemo slovo koje zelimo.

#Stringove mozemo i da nadovezujemo
c = a + b
print(c)    #konkatenacija stringova

a = 'c' + a[1:]
print(a)
d = a*3     #3 puta se stampa cython

print(len(a))   #length = len, stampa koliko string a ima karaktera

broj = 3.14
e = str(broj)
print(e*2)      #"3.143.14"

#str() pretvara vrijednost promjenljive broj u string.
#Dakle, 3.14 (koji je tipa float) se pretvara u string i dodjeljuje se promjenljivoj e.
#Nakon izvršenja ovog dijela, e postaje string "3.14".

f = "15"
broj = int(f)
print(broj*4)   #60

#Ovdje je f promenljiva koja sadrži string "15".
#Iako je u pitanju broj, on je trenutno zapisan kao string, jer je okružen sa navodnicima.

#onda koristi funkciju int() da bi pretvorio vrijednost promjenljive f iz stringa u cjelobrojnu vrednost.

a = "programiranje u pythony"
print(a.capitalize())      #tackom pozivamo string. Pretvaranje prvog slova stringa u veliko slovo

print(a)    #ako bismo sada ponovo pokusali da odstampamo a bilo bi malim slovom, jer tackom samo pozivamo
            #i privremeno mijenjamo string, a ne za ubuduce
            
print(a.count("ra"))    #izbrojace koliko puta se ra pojavilo u stringu a
print(a.count("ra", 5, 10))     #--||--  poceci od 5. kar do 10.

#na testu ne dobijamo opcije da nam samo pokaze ovo capitalize ili count npr.

print(a.find("ra"))     #na kojoj poz se javlja ra - pronadje samo prvo pojavljivanje
print(a.find("ra", 5, 8))

print(a.rfind("ra"))    #index poslednjeg pojavljivanja
print(a.index("ra"))
print(a.upper())        #sva slova velika
print(a.lower())        #sva slova mala
print(a.replace("ra", "x"))     #zamijeni ra sa x
print(a.replace("ra", "abcd", 1))      #samo prvo pojavljivanje zamijeni

b = "   pmf"
print(b.strip)      #mice blank ali samo s pocetka i kraja stringa, ne izmedju rijeci

c = "program"
print(c.isalpha())  #da li je string sav u slova(true/false)
print(c.isnumeric())    #da li je string sav u brojeve
print(c.islower())
print(c.isupper())
print(c.isalnum())      #da li je string i u brojeve i u slova (ne uklj spec karaktere)
