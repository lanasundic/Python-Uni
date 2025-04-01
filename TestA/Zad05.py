n, i = 5, 1
while i <= n:   # 5 puta ide kroz petlju
    j = 1   
    s = ""
    while j <= i:   #1 <= 1 - ide samo jedan put kroz ovu petlju
        s += "*"    # s = s + * ----> to je samo *
        j += 1  #j = 2

#ali ponovo se j resetuje na 1...

    print(s)    # stampa - *****
    i += 1