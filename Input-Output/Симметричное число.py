a = int(input())
first = a // 1000
second = a // 100 % 10
third = a // 10 % 10
fourth = a % 10
print(int(first == fourth)* int(second == third) + int(first != fourth)*(second != third)*37 + int(first == fourth)*(second != third)*37 + int(first != fourth)*(second == third)*37)

