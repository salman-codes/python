
def generate_fibonacci_numbers(count):
	first =0
	second=1
	counter = 2;
	print(first)
	print(second)
	while counter != count:
		next_n = first+second
		print(next_n)
		first=second
		second=next_n
		counter += 1


def find_fibonacci_at_pos(position):
	first  = 0
	second = 1
	counter = 2
	if position==1:
		print(first)
	elif position==2:
		print(second)
	else:
		while counter != position:
			next_n = first+second
			first=second
			second=next_n
			counter += 1

		print(next_n)

n = int(input("How many fibonacci numbers you want? "))

# generate_fibonacci_numbers(n)
find_fibonacci_at_pos(n)