# 

# Approach1 - Brute force

def previousSmallerElement(arr):
    n = len(arr)
    
    prev_smaller = [-1]*n
    
    for i in range(n):
        for j in range(i-1,-1,-1):
            if arr[j] < arr[i]:
                prev_smaller[i] = arr[j]
                break
    return prev_smaller

arr = [4,5,2,10,8] 
result = previousSmallerElement(arr)
print(result)

# TC = 0(N^2)
# SC = 0(N)

# Approach2 - Using monotonic stack

def previousSmallerElement(arr):
    n = len(arr)
    
    st = []
    prev_smaller = [-1]*n
    
    for i in range(n):
        while len(st) != 0 and st[-1] >= arr[i]:
            st.pop()
        if len(st) == 0:
            prev_smaller[i] = -1
        else:
            prev_smaller[i] = st[-1]
        st.append(arr[i])
        i += 1
        
    return prev_smaller
            
arr = [4,5,2,10,8] 
result = previousSmallerElement(arr)
print(result)

# TC = 0(2N)
# SC = 0(N) + 0(N)