n = int(input())
if n < 1440:
    print(n // 60, n % 60)
if n >= 1440:
    print(n // 60 % 24, n % 60)
    