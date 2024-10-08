# Longest subarray with given sum K(positives). only positive elements
# Link - https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-sub-array-with-sum-k

# Method1 - Brute force

arr = [10, 5, 2, 7, 1, 9]
K = 15

max_len = 0
start_idx = -1
end_idx = -1

n = len(arr)
for i in range(0,n):
    for j in range(i,n):
        sm = 0
        for k in range(i,j+1):
            sm += arr[k]
            
        if sm == K:
            curr_len = j-i+1
            
            if curr_len > max_len:
                max_len = max(curr_len,max_len)
                start_idx = i
                end_idx = j
            
print(f"longest subarray length:{max_len}")
print(f"longest subbarray with sum k is from: {start_idx} to {end_idx}")
print(f"longest subarray with sum k has elements:{arr[start_idx:end_idx+1]}")

# TC = 0(N^3)
# SC = 0(1)

# Method2 - Improved brute froce

arr = [10, 5, 2, 7, 1, 9]
K = 15

max_len = 0
start_idx = -1
end_idx = -1

n = len(arr)
for i in range(0,n):
    sm = 0
    for j in range(i,n):
        sm += arr[j]
            
        if sm == K:
            curr_len = j-i+1
            
            if curr_len > max_len:
                max_len = max(curr_len,max_len)
                start_idx = i
                end_idx = j
            
print(f"longest subarray length:{max_len}")
print(f"longest subbarray with sum k is from: {start_idx} to {end_idx}")
print(f"longest subarray with sum k has elements:{arr[start_idx:end_idx+1]}")

# TC = 0(N^2)
# SC = 0(1)

# Method3 - Hashing method

arr = [10, 5, 2, 7, 1, 9]
K = 15

n = len(arr)

max_len = 0
start_idx = -1
end_idx = -1
freq = {}
sm = 0

for i in range(0,n):
    sm += arr[i]
    
    if sm == K:
        max_len = max(max_len,i+1)
        start_idx = 0
        end_idx = i
    
    rem = sm - K
    
    if rem in freq:
        if i-freq[rem] > max_len:
            max_len = max(max_len,i-freq[rem])
            start_idx = freq[rem] + 1
            end_idx = i
    else:
        freq[sm] = i
# print(freq)

            
print(f"longest subarray length:{max_len}")
print(f"Longest subbarray with sum k is from: {start_idx} to {end_idx}")
print(f"Longest subarray with sum k has elements:{arr[start_idx:end_idx+1]}")

# Most optimal for positive and zero only - using two pointer

# arr = [1,2,3,1,1,1,1,3,3]
arr = [2,0,0,3]
K = 3

n = len(arr)

left = 0
right = 0
start = -1
end = -1
sm = arr[0]
mx = 0

while right < n:
    while left <= right and sm > K:
        sm -= arr[left]
        left += 1
    
    if sm == K:
        if right-left+1 > mx:
            mx = max(mx,right-left+1)
            start = left
            end = right
    
    right += 1
    if right < n :
        sm += arr[right]
        
            
print(f"longest subarray length:{mx}")
print(f"Longest subbarray with sum k is from: {start} to {end}")
print(f"Longest subarray with sum k has elements:{arr[start:end+1]}")

# TC = 0(2N)
# SC = 0(1)