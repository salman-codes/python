def selection_sort(arr):

	for i in range(len(arr)):
		
		min_ind = i
		for j in range(i+1,len(arr)):
			if arr[min_ind] > arr[j]:
				min_ind = j

		arr[i], arr[min_ind] = arr[min_ind], arr[i]
	
	print(arr)

# n = int(input("Input Array size: "))
arr = [78, 6, 65, 52, 4, 21, 4, 6, 1]
# for x in range(n):
# 	arr[x] = int(input("Input number %s: " % x))

selection_sort(arr)