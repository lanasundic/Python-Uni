n = 375
s = str(n)  #broj pretvaramo u string
m = int(s[::-1])    #stampaj unazad elemente iz stringa pa ih opet pretvori u broj - zato sto samo string mozemo da sjeckamo - npr. uzmemo 5. cifru, stampamo ih unazad...

print(m)    #stampa - 573