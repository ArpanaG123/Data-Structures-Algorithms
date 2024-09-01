# Find the Union of the two sorted arrays.
# Link - https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/0

arr1 =[85, 25, 1, 32, 54, 6]
arr2 = [85, 2]
# Output: 5

# Method1 - using python dictionary

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

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3]

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