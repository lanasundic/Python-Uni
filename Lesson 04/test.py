
#da se dati imenik izmijeni tako da se na pocetku svakog broja telefona doda +382 a da se 0 izbrise

imenik = {"Marko": "069595131", "Marija": "098755765", "Ivan":"83738827383"}

'''for x in imenik.values():
    if x[0]== "0":
        x = x[1:]
        
    x = "+382" + x
    print(x)
'''

for key in imenik.keys():
    if imenik[key][0] == "0":           #ovim imenik[key] dobijamo value
        imenik[key] = imenik[key][1:]
    
    imenik[key] = "+382" + imenik[key]
    print(imenik[key])