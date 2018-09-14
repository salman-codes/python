''' Read input from STDIN. Print your output to STDOUT '''
	#Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
	n = int(input("Tuple length: "))
	tup=()

	num = input("Enter Elements: ")
	num = num.split(' ')
	if n < len(num):
		n = len(num)

	for i in range(n):
		tup = tup+(int(num[i]), )

	num = int(input("Number to Check: "))
	counter=0
	for i in range(len(tup)):
		if num==tup[i]:
			counter += 1

	print("%s is %s times in the tuple." % (num, counter))

main()