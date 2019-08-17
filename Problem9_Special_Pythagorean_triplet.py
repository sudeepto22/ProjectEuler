# a + b + c = 1000
# Find a * b * c

flag = False
for a in range(1, 998):
    for b in range(1, 998-a):
        if a**2 + b**2 == (1000 - a - b)**2:
            flag = True
            break
    if flag:
        break
print(a * b * (1000 - a - b))
