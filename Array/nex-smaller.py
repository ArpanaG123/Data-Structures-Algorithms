# next smaller - GFG

def leftSmaller(arr):
    n = len(arr)
    st = []
    ans = []
    
    for i in range(n):
        while (len(st) and st[-1] >= arr[i]):
            st.pop()
        
        if len(st):
            ans.append(st[-1])
        else:
            ans.append(-1)
        
        st.append(arr[i])
    
    return ans

    
arr = [1,6,4,10,2,5]
res = leftSmaller(arr)
print(res)