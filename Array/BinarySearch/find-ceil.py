# ceil of the array

arr = [1,2,8,10,11,12,19]
x = 9

def find_ceil(arr,x):
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
    
result = find_ceil(arr,x)
print(result)

# TC = 0(logn)
# SC = 0(1)

# Type2

def getFloorAndCeil(self, x: int, arr: list) -> list:
    # code here
    arr.sort()
        
    n = len(arr)
        
    low = 0
    high = n-1
        
    floor = -1
    ceil = -1
        
    while low <= high:
        mid = (low+high)//2
            
        if arr[mid] == x:
            return [arr[mid], arr[mid]]
            
        elif arr[mid] < x:
            floor = arr[mid]
            low = mid + 1
        else:
            ceil = arr[mid]
            high = mid - 1
                
    return [floor,ceil]

x = 7 
arr = [5, 6, 8, 9, 6, 5, 5, 6]
# Output: 6, 8
# Explanation: Floor of 7 is 6 and ceil of 7 is 8.