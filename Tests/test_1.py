# Знайти добуток всіх чисел від 1 до n(включно) які діляться на 8
n = int(input())
product = 1

for i in range(1, n + 1):
    if i % 8 == 0:
        product *= i
        
print(product)

