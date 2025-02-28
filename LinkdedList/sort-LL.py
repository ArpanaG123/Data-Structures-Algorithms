# Sort List
# Link - https://leetcode.com/problems/sort-list/description/

# Given the head of a linked list, return the list after sorting it in ascending order.

# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

class Solution:
    def sortList(self, head):
        temp = head
        arr = []

        while temp is not None:
            arr.append(temp.val)
            temp = temp.next
        
        arr = sorted(arr)

        i = 0
        temp = head

        while temp is not None:
            temp.val = arr[i]
            i += 1
            temp = temp.next
        
        return head
    
# TC = 0(N) + 0(log N) + 0(N)
# SC = 0(N)

# Approach2 - using merge sort
