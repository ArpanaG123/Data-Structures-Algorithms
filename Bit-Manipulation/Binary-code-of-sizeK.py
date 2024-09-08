# Check If a String Contains All Binary Codes of Size K
# Link - https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/

# Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.
s = "00110110"
k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.

n = len(s)
total_subsets_of_len_k = 1<<k
hash_set = set()

for i in range(0,n):
    if i+k <= n:
        hash_set.add(s[i:i+k])

if len(hash_set) == total_subsets_of_len_k:
    print(True)
else:
    print(False)

# TC = 0(N*K)
# SC = 0(SIZE Of hash_set * k)