# Sum of Subarray Ranges
# Link - https://leetcode.com/problems/sum-of-subarray-ranges/description/

# You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.
# Return the sum of all subarray ranges of nums.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Input: nums = [1,2,3]
# Output: 4
# Explanation: The 6 subarrays of nums are the following:
# [1], range = largest - smallest = 1 - 1 = 0 
# [2], range = 2 - 2 = 0
# [3], range = 3 - 3 = 0
# [1,2], range = 2 - 1 = 1
# [2,3], range = 3 - 2 = 1
# [1,2,3], range = 3 - 1 = 2
# So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

# Brute force
def subArrayRanges(arr):
    n = len(arr)
    ans = 0

    for i in range(n):
        largest = arr[i]
        smallest = arr[i]
        for j in range(i,n):
            largest = max(arr[j],largest)
            smallest = min(arr[j],smallest)
            
            ans = ans + (largest - smallest)
    return ans

arr = [1,4,3,2] 
result = subArrayRanges(arr)
print(result)

# TC = 0(N^2)
# SC = 0(1)

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
        while len(st) != 0 and arr[st[-1]] >= arr[i]:
            st.pop()
        if len(st) == 0:
            pse[i] = -1
        else:
            pse[i] = st[-1]
        st.append(i)
    return pse

def findNextLarger(arr):
    n = len(arr)
    nle = [n] * n
    st = []

    for i in range(n):
        while len(st) != 0 and arr[st[-1]] < arr[i]:
            nle[st.pop()] = i
        st.append(i)
    return nle


def findPreviousLarger(arr):
    n = len(arr)
    ple = [-1] * n
    st = []

    for i in range(n):
        while len(st) != 0 and arr[st[-1]] <= arr[i]:
            st.pop()
        if len(st) == 0:
            ple[i] = -1
        else:
            ple[i] = st[-1]
        st.append(i)
    return ple

   
def sumSubarrayMins(arr):
    n = len(arr)
    
    nse = findNextSmaller(arr)
    pse = findPreviousSmaller(arr)
    MOD = 10**9 + 7
    mini = 0

    for i in range(n):
        left = i - pse[i]
        right = nse[i] - i
        
        mini = (mini + (right * left * arr[i]) % MOD) % MOD
                
    return mini
    
def sumSubarrayMaxs(arr):
    n = len(arr)
    nle = findNextLarger(arr)
    ple = findPreviousLarger(arr)
    MOD = 10**9 + 7
    maxi = 0

    for i in range(n):
        left = i - ple[i]
        right = nle[i] - i
        maxi = (maxi + (right * left * arr[i]) % MOD) % MOD

    return maxi


def subArrayRanges(nums):
    
        MOD = 10**9 + 7
        max_sum = sumSubarrayMaxs(nums)
        min_sum = sumSubarrayMins(nums)
        
        result = (max_sum - min_sum + MOD) % MOD

        return result

nums = [1,4,3,2] 
result = subArrayRanges(nums)
print(result)

# TC = 0(10N)
# SC = 0(10N)