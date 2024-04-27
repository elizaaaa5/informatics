i = int(input())
total = (45*i + 5*(i //2) + 15*((i - 1)//2))
d = total // 60
hours = 9 + d
minutes = total % 60
print (hours, minutes)