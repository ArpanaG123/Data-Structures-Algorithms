# Count subarrays with xor K.

arr = [4,2,2,6,4]
# Output = 4

# Brute force

arr = [4,2,2,6,4]
k = 6

n = len(arr)
count = 0

for i in range(0,n):
    for j in range(i,n):
        xor = 0
        for k in range(i,j+1):
            xor ^= arr[k]
            
            if xor == k:
                count += 1
                
print(f"subarray count with xor is equal to k is: {count}")

# TC = 0(n^3)
# sc = 0(1)

# Better
arr = [4,2,2,6,4]
k = 6

n = len(arr)
count = 0

for i in range(0,n):
    xor = 0
    for j in range(i,n):
        xor ^= arr[j]
            
        if xor == k:
            count += 1
                
print(f"subarray count with xor is equal to k is: {count}")

# TC = 0(n^2)
# sc = 0(1)

# Optimal

arr = [4,2,2,6,4]
k = 6

n = len(arr)

count = 0
xor = 0

freq = {0:1}

for i in range(0,n):
    xor ^= arr[i]
    
    # Calculate the remainder we need to find in the freq dictionary
    rem = xor ^ k
    
    # If rem is in the freq dictionary, it means there's a subarray
    # with XOR equal to k, so add the number of occurrences of this rem.
    if rem in freq:
        count += freq[rem]
    
    # Update the frequency of the current xor value in the freq dictionary
    if xor in freq:
        freq[xor] += 1
    else:
        freq[xor] = 1
        
                
print(f"subarray count with xor is equal to k is: {count}")

# TC = 0(n)
# sc = 0(1)
