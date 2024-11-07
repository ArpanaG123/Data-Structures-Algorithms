# Sorted matrix
# Link - https://www.geeksforgeeks.org/problems/sorted-matrix2333/1

# Given an NxN matrix Mat. Sort all elements of the matrix.


N=4
Mat=[[10,20,30,40],
[15,25,35,45] 
[27,29,37,48] 
[32,33,39,50]]

# Output:
# 10 15 20 25 
# 27 29 30 32
# 33 35 37 39
# 40 45 48 50
# Explanation:sorting the matrix gives this result.

def sortedMatrix(mat):
    n = len(mat)
    
    flatten_mat = [element for row in mat for element in row]
    flatten_mat.sort()
    
    # Reconstruct the sorted matrix
    sorted_mat = []
    for i in range(n):
        sorted_mat.append(flatten_mat[i*n:(i+1)*n])
    
    return sorted_mat

mat = [[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]]
result = sortedMatrix(mat)
print(result)