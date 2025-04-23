#Napisati programski kod koji provjerava da li je uneseni string s palindrom. Npr. ako je s = "ana", program treba da odstampa "da".
#Ako je s="anja", program treba da odstampa "ne".

s = input("Unesi string: ")

if s == s[::-1]:
    print("da")
else:
    print("ne")
