# Insertion sort

# Insertion Sort is a simple and intuitive sorting algorithm that builds the final sorted array (or list) one element at a time. It works similarly to how we sort playing cards in our hands. The array is conceptually split into two parts: the sorted and unsorted portions. Elements from the unsorted portion are picked and placed at the correct position in the sorted portion.

def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Element to be placed at its correct position
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key at the correct position
        arr[j + 1] = key

# Test the code with an example
arr = [5, 2, 9, 1, 5, 6]
print("Original array:", arr)

insertionSort(arr)
print("Sorted array:", arr)

# second way

def insert(alist, index, n):
    #code here
    key = alist[index]
    j = index-1
        
    while j >= 0 and alist[j] > key:
        alist[j+1] = alist[j]
        j -= 1
    alist[j+1] = key
        
#Function to sort the list using insertion sort algorithm.    
def insertionSort(alist, n):
    #code here
    n = len(alist)
    for i in range(1,n):
        insert(alist,i,n)
        
    return alist

alist = [2,1,5,4,3]
n = len(alist)
result = insertionSort(alist,n)
print(result)
