# Trapping Rain Water
# Link - https://leetcode.com/problems/trapping-rain-water/description/

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

def trap(height):
    n = len(height)
    
    left = height[0]
    left_mx = [0]*n
    
    for i in range(n):
        left = max(left,height[i])
        left_mx[i] = left
    
    right = height[n-1]
    right_mx = [0]*n
    
    for i in range(n-1,-1,-1):
        right = max(right,height[i])
        right_mx[i] = right
    
    trapping_water = 0
    for i in range(n):
        trapped_water = min(right_mx[i],left_mx[i])-height[i]
        if trapped_water > 0:
            trapping_water += trapped_water
    
    return trapping_water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
result = trap(height)
print(result)