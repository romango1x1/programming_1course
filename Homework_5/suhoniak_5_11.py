n = int(input())
arr = [int(el1) for el1 in input().split()]

arr = [arr[-1]] + arr[:-1]

print(*arr)

# https://www.eolymp.com/uk/submissions/15407323
