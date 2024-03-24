import time
import winsound


def mergeSort(arr):
	if len(arr) > 1:

        # Dividing the array elements
		left_arr = arr[:len(arr)//2]
		

		# Into 2 halves
		right_arr = arr[len(arr)//2:]

		# Sorting the first half
		mergeSort(left_arr)

		# Sorting the second half
		mergeSort(right_arr)
		
		

		i = 0
		j = 0
		k = 0 
		
	

		# Copy data to temp arrays left_arr[] and right_arr[]
		while i < len(left_arr) and j < len(right_arr):
			if left_arr[i] <= right_arr[j]:
				arr[k] = left_arr[i]
				i += 1
			else:
				arr[k] = right_arr[j]
				j += 1
				winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS) #plays window sound when swap occurs
				print(f'Current array is - {arr}')


			k += 1

		# Checking if any element was left
		while i < len(left_arr):
			arr[k] = left_arr[i]
			i += 1
			k += 1

		while j < len(right_arr):
			arr[k] = right_arr[j]
			j += 1
			k += 1

products = [11,1,30,2,51,6,29,7,67,15,118,4,89,23]

mergeSort(products)

print(f'Sorted Array is - {products}')




