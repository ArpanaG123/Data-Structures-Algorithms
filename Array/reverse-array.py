# Question Reverse the array.
# Link - https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

arr = [1, 2, 3]
# Output: array_reversed = [3, 2, 1]

# Method1
n = len(arr)
res = []

for i in range(n-1,-1,-1):
    res.append(arr[i])
print(res)
# TC = 0(N)
# SC = 0(N)

# Method2
n = len(arr)
i = 0
j = n-1

while i < j:
    arr[i],arr[j] = arr[j],arr[i]
    i += 1
    j -= 1

print(arr)

# TC = 0(N)
# SC = 0(1) - In-place reversal, meaning it doesn’t use additional space.

# Method3 - In-built method
arr = [1,2,3]
arr.reverse()
print(arr)

# TC = 0(N)
# SC = 0(1)
arr = [1,2,3]
rev_arr = arr[::-1]
print(rev_arr)

# TC = 0(N)
# SC = 0(N) - Extra space to returing the result

