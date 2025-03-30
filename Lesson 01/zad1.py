'''
Neka korisnik unese temperaturu u celzijusima, a da program tu temperaturu pretvori
u Feranhajte.
formula ---> C = (f - 32) * 5/9
'''

c = input("Unesite temperaturu u Celzijusima:")
c = float(c)    #c moramo da pretvorimo u float ili int zato sto se inputom unosi samo tekst.
                #Ne postoji rjesenje za unos brojeva.

f = 9/5 * c + 32
print("Temperatura u Feranhajtima je", f)