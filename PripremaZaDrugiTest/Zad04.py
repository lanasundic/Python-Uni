#4. Napisati program koji računa starost psa. Prva navršena kalendarska godina života psa 
#je ekvivalent 15 ljudskih. Druga kalendarska godina donosi još 9 ljudskih. Svaka sljedeća 
#kalendarska godina je još pet ljudskih.

n = int(input("Unesite godine vaseg psa: "))
ljudskeGodine = 0

for i in range(1, n + 1):   #od 1. godine do n godina
    if i == 1:
        ljudskeGodine += 15
    elif i == 2:
        ljudskeGodine += 9
    else:   #sve ostalo
        ljudskeGodine += 5

print("Godine u ljudskim godinama su:", ljudskeGodine)