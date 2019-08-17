def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True


j = 2
sum1 = 0
while j < 2000000:
    if is_prime(j):
        print(j)
        sum1 += j
    j += 1

print(sum1)
