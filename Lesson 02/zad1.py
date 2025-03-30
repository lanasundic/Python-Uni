'''
Napisati program u kojem se unosi prirodan broj n i na osnovu tog broja n treba da se odstampa
odredjen oblik sa zvjezdicama
npr. n = 4          n = 3
*                   *
**                  **
***                 ***
****                **
***                 *
**
*
'''

n = int(input("Unesite n:"))

b = "*"

i = 1
while i <= n:
    print(i * b)        #U Pythonu, množenje stringa sa brojem (kao što je i * b) znači ponavljanje tog stringa onoliko puta koliko iznosi broj i.
    i += 1
    
i = n - 1
while i > 0:
    print(i * b)
    i -= 1
    
    
'''
1. Unosimo koliko ce da bude redova sa zvjezdicama, to je ovo n
2.rastuci dio - treba prvo da ispisemo zvjezdice pocevsi od 1. zvjezdice, pa do n zvjezdica, pri cemu broj zvjezdica
  raste sa svakim sljedecim redom
3.opadajuci dio - onda nakon sto ispisemo n zvjezdica ispisujemo redove sa manjim brojem zvjezdica, sve dok ne stignemo
  do 1 zvjezdice
  
Dakle, prvo ispisujemo rastuće redove sa zvjezdicama (od 1 do n).
Zatim, ispisujemo opadajuće redove sa zvjezdicama (od n-1 do 1).
'''