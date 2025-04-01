s = "Abc3DEf02ghl98"
t = ""
for c in s:
    t += c  #t = t + c     blank + karakter
    if c.isdigit():     #ako je karakter broj
        t += str((int(c) + 1) % 10)     #3 + 1 % 10...

print(t)    # A b c 4 D E f 0 3 g h l 0 9