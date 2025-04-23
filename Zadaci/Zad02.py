#Napisati programski kod koji izbacuje parne cifre unesenog prirodnog broja n. Npr. ako je n = 24523, program treba da odstampa 53.

n = int(input("Unesite pr broj: "))

for cifra in n:
    if int(cifra) % 2 == 0:
        print()