a, b, c, d = map(int, input().split())
prods = []

for i in range(min(a, b), (max(a, b) + 1)):
    for j in range(min(c, d), (max(c, d)) + 1):
        res = i * j
        if res not in prods:
            prods.append(res)

variants = len(prods)

print(variants)

# https://www.eolymp.com/uk/submissions/15419255
