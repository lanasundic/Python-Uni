

l1 = [15, 10, 7, 3, 8]
def fun3(x):
    return x%5, x%3

l1.sort(key = fun3)
print(l1)