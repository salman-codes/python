def bubble_sort(arr):
	
	for i in range(len(arr)):
		for j in range(0, len(arr)-i-1):
			if arr[j]>arr[j+1]:
				temp = arr[j]
				arr[j]=arr[j+1]
				arr[j+1]=temp

	print(arr)


arr =[8, 9, 8, 1, 5, 3, 98, 24, 654, 5, 4, 5, 0]

bubble_sort(arr)