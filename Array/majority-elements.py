# Majority elements
# Link - https://leetcode.com/problems/majority-element/description/

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

nums = [3,2,3]
# Output: 3

# Brute force
nums = [3, 2, 2]
n = len(nums)


# Brute force method to count the elements
arr = [2,2,3,3,1,2,2]
n = len(arr)

for i in range(0,n):
    cnt = 0
    for j in range(0,n):
        if arr[i] == arr[j]:
            cnt += 1

    if cnt > n/2:
        print(arr[i])
        break
else:
    print(-1)

# Better approach - using hashing

arr = [2,2,3,3,1,2,2]

n = len(arr)

freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for k,v in freq.items():
    if v > n//2:
        print(k)

# TC = 0(N)
# SC = 0(N)

#optimal - using moore's voting algotithm
nums = [1,2,2]

n = len(nums)
candidate = nums[0]
cnt = 0

for i in range(n):
    if cnt == 0:
        candidate = nums[i]
    if nums[i] == candidate:
        cnt += 1
    else:
        cnt -= 1

print("Candidates count with greater than n//2:",candidate)

# TC = 0(N)
# SC = 0(1)
