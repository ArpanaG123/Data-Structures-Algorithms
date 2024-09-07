# Largest subarray with 0 sum
# Link - Link - https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1?category%5B%5D=Hash&company%5B%5D=Amazon&page=1&query=category%5B%5DHashcompany%5B%5DAmazonpage1company%5B%5DAmazoncategory%5B%5DHash&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=largest-subarray-with-0-sum

arr = [15,-2,2,-8,1,7,10,23]
# Output: 5
# Explanation: The largest subarray with sum 0 is -2 2 -8 1 7.

# Method1 - Brute force

arr = [15,-2,2,-8,1,7,10,23]
n = len(arr)
max_len = 0
start_idx = -1
end_idx = -1


for i in range(0,n):
    for j in range(i,n):
        sm = 0
        for k in range(i,j+1):
            sm += arr[k]
    
        if sm == 0:
            curr_len = j-i+1
            
            if curr_len > max_len:
                max_len = curr_len
                start_idx = i
                end_idx = j
if max_len == 0:
        print("No subarray with sum 0 found.")
else:
    print(f"maximum length of subarray with sum 0 is : {max_len}")
    print(f"Index of the maximum subarray with sum 0 is from {start_idx} to {end_idx}")
    print(f"The subarray is: {arr[start_idx:end_idx+1]}")

# TC = 0(N^3)
# SC = 0(1)

# Method2 - Improved Brute force

arr = [15,-2,2,-8,1,7,10,23]
n = len(arr)
max_len = 0
start_idx = -1
end_idx = -1


for i in range(0,n):
    sm = 0
    for j in range(i,n):
        sm += arr[j]
    
        if sm == 0:
            curr_len = j-i+1
            
            if curr_len > max_len:
                max_len = curr_len
                start_idx = i
                end_idx = j
if max_len == 0:
        print("No subarray with sum 0 found.")
else:
    print(f"maximum length of subarray with sum 0 is : {max_len}")
    print(f"Index of the maximum subarray with sum 0 is from {start_idx} to {end_idx}")
    print(f"The subarray is: {arr[start_idx:end_idx+1]}")

# TC = 0(N^2)
# SC = 0(1)

# Method3 - Hash map(optimal and efficient)

arr = [15,-2,2,-8,1,7,10,23]
n = len(arr)

max_len = 0

start_idx = -1
end_idx = -1

freq = {}
sm = 0


for i in range(0,n):
    sm += arr[i]
    
    if sm == 0:
        max_len = i+1
        start_idx = 0
        end_idx = i
    
    if sm in freq:
        max_len = max(max_len,i-freq[sm])
        start_idx = freq[sm]+1
        end_idx = i
    else:
        freq[sm] = i
        
# print(freq)
    
if max_len == 0:
        print("No subarray with sum 0 found.")
else:
    print(f"maximum length of subarray with sum 0 is : {max_len}")
    print(f"Index of the maximum subarray with sum 0 is from {start_idx} to {end_idx}")
    print(f"The subarray is: {arr[start_idx:end_idx+1]}")

# TC = 0(N)
# SC = 0(1)