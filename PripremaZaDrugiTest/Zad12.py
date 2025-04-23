'''
12. Napisati program koji provjerava validnost unijete šifre. Šifra se smatra validnom ukoliko 
ispunjava sljedeće kriterijume 
 Sadrži barem jedno veliko i barem jedno malo slovo abecede. 
 Sadrži barem jednu cifru 
 Sadrži barem jedan od specijalnih karaktera iz skupa {$,#,@}. 
 Ima više od 6 karaktera.  
'''

def provjera_sifre(tekst):  #ova f predstavlja da li dati tekst predstavlja validnu sifru
    tekst = str(tekst)
    if len(tekst) < 6:
        return False
    
    velikoSlovo, maloSlovo, cifra, specKarakter = False, False, False, False    #pretpostavimo da je sve false
    
    i = 0
    while i < len(tekst):
        if(tekst[i].isupper()):    
            velikoSlovo = True
            
        elif(tekst[i].islower()):
            maloSlovo = True
            
        elif(tekst[i].isnumeric()):
            cifra = True
            
        elif(not tekst[i].isalnum()):
            specKarakter = True
            
        i += 1
        
    return velikoSlovo and maloSlovo and cifra and specKarakter
    
print(provjera_sifre)
