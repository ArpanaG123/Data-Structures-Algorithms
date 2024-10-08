# Sort an array using recursion
arr = [2,5,4,6,7,9,3]
# output = [2,3,4,5,6,7,9]

def sort_array(arr):
    n = len(arr)
    
    # Helper function that sorts the array and handles insertion
    def helper(arr):
        # Base case: an array with one or zero elements is already sorted
        if n == 1:
            return
        
        if arr:
            #Remove the last element and recursively sort the remaining arr
            last_element = arr.pop()
            helper(arr)
        
            # Insert the last element into the sorted portion of the array
            insert(arr, last_element)
    
    # Helper function to insert an element in its correct position in a sorted array
    def insert(arr, value):
        # If the array is empty or value is greater than the last element, append it
        if not arr or value >= arr[-1]:
            arr.append(value)
        else:
            # Recursively remove the last element, insert value, then put the last element back
            last = arr.pop()
            insert(arr, value)
            arr.append(last)
    
    # Start the recursive sorting process
    helper(arr)
    return arr

# Example usage:
arr = [3, 1, 4, 1, 5]
sorted_arr = sort_array(arr)
print(sorted_arr)