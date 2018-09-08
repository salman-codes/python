
def fibonacci(first, second, count, counter):
	if count == 1:
		print(first)
	elif count == 2:
		print(second)
	elif counter==count-1:
		next_n = first+second
		print(next_n)
	else:
		if counter <= 2:
			print(first)
			print(second)
		next_n = first+second
		print(next_n) 
		counter+=1
		fibonacci(second, next_n, count, counter)


n= int(input("A number. that's all i need: "))

fibonacci(0, 1, n, 2)