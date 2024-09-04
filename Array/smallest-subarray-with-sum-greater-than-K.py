# Smallest Subarray with sum greater than a given value K.
# Link - https://practice.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x/0

# Method1 - Brute force

arr = [1, 4, 45, 6, 0, 19]
X = 51

# output = 3

n = len(arr)
start = -1
end = -1
smallest_len = float('inf')

for i in range(0,n):
    for j in range(i,n):
        sm = 0
        for k in range(i,j+1):
            sm += arr[k]
            
            if sm > X:
                curr = j-i+1
                
                if curr < smallest_len:
                    smallest_len = curr
                    start = i
                    end = j
                break
            
if smallest_len == float('inf'):
    print("No subarray found")
else:
    print(f"smallest subarray with sum greater than X:{smallest_len}")
    print(f"smallest subarray with sum greater than X from :{start} to {end}")
    print(f"smallest subarray with sum greater than X of array:{arr[start:end+1]}")

# TC = 0(N^3)
# SC = 0(1)

# Mathod2 - Better approach
arr = [1, 4, 45, 6, 0, 19]
X = 51

# output = 3

n = len(arr)
start = -1
end = -1
smallest_len = float('inf')

for i in range(0,n):
    sm = 0
    for j in range(i,n):
            sm += arr[j]
            
            if sm > X:
                curr = j-i+1
                
                if curr < smallest_len:
                    smallest_len = curr
                    start = i
                    end = j
                break
            
if smallest_len == float('inf'):
    print("No subarray found")
else:
    print(f"smallest subarray with sum greater than X:{smallest_len}")
    print(f"smallest subarray with sum greater than X from :{start} to {end}")
    print(f"smallest subarray with sum greater than X of array:{arr[start:end+1]}")

# TC = 0(N^3)
# SC = 0(1)

# Mathod3 - Optimal approach(prefix sum and sliding window)

arr = [1, 4, 45, 6, 0, 19]
X = 51

# output = 3

n = len(arr)
start = -1
end = -1
st = 0
smallest_len = float('inf')
sm = 0

for i in range(0,n):
    sm += arr[i]
    
    while sm > X:
        if i - st + 1 < smallest_len:
            smallest_len = i - st + 1
            start = st
            end = i
        sm -= arr[st]
        st += 1

        
if smallest_len == float('inf'):
    print("No subarray found")
else:
    print(f"smallest subarray with sum greater than X:{smallest_len}")
    print(f"smallest subarray with sum greater than X from :{start} to {end}")
    print(f"smallest subarray with sum greater than X of array:{arr[start:end+1]}")
