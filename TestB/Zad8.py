s = "Abc3DEf02ghiJ98"
t = ""
for c in s:
    t += c  #AbC32DEf0921ghiJ9887
    if c.isdigit():
        t += str((int(c) - 1) % 10)

print(t) # stampa - Abc32DEf0921ghiJ9887 ->  -1 % 10 = 9
