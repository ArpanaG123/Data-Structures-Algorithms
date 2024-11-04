# Maximum of Absolute Value Expression
# link - https://leetcode.com/problems/maximum-of-absolute-value-expression/description/

# Given two arrays of integers with equal lengths, return the maximum value of:
# |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
# where the maximum is taken over all 0 <= i, j < arr1.length.

arr1 = [1,2,3,4]
arr2 = [-1,4,5,6]
# Output: 13

def maxAbsValExpr(arr1,arr2):
    n = len(arr1)
    
    mx1 = mx2 = mx3 = mx4 = (-2**31)
    mn1 = mn2 = mn3 = mn4 = (2**31) - 1
    
    for i in range(n):
        exp1 = arr1[i] + arr2[i] + i
        exp2 = arr1[i] + arr2[i] - i
        exp3 = arr1[i] - arr2[i] + i
        exp4 = arr1[i] - arr2[i] - i
        
        mx1 = max(exp1,mx1)
        mn1 = min(exp1,mn1)
    
        mx2 = max(exp2,mx2)
        mn2 = min(exp2,mn2)
    
        mx3 = max(exp3,mx3)
        mn3 = min(exp3,mn3)
    
        mx4 = max(exp4,mx4)
        mn4 = min(exp4,mn4)
    
    result = max(mx1 - mn1, mx2 - mn2, mx3 - mn3, mx4 - mn4)

    return result

arr1 = [1,2,3,4]
arr2 = [-1,4,5,6]   
res = maxAbsValExpr(arr1,arr2)
print(res)