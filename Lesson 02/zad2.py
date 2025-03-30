'''
Napisi provjera_sifre() koja kao arg dobija jedan string i provjerava da li taj string predstavlja pravilnu sifru

Pravila za sifru:
> 6 karaktera
barem 1 veliko slovo
barem 1 malo slovo
barem 1 cifra
barem 1 spec karakter
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
    
a = "Sifra1!]"
print(provjera_sifre(a))
