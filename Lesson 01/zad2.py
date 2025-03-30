'''
Dat nam je broj riba u jezeru s i receno nam je da svake godine broj riba u jezeru raste za 5%.
Napisi program koji ce da nam kaze koliko ce riba da bude za nekoliko godina.
'''

s = int(input("Pocetni broj riba:"))
g = int(input("Broj goina:"))

i = 0
while i < g:
    s += s * 5  #ribe povecavaj za 5%
    i += 1
    
print("Broj riba nakon", g, "godina je", round(s), ".")

#round() koristimo kada zelimo da zaokruzimo na onaj dio kojem je broj blizi. Mogli smo da stavimo i int(s) ali
#round je preciznije