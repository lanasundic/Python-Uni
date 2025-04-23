'''
13. Napisati funkciju umetni_string(string1, string2) koji u sredinu stringa1 umeće string2. 
Na primjer, ako je string1=”Python” a string2=”Programiranje”, rezultat je: 
“PytProgramiranjehon”. 
'''

def umetni_string(string1, string2):
    sredina = len(string1) // 2     #sredina stringa1

    novi_string = string1[:sredina] + string2 + string1[sredina:]   #novistr = str1 ali prva polovina + str2 + str1 ali druga polovina

    return novi_string

string1 = input("Unesite prvi string: ")
string2 = input("Unesite drugi string: ")

print(umetni_string(string1, string2))