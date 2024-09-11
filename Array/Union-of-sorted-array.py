# Find the Union of the two arrays.

# unsorted
arr1 =[85, 25, 1, 32, 54, 6]
arr2 = [85, 2]
# Output: 5

# Method1 - using python dictionary
arr1 =[85, 25, 1, 32, 54, 6]
arr2 = [85, 2]

freq = {}

for i in arr1:
    freq[i] = True
for i in arr2:
    freq[i] = True
res = list(freq.keys())
# print(freq)
print(res)
print(len(res))

# TC = 0(N*M)
# SC = 0(N)


# Method2 - Using manual loop and list

union = []
for i in arr1:
    if i not in union:
        union.append(i)
for i in arr2:
    if i not in union:
        union.append(i)
print(union)
print(len(union))

# TC = 0(N)
# SC = 0(N)

# Method3 - Using set  - most approached and efficient

arr1 =[85, 25, 1, 32, 54, 6]
arr2 = [85, 2]

union_set = set()
for i in arr1:
    union_set.add(i)
for i in arr2:
    union_set.add(i)
res = list(union_set)
print(res)
print(len(res))

# TC = 0(N)
# SC = 0(N)

# ============================================================================

# Find the Union of the two sorted arrays.
# Link - https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/0

# Method1 - using set
arr1 = [1, 1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5, 6]

st = set()
for num in arr1:
    st.add(num)
    
for num in arr2:
    st.add(num)

union = []
for i in st:
    union.append(i)
print(union)

# TC = 0(n1logn1) + 0(n2logn2) + 0(n1+n2)
# SC = 0(n1+n2) + 0(n1+n2)

# Method2 - using two pointer

arr1 = [1, 1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5, 6]

n1 = len(arr1)
n2 = len(arr2)

i = 0
j = 0

union = []

while i < n1 and j < n2:
    if arr1[i] <= arr2[j]:
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
    else:
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1


while i < n1:
    if not union or union[-1] != arr1[i]:
        union.append(arr1[i])
    i += 1

while j < n2:
    if not  union or union[-1] != arr2[j]:
        union.append(arr2[j])
    j += 1
    
print(union)

# TC = 0(N1+N2)
# SC = 0(N1+N2) = To return the result not for solving