d = "17-03-2023"
a = d.split("-")    #od stringa napravi listu
a[0] = str(int(a[0])-1) # 17 postaje 16
s = "/".join(a) #od liste napravi string joinovanjem pomocu /
print(s)    #stampa - 16/03/2023