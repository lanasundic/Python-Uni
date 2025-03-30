#4. -> prvi test - na papiru se radi

#Napisati program koji izbacuje svaku drugu cifru (znaci izbacuje parne cifre)
#5763 -> 56
#27458 -> 248

n = int(input())
n = str(n)  #pretvorimo n u string
print(n[::2])   #stampaj od pocetka do kraja, svaki drugi string

    