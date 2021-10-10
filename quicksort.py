import shutil
columns = shutil.get_terminal_size().columns

def Partitioning(A, start, end):
	#sort everything less than pivot to left, and everything more than the pivot to the right of the pivot
	pivot = A[end]
	pIndex = start

	for i in range(start, end):
		#all the values bigger than pivot get pushed to the right of the pivot
		if A[i] <= pivot:
			A[i], A[pIndex] = A[pIndex], A[i]
			pIndex += 1

	A[end], A[pIndex] = A[pIndex], A[end]

	return pIndex

def Quicksort(A, start, end):

	if start >= end:
		return

	pivot = Partitioning(A, start, end)

	#repeat partitioning on sublist containing elements less than the pivot 
	Quicksort(A, start, pivot-1)
	#repeat partitioning on sublist containing elements more than the pivot 
	Quicksort(A, pivot+1, end)



# Python implementation of the Quicksort algorithm
if __name__ == '__main__':
 
    print("QUICKSORT ALGORITHM! \n".center(columns))
    while True:
	    array = input("Please input the numbers separated by commas: ").split(",")
	    array = [int(x) for x in array]
	    n = len(array)

	    Quicksort(array, 0, n - 1)

	    # print the sorted list
	    print(array)

	    ask = input("\nWanna Continue? [y/n]").lower()
	    if ask == "y":
	    	continue
	    elif ask == "n":
	    	exit()
