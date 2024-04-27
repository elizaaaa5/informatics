a = int(input())
b = int(input())
print(int(a!=b)*int(a // b != 0)*a + int(a!=b)*int(b//a != 0)*b + int(a == b)*a)