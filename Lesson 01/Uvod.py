a = 5                   #ovako definisemo int
b, c, d = 7, 3, 3.14

print(a + b)
print(a - b)
print(a * b)
print(a / b)    #klasicno matematicko dijeljenje
print(a // c)   #div-cjelobrojno dijeljenje
print(a % b)    #mod
print(a ** b)   #"a na b"-stepenovanje

print(a < b)
print(a > b)
print(a == b)
print(a != b)

#Logicki operatori
a = True
b = False

print(a or b)
print(a and b)
print(not b)
print(a or b and True)

#Komentar u jednoj liniji
'''
Komentar u 
vise linija 
'''

#IF:
a = 10

if a > 7:
    print("Broj je veci od 7.")
else:
    print("Broj je manji od 7.")
    

i = 0
while i < 10:
    print("i=", i, "PMF")
    i = i + 1
    i += i          #ne postoji i++
    