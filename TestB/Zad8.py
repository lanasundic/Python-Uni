s = "Abc3DEf02ghiJ98"
t = ""
for c in s:
    t += c  #Abc32DEf.... sta sa -1?
    if c.isdigit():
        t += str((int(c) - 1) % 10)

print(t)