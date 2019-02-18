def search(arr,n,x):
	for i in range(0,n):
		if (arr[i] == x):
			return i
	return -1	
				
arr = [58,96,35,47,23,12,4,74]
x = 35
n = len(arr)
result = search(arr,n,x)
if (result == -1):
	print("Element x is not present in array")
else:
	print("Element x is present at index", result)	
