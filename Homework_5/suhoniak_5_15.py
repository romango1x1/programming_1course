n = int(input())
a = list(map(int, input().split()))
min, max = min(a), max(a)

for i in range(n):
    if a[i] == min:
        a[i] = max
    if a[i] == max:
        a[i] = min

print(*a)
