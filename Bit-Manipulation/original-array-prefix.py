# . Find The Original Array of Prefix Xor
# Link - https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/

# You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:
# pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
# Note that ^ denotes the bitwise-xor operation.

 

pref = [5,2,0,3,1]
# Output: [5,7,2,3,2]

pref = [5,2,0,3,1]
n = len(pref)

res = [0]*n
res[0] = pref[0]

for i in range(1,n):
    res[i] = pref[i] ^ pref[i-1]
print(res)