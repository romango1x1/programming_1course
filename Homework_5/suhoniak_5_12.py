n = int(input())
lst1 = [int(el) for el in input().split()]
lst2 = []

for i in range(len(lst1)):
    el = lst1[i]
    if el not in lst2:
        lst2.append(el)

print(*lst2)

# https://www.eolymp.com/uk/submissions/14692027
