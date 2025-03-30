#Napravi program koji ce da sortira listu brojeva po cifri desetica - opadajuce
#[624, 358, 19, 92, 133]
#[92, 358, 133, 624, 19]    PO CIFRI DESETICA

lista = [624, 358, 19, 92, 133]

def pom(x):
    return (x%100)//10 

lista.sort(key = pom, reverse = True)
print(lista)

#jasno