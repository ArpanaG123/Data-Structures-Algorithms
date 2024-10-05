# Letter Combinations of a Phone Number
# Link - https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

def letterCombinations(digits):
    letters = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    
    if not digits:
        return []
    
    ans = []
    
    digits = int(digits)
    
    def helper(num,temp):
        if num == 0:
            ans.append(temp)
            return 
        
        curr_digit = num % 10
        
        for letter in letters[curr_digit]:
            # Recur with the next digit, adding the current letter to temp
            helper(num//10,letter+temp)
    
    helper(digits,"")
    return ans
    
digits = "23"   
result = letterCombinations(digits)
print(result)