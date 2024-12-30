# Palindrome Pairs
# Link - https://leetcode.com/problems/palindrome-pairs/description/

# You are given a 0-indexed array of unique strings words.
# A palindrome pair is a pair of integers (i, j) such that: 0 <= i, j < words.length,i != j, and words[i] + words[j] (the concatenation of the two strings) is a palindrome.
# Return an array of all the palindrome pairs of words.
# You must write an algorithm with O(sum of words[i].length) runtime complexity.


# Example 1:
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]

# Example 2:
# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]

# Approach1 - Brute force
def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False

def palindrome_pairs(words):
    res = []
    n = len(words)
    
    # Compare every pair of words
    for i in range(n):
        for j in range(n):
            if i != j:
                # Check words[i] + words[j]
                if is_palindrome(words[i] + words[j]):
                    res.append([i, j])
    return res

# Example usage:
words = ["abcd", "dcba", "lls", "s", "sssll"]
print(palindrome_pairs(words))

# TC = 0(N^2) * 0(N)
# SC = 0(1)

# Optimal 

class Solution:
    def is_palindrome(self, word):
        return word == word[::-1]

    def palindromePairs(self, words):
        word_map = {}

        # Create a map of reversed words
        for i in range(len(words)):
            word_map[words[i][::-1]] = i  # Store reversed word with its index
        
        res = []

        # Iterate over the words
        for i in range(len(words)):
            word = words[i]
            n = len(word)

            # Split the word into prefix and suffix
            for j in range(n + 1):
                prefix = word[:j]
                suffix = word[j:]

                # Case 1: Check if prefix is a palindrome and reverse of suffix exists in the map
                if self.is_palindrome(prefix) and suffix in word_map and word_map[suffix] != i:
                    res.append([word_map[suffix], i])

                # Case 2: Check if suffix is a palindrome and reverse of prefix exists in the map
                # Make sure to avoid the whole word being treated twice
                if j != n and self.is_palindrome(suffix) and prefix in word_map and word_map[prefix] != i:
                    res.append([i, word_map[prefix]])
    
        return res


