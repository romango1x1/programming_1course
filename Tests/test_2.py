n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

symmetrical = True

for i in range(n):
    for j in range(n):
        if arr[i][j] != arr[j][i]:
            symmetrical = False
            break

if symmetrical:
    print("Symmetrical")
else:
    print("Not symmetrical")
