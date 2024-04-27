n = int(input())
h = n //3600 % 24
m = n // 60 % 60
s = n % 60 
if m < 10 and s < 10:
    print(f'{h}:0{m}:0{s}')
elif m < 10 and s >= 10:
    print(f'{h}:0{m}:{s}')
elif m >= 10 and s < 10:
    print(f'{h}:{m}:0{s}')
else:
    print(f'{h}:{m}:{s}')
