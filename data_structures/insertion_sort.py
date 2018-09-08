def insertion_sort(arr):
	for i in range(len(arr)):
		
		key = arr[i]
		j =i-1
		while j>=0 and key < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1]=key

	print(arr)


arr = [5, 98, 6, 1, 5, 552, 40, 44, 7, 8]

insertion_sort(arr)