# Upper bound

arr = [2,3,6,7,8,8,11,11,11,12]
x = 11

def upper_bound(arr,x):
    n = len(arr)
    
    low = 0
    high = n-1
    
    ans = -1
    
    while low <= high:
        mid = (low + high)//2
        
        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans
    
result = upper_bound(arr,x)
print(result)

# TC = 0(logn)
# SC = 0(1)