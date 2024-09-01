# Write a program to cyclically rotate an array by one.
# Link - https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one/0

arr = [1,2,3,4,5]
def rotate(arr):
    n = len(arr)
    if n == 0:
        return
        
    last_element = arr[-1]
        
    # Shift all elements to the right by one position
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
        
    # Set the first element to be the last element
    arr[0] = last_element

    return arr

res = rotate(arr)
print(res)

# TC = 0(N)
# SC = 0(1)