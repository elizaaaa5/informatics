n = int(input())
m = int(input())
print((int(n % m ==0) + int(m % n ==0) + int(n % m !=0)*2 + int(m % n !=0)*2)//2)

