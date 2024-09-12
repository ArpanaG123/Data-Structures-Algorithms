# 2SUM
# Link - https://leetcode.com/problems/two-sum/description/

nums = [2,7,11,15]
target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# Brute force
n = len(nums)

# Type1 -
for i in range(0,n):
    for j in range(i+1,n):
        if nums[i] + nums[j] == target:
            print("YES")


# Type2 - 
for i in range(0,n):
    for j in range(i+1,n):
        if nums[i] + nums[j] == target:
            print([i,j])
            break

# TC = 0(N^2)
# SC = 0(1)

# Better approach - Hashing

nums = [2,7,11,15]
target = 9
# Output: [0,1]

# Type1
n = len(nums)

hash_map = {}

for i in range(0,n):
    a = nums[i]
    need = target - a
    
    if need in hash_map:
        print([hash_map[need],i])
    else:
        hash_map[a] = i
print(hash_map)

# Type2
n = len(nums)

hash_map = {}

for i in range(0,n):
    a = nums[i]
    need = target - a
    
    if need in hash_map:
        print("YES")
    else:
        hash_map[a] = i
print(hash_map)

# TC = 0(N)
# SC = 0(N)

# Optimal approach
# type2 only

nums = [2,7,11,15]
target = 9

nums.sort()
n = len(nums)

left = 0
right = n-1

while left < right:
    sm = nums[left] + nums[right]
    
    if sm == target:
        print("YES")
        break
    elif sm < target:
        left += 1
    else:
        right -= 1
else:
    print("NO")