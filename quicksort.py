import shutil
columns = shutil.get_terminal_size().columns()

def Quicksort(A, start, end):
	




# Python implementation of the Quicksort algorithm
if __name__ == '__main__':
 
    print("QUICKSORT ALGORITHM! \n".center(columns))
    array = input("Please input the numbers separated by commas: ").split(",")
    array = [int(x) for x in array]
    n = len(array)

    Quicksort(array, 0, n - 1)

    # print the sorted list
    print(array)