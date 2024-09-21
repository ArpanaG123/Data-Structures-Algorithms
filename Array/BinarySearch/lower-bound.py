# Implement lower bound

arr = [3,5,8,15,19]
x = 8
# output = 2

x = 16
# output = 4

x = 20
# output = 5(hypothetical index)

arr = [1,2,3,3,7,8,9,9,9,11]
x = 9

def lower_bound(arr,x):
    n = len(arr)
    
    low = 0
    high = n-1
    
    ans = -1
    
    while low <= high:
        mid = (low + high)//2
        
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans
    
result = lower_bound(arr,x)
print(result)

# TC = 0(logn)
# SC = 0(1)