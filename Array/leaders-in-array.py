# Array Leaders
# Given an array arr of n positive integers, your task is to find all the leaders in the array. An element of the array is considered a leader if it is greater than all the elements on its right side or if it is equal to the maximum element on its right side. The rightmost element is always a leader.
# Link - https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=leaders-in-an-array

arr = [16,17,4,3,5,2]
# Output: 17 5 2
# Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.


# Brute force

arr = [16,17,4,3,5,2]
n = len(arr)

ans = []
for i in range(0,n):
    leader = True
    
    for j in range(i+1,n):
        if arr[j] > arr[i]:
            leader = False
            break
    
    if leader == True:
        ans.append(arr[i])

print(ans)

# TC = 0(N^2)
# SC = 0(1) and 0(N) - to store answer

# Optimal

arr = [16,17,4,3,5,2]
n = len(arr)

mx = float('-inf')
ans = []
for i in range(n-1,-1,-1):
    if arr[i] > mx:
        ans.append(arr[i])
    
    # To keep track of maximum elemnt of right
    mx = max(arr[i],mx)

ans.reverse()
print(ans)

# TC = 0(N)
# SC = 0(1) and 0(N) - to store answer

# variety 2 for dupliactes also

def leaders(n, arr):
    #Code here
        
    mx = float('-inf')
        
    ans = []
        
    for i in range(n-1,-1,-1):
        if arr[i] >= mx:
            ans.append(arr[i])
            
            mx = arr[i]
            
    ans.reverse()
            
    return ans
