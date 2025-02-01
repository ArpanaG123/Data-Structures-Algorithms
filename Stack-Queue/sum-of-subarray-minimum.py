# Sum of Subarray Minimums
# Link - https://leetcode.com/problems/sum-of-subarray-minimums/description/

# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.


# Input: arr = [3,1,2,4]
# Output: 17
# Explanation: 
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.


# Brute force
def sumSubarrayMins(arr):
    
    n = len(arr)
    MOD = 10**9 + 7

    ans = 0

    for i in range(n):
        mini = arr[i]
        for j in range(i,n):
            mini = min(mini,arr[j])
            ans = (ans + mini)%MOD
                
    return ans
            
arr = [3,1,2,4] 
result = sumSubarrayMins(arr)
print(result)

# Optimal

def findNextSmaller(arr):
    n = len(arr)
    nse = [n] * n
    st = []
    
    i = 0
    while i < n:
        while len(st) != 0 and arr[st[-1]] > arr[i]:
            nse[st.pop()] = i
        st.append(i)
        i += 1
    return nse


def findPreviousSmaller(arr):
    n = len(arr)
    pse = [-1] * n
    st = []

    for i in range(n):
        while len(st) != 0 and arr[st[-1]] > arr[i]:
            st.pop()
        if len(st) == 0:
            pse[i] = -1
        else:
            pse[i] = st[-1]
        st.append(i)
    return pse


def sumSubarrayMins(arr):
    n = len(arr)
    
    nse = findNextSmaller(arr)
    pse = findPreviousSmaller(arr)
    MOD = 10**9 + 7
    ans = 0

    for i in range(n):
        left = i - pse[i]
        right = nse[i] - i
        
        ans = (ans + (right * left * arr[i]) % MOD) % MOD
                
    return ans

arr = [3, 1, 2, 4] 
result = sumSubarrayMins(arr)
print(result)

# TC = 0(5N)
# SC = 0(5N)