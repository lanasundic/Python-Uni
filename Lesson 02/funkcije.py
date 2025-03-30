#def + ime funkcije + obicne zagrade u kojima stavimo parametar

def zbir(a, b=2, c=4):      #ako ne predamo b bice 2
    s = a + b + c
    
    return s

print(zbir(10,6))