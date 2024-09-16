n = int(input())
arr1 = [int(el1) for el1 in input().split()]
m = int(input())
arr2 = [int(el) for el in input().split()]
res = []

for el1 in arr1:
    if el1 not in arr2:
        res.append(el1)
print(len(res))
print(*res)

# https://www.eolymp.com/uk/submissions/15407089
