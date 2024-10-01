# Reverse array
arr = [1, 2, 3, 4]
# Output: [4, 3, 2, 1]
# Explanation: The elements of the array are 1 2 3 4. After reversing the array, the first element goes to the last position,
# the second element goes to the second last position and so on. Hence, the answer is 4 3 2 1.

# using loop
def reverse(arr):
    n = len(arr)
    
    i = 0
    j = n-1
    
    while i < j:
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1
    return arr
    
arr = [1,2,3,4,5]
result = reverse(arr)
print(result)

# using recursion - parameterised recursion

def reverse(l,r):
    if l >= r:
        return 
    
    arr[l],arr[r] = arr[r],arr[l]
    
    reverse(l+1,r-1)
    
arr = [1,2,3,4,5]
n = len(arr)
l = 0
r = n-1

reverse(l,r)
print(arr)

# sum of array


arr = [1,2,3,4,5]
n = len(arr)

def sumOfArray(arr,n):
    
    if n == 1:
        return arr[0]
    
    return arr[0] + sumOfArray(arr[1:],n-1)

result = sumOfArray(arr,n)
print(result)

# find index 

arr = [9,8,10,8]
n = len(arr)
x = 10

def firstIndexfElement(arr,n,x):
    
    if arr[0] == x:
        return 0
        
    ans = firstIndexfElement(arr[1:],n-1,x)
    
    if ans == -1:
        return -1
    else:
        ans += 1

    return ans

result = firstIndexfElement(arr,n,x)
print(result)

arr = [9,8,10,8,8]
n = len(arr)
x = 8

def lastIndexfElement(arr,n,x):
    
    if n == 0:
        return -1
    
    ans = lastIndexfElement(arr[1:],n-1,x)
    
    if ans != -1:
        return ans + 1
    
    if arr[0] == x:
        return 0
    else:
        return -1

result = lastIndexfElement(arr,n,x)
print(result)

