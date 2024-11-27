# Container With Most Water
# Link - https://leetcode.com/problems/container-with-most-water/description/?envType=problem-list-v2&envId=array

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

height = [1,1]
# Output: 1

# Brute force

def maxArea(height):
    # Get the number of elements in the height list
    n = len(height)
    
    # Initialize the variable to store the maximum water area found so far
    max_water = 0
    
    # Outer loop as left boundary to go through each element in the list from the first to the second last
    for i in range(0, n):
        # Inner loop as for right boundary to go through the list starting from the element after 'i'
        for j in range(i+1, n):
            # Find the minimum height between the two selected heights at index i and j to avoid overflow we select miniumum of both boundaries
            h = min(height[i], height[j])
            
            # Calculate the width between the two positions i and j
            w = j - i
            
            # Calculate the area formed by the two lines (heights at i and j)
            area = h * w
        
            # Update the maximum area if the current area is larger than the previous max_water
            max_water = max(area, max_water)
    
    # Return the maximum area of water found
    return max_water
    
# Example input
height = [1, 1]
result = maxArea(height)
print(result)

# TC = 0(N^2)
# SC = 0(1)

# Optimal - using two pointer

def maxArea(height):
    # Get the number of elements in the height list
    n = len(height)
    
    # Initialize the variable to store the maximum water area found so far
    max_water = 0
    
    # Initialize two pointers, one at the beginning and one at the end of the list
    left_b = 0
    right_b = n - 1
    
    # Loop until the two pointers meet
    while left_b < right_b:
        # Calculate the width between the two pointers
        w = right_b - left_b
        
        # Find the minimum height between the two heights at the pointers
        h = min(height[left_b], height[right_b])
        
        # Calculate the area formed by the container
        area = h * w
        
        # Update the maximum area if the current area is larger
        max_water = max(max_water, area)
        
        # Move the pointer corresponding to the smaller height
        if height[left_b] < height[right_b]:
            left_b += 1
        else:
            right_b -= 1
    
    # Return the maximum area of water found
    return max_water

# Example input
height = [8, 7, 2, 1]
# Call the function and store the result
result = maxArea(height)
# Print the result
print(result)


