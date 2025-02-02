# Largest Rectangle in Histogram
# Link - https://leetcode.com/problems/largest-rectangle-in-histogram/description/

# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

# Approcah1
def previousSmallerElement(arr):
    n = len(arr)
    prev_smaller = [-1] * n
    st = []
    
    for i in range(n):
        while len(st) != 0 and arr[st[-1]] >= arr[i]:
            st.pop()
        if len(st) == 0:
            prev_smaller[i] = -1
        else:
            prev_smaller[i] = st[-1]
        st.append(i)
     
    return prev_smaller
    
def nextSmallerElement(arr):
    n = len(arr)
    next_smaller = [n] * n
    
    st = []
    for i in range(n):
        while len(st) != 0 and arr[st[-1]] > arr[i]:
            next_smaller[st.pop()] = i
        st.append(i)
    return next_smaller

def largestRectangleArea(arr):
    n = len(arr)
    
    nse = nextSmallerElement(arr)
    pse = previousSmallerElement(arr)
    
    maxi = 0
    
    for i in range(n):
        # Calculate width and area for the current element
        width = nse[i] - pse[i] - 1
        area = arr[i] * width
        maxi = max(area, maxi)
    
    return maxi
            
arr = [2, 1, 5, 6, 2, 3] 
result = largestRectangleArea(arr)
print(result)

# TC = 0(5N)
# SC = 0(2N) + 0(2N)

# Approach2

def largestRectangleArea(heights):
    # Initialize an empty stack to store indices of heights
    stack = []
    max_area = 0
    n = len(heights)
    
    # Traverse through all bars of the histogram
    for i in range(n):
        # If this bar is smaller than the bar on the top of the stack, pop the stack
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]  # Height of the bar at the popped index
            # If the stack is empty after popping, width is i (since we can extend to the leftmost bar)
            width = i if not stack else i - stack[-1] - 1
            # Update the maximum area
            max_area = max(max_area, h * width)
        
        # Push the current bar's index onto the stack
        stack.append(i)
    
    # Now, pop the remaining bars from the stack and calculate area
    while stack:
        h = heights[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, h * width)
    
    return max_area
# Test case
heights = [2, 0, 2]
result = largestRectangleArea(heights)
print(result)  # Expected output: 2

