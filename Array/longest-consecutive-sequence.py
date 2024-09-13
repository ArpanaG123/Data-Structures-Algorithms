# Longest Consecutive Sequence in an Array. - Done
# Link - https://leetcode.com/problems/longest-consecutive-sequence/description/

arr = [102,4,100,1,101,3,2,1,1]

# Brute force

arr = [102,4,100,1,101,3,2,1,1]
n = len(arr)

def linearSearch(arr,x):
    for i in range(0,n):
        if arr[i] == x:
            return True
    return False


def longestConsecutive(arr):
    longest = 1
    for i in range(0,n):
        cnt = 1
        x = arr[i]
        
        while linearSearch(arr,x+1):
            x += 1
            cnt += 1
            
        longest = max(longest, cnt)
        
    return longest

result = longestConsecutive(arr)
print(result)

# TC = 0(n^2)
# sc = 0(1)

# Better
def longestSuccessiveElements(a):
    n = len(a)
    if n == 0:
        return 0

    # sort the array
    a.sort()
    lastSmaller = float('-inf')
    cnt = 0
    longest = 1

    # find longest sequence
    for i in range(n):
        if a[i] - 1 == lastSmaller:
            # a[i] is the next element of the
            # current sequence
            cnt += 1
            lastSmaller = a[i]
        elif a[i] != lastSmaller:
            cnt = 1
            lastSmaller = a[i]
        longest = max(longest, cnt)
    return longest

a = [100, 200, 1, 2, 3, 4]
ans = longestSuccessiveElements(a)
print("The longest consecutive sequence is:", ans)

# TC: O(NlogN) + O(N), N = size of the given array.
# Reason: O(NlogN) for sorting the array. To find the longest sequence, we are using a loop that results in O(N).

# SC: O(1), as we are not using any extra space to solve this problem.

# Optimal

def longestSuccessiveElements(a):
    n = len(a)
    if n == 0:
        return 0

    longest = 1
    st = set()
    # put all the array elements into set
    for i in range(n):
        st.add(a[i])

    # Find the longest sequence
    for it in st:
        # if 'it' is a starting number
        if it - 1 not in st:
            # find consecutive numbers
            cnt = 1
            x = it
            while x + 1 in st:
                x += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest

a = [100, 200, 1, 2, 3, 4]
ans = longestSuccessiveElements(a)
print("The longest consecutive sequence is", ans)
