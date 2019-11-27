arr = [1, 2, 3, 4, 5, 6]
sum = 0

for num in arr:
	sum = sum + num

print (sum)

length = len(arr)

while length:
	sum = sum + arr[length - 1]
	length = length - 1

print (sum)
