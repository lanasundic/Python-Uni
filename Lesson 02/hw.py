'''
Napisati program u kojem se unosi n tako da odstampa ovakav oblik
npr. n = 3
        *
       ***
      *****
       ***
        *   

'''
n = 3#int(input("Unesite broj n:"))
b = '*'

g = "/"

i = 1
while i <= n:
    print(g * ((n - i) // 2))
    
    print((i*2 -1) * b)
    i += 1

i = n - 1
while i > 0:
    print(g * ((n - i) // 2))
    print((i*2 - 1) * b)
    i -= 1
