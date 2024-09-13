# sort 0's,1's and 2's - sort colors
# Link - https://leetcode.com/problems/sort-colors/description/

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

 

nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Brute force - using sorting algorithm

nums.sort()

# TC = 0(nlogn)
# SC = 0(N)

# Better approach using count

arr = [0,1,2,0,1,2,1,2,0,0,0,1]
n = len(arr)

cnt0 = 0
cnt1 = 0
cnt2 = 0

for i in range(0,n):
    if arr[i] == 0:
        cnt0 += 1
    elif arr[i] == 1:
        cnt1 += 1
    else:
        cnt2 += 1

for i in range(0,cnt0):
    arr[i] = 0
for i in range(cnt0,cnt0+cnt1):
    arr[i] = 1
for i in range(cnt1+cnt0,n):
    arr[i] = 2
print(arr)

# TC = 0(2N)
# SC = 0(1)

# Optimal approach - DNF(Dutch national flag)

arr = [0,1,2,0,1,2,1,2,0,0,0,1]
n = len(arr)

low = 0
mid = 0
high = n-1

while mid <= high:
    if arr[mid] == 0:
        arr[mid],arr[low] = arr[low],arr[mid]
        low += 1
        mid += 1
    elif arr[mid] == 1:
        mid += 1
    else:
        arr[mid],arr[high] = arr[high],arr[mid]
        high -= 1
print(arr)

# TC = 0(N)
# SC = 0(1)