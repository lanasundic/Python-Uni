'''
7. Napisati program koji omogućava korisniku da unese veličinu fajla u gigabajtima i koji 
izračunava koliko će sekundi biti potrebno za prenos tog fajla mrežom čija je brzina 
100Mbit/s. 
Napomena: 
1 bajt = 8 bita 
1 kilobajt = 1024 bajta 
1 megabajt = 1024 kilobajta 
1 gigabajt = 1024 megabajta 
1 kilobit = 1000 bita 
1 megabit = 1000 kilobita 
'''

giga = int(input("Unesite velicinu fajla u gigabajtima: "))

# giga_u_sec = 100 / 8 / 1024

# print(giga/giga_u_sec)


#pretvorimo prvo u megabite
mega = giga * 1024 * 8

vrijemePrenosa = mega / 100

print(vrijemePrenosa)
