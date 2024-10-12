# Check if array is sorted or not - 

# Brute force

arr = [1,2,3,4,2]
n = len(arr)

for i in range(1,n):
    if arr[i] >= arr[i-1]:
        continue
    else:
        print(False)
        break
else:
    print(True)

# TC = 0(N)
# SC = 0(1)

# Check if Array Is Sorted and Rotated
# LINK - https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

# case1 = array is sorted = 1,2,3,4,5 if arr[last] > arr[0] = True
# case2 = atleast 1 pair exist whose - [3,4,5,1,2],arr[i-1] > arr[i] - True
# case3 - Neither sorted not rotated - [2,1,3,4] - False
# case4 - all elements are equal - [1,1,1] - True

# code -
def check(nums):
    n = len(nums)
    count_pair = 0

    for i in range(1,n):
        if nums[i-1] > nums[i]:
            count_pair += 1

    if nums[n-1] > nums[0]:
        count_pair += 1
        
    if count_pair <= 1:
        return True
    else:
        return False

nums = [3,4,5,1,2]
result = check(nums)
print(result)

# TC = 0(N)
# SC = 0(1)