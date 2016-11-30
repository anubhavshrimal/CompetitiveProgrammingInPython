import math
n = int(input().strip())
arr = []

def sum_of_digits(i):
    digitSum = 0
    while i != 0:
        digitSum += i % 10
        i //= 10
    return digitSum

max = 1
num = 1

for i in range(2,int(math.sqrt(n)+1)):
    if n % i == 0:
        a = sum_of_digits(i)
        if max < a:
            max = a
            num = i
        elif max == a and num > i:
            num = i
        if i != n//i:
            b = sum_of_digits(n//i)
            if max < b:
                max = b
                num = n // i
            elif max == b and num > n // i:
                num = n // i

a = sum_of_digits(n)

if max < a:
    num = n

print(num)
