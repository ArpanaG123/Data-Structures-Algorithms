# Longest subarray with sum K (Positives + Negatives).
# Link - https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=longest-sub-array-with-sum-k

# Handled all cases as positive, negative and zero
arr = [1, 12, 18, 13, 8, -2, 12, -1, -10, 6, 3, -14, 0 ,4,10, 0, -7, 3, -12, 18]
K = 30

n = len(arr)

max_len = 0
start_idx = -1
end_idx = -1
freq = {}
sm = 0

for i in range(n):
    sm += arr[i]
    
    # If cumulative sum equals K, update max_len directly
    if sm == K:
        max_len = i + 1
        start_idx = 0
        end_idx = i
    
    rem = sm - K
    
    # If remaining sum is found in dictionary, update max_len
    if rem in freq:
        if i - freq[rem] > max_len:
            max_len = max(max_len,i - freq[rem])
            start_idx = freq[rem] + 1
            end_idx = i
    
    # Store the first occurrence of sm
    if sm not in freq:
        freq[sm] = i

print(f"Longest subarray length: {max_len}")
print(f"Longest subarray with sum {K} is from: {start_idx} to {end_idx}")
print(f"Longest subarray with sum {K} has elements: {arr[start_idx:end_idx + 1]}")