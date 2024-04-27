a = int(input())
b = int(input())
n = int(input())
rub = a*n + (b*n // 100)
cop = b*n % 100
print(rub, cop)