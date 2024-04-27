v = int(input())
t = int(input())
if v > 0:
    print(v*t % 109)
if v == 0:
    print(0)
if v < 0:
    print((109 + v*t)%109)
    