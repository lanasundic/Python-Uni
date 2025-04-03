#2. Data je lista od n-1 jedinstvenih brojeva od 1 do n. Nadi broj koji nedostaje, bez sortiranja

#input: [4, 1, 3, 5, 6]
#output: 2

l1 = [4, 1, 3, 5, 6]
n = len(l1)

# l2 = []
# i = 1
# for c in l1:
#     l2.append(i)
#     i += 1
# l2.append(i)
l2 = list(range(1, len(l1) + 2))

print(sum(l2)-sum(l1))




# s1 = 0
# for i in l1:
#     s1 += i

# s2 = 0
# for j in l2:
#     s2 += j

# print(s2-s1)




# for j in l2:
#     postoji = False
#     for c in l1:
#         if j == c:
#             postoji = True
#     if postoji == False:
#         print(j)
#         break

    