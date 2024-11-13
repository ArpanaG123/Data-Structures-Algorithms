# Subsets
# link - https://leetcode.com/problems/subsets/description/

# Given an integer array nums of unique elements, return all possible subsets(the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

nums = [0]
# Output: [[],[0]]

def subsets(arr):
    # Get the length of the input array.
    n = len(arr)
    
    # Initialize an empty list to store all subsets.
    ans = []
    
    # Define a helper function that will be used to generate subsets recursively.
    # It takes three parameters:
    # - idx: the current index in the array to explore
    # - arr: the input array
    # - temp: a list to store the current subset being formed
    def helper(idx, arr, temp):
        
        # Append a copy of the current subset (temp) to the answer list (ans).
        # This ensures that we save the current state of 'temp' as a valid subset.
        ans.append(temp[:])  # Use temp[:] to create a shallow copy
        
        # Iterate over the array starting from the current index (idx).
        for i in range(idx, n):
            
            # Include the current element (arr[i]) in the subset.
            temp.append(arr[i])
            
            # Recursively call the helper function with the next index (i+1).
            # This will explore all subsets that include arr[i].
            helper(i + 1, arr, temp)
            
            # Backtrack: remove the last added element to explore other possibilities.
            # This step ensures we can explore subsets without the current element.
            temp.pop()
    
    # Call the helper function starting with the first index (0) and an empty subset (temp).
    helper(0, arr, [])
    
    # Return the list of all generated subsets.
    return ans

# Example usage:
arr = [1, 2, 3]

# Get all subsets of the array and print them.
result = subsets(arr)
print(result)