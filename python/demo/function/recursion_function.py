def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)

# print(fact(20))

def fact_iter(num, product = 1):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)

print(fact_iter(999))
