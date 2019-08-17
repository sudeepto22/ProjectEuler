i = 3
a, b = 1, 2
sum1 = 0
while i < 4000000:
	a, b = b, a+b
	i = a
	if i < 4000000:
		if i % 2 == 0:
			sum1 += a
print(sum1)
