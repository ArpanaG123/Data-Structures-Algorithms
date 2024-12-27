# Longest Substring Without Repeating Characters
# Link - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def longest_substring_without_repeating(s):
    n = len(s)
    seen = set()  # Hash set to store characters in the current window
    max_len = 0
    i = 0  # Left pointer

    for j in range(n):  # j is the right pointer, sliding over the string
        # If we encounter a repeating character, move the left pointer (i)
        while s[j] in seen:
            seen.remove(s[i])
            i += 1

        # Add the current character to the set
        seen.add(s[j])

        # Calculate the maximum length of the substring without repeating characters
        max_len = max(max_len, j - i + 1)

    return max_len