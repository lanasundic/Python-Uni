d = "17.03.2023"
a = d.split(".")    #pretvori u listu tako sto ces da el razdvojis po tacki - ["17", "03", "2023"]    
a[0] = str(int(a[0]) + 1)   #prvi element - 17:  saberi sa 1 - to je 18 i pretvori ga u string - a[0] = 18
s = "-".join(a) #pretvara nazad u string, spaja ih crticom -.

print(s)    #stampa - 18-03-2023