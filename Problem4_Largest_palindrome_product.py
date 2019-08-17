def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False


final_ans = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        prod = i * j
        if is_palindrome(prod):
            if prod > final_ans:
                final_ans = prod
print(final_ans)

