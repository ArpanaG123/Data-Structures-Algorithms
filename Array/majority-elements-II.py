# Majority Element II
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Link - https://leetcode.com/problems/majority-element-ii/description/

# Brue force
arr = [1,1,1,3,3,2,2,2]

n = len(arr)

ans = set()

for i in range(0,n):
    cnt = 0
    for j in range(0,n):
        if arr[i] == arr[j]:
            cnt += 1
    if cnt > n//3:
        ans.add(arr[i])
print(list(ans))

# TC = 0(N^2)
# SC = 0(N)

# using hashing
arr = [1, 1, 1, 3, 3, 2, 2, 2]
n = len(arr)

# Dictionary to store frequency counts
freq = {}

# Count the frequency of each element
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Store elements that appear more than n // 3 times
ans = set()
for key, value in freq.items():
    if value > n // 3:
        ans.add(key)

# Convert set to list and print result
print(list(ans))

# TC = 0(N)
# SC = 0(N)

# using moore's agorithm

def mooreVoting(arr):
    n = len(arr)
    
    # Step 1: Find two potential candidates for majority element
    candidate1, candidate2 = None, None
    count1, count2 = 0, 0
    
    for num in arr:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    
    # Step 2: Verify the candidates by counting their actual occurrences
    count1, count2 = 0, 0
    for num in arr:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
    
    # Step 3: Return the candidates that appear more than n // 3 times
    result = []
    if count1 > n // 3:
        result.append(candidate1)
    if count2 > n // 3:
        result.append(candidate2)
    
    return result

# Example usage
arr = [1, 1, 1, 3, 3, 2, 2, 2]
result = mooreVoting(arr)
print(result)
