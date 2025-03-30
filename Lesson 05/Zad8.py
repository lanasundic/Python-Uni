#Najveca drzava: za svaku listu data nam je drzava i broj stanovnika

drzave = [("Crna Gora", 645258), ("Malta", 12574), ("Vatikan", 1000)]

def pom(x):
    return x[1]

najvecaDrzava = max(drzave, key = pom)
print(najvecaDrzava)    #ako cemo samo ime drzave samo stavimo najvecaDrzava[0]

###     sum(somelist)/len(somelist)

'''
najvecaDrzava = max(drzave, key=lambda x: x[1]) #on je ovako bio napisao kao kako jos mozemo

'''

#da se iz liste izbace svi brojevi koje su manji od prosjecne vrijednosti - ovo da vjezbamo