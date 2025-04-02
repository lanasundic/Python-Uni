n, i = 3, 1
while i <= 2*n-1:   #1 <= 5  2 <= 5  3 <= 5   4 <= 5
    j = 1
    s = ""
    while j <= min(i, 2*n-i):   #ovaj dio odredjuje koliko zvjezdica * treba da bude u svakoj liniji
        s += "*"
        j += 1

    print(s)
    i += 1

#unutrasnja petlja dodaje zvjezdice * u s

#1	5	min(1,5) = 1	*
#2	4	min(2,4) = 2	**
#3	3	min(3,3) = 3	***
#4	2	min(4,2) = 2	**
#5	1	min(5,1) = 1	*