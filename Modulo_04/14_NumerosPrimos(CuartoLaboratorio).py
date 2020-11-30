def isPrime(num):
    div = 0
    for i in range(1, num+1):
        if num % i == 0:
            div += 1
            
    if div > 2:
        return False
    return True

for i in range(1, 100):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()