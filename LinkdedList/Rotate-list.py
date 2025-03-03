# Rotate List
# Link - https://leetcode.com/problems/rotate-list/description/

# Given the head of a linked list, rotate the list to the right by k places.

# Input: head = [1,2,3,4,5]
# k = 2(Given)
# Output: [4,5,1,2,3]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head, k: int):
        if not head or not head.next or k == 0:
            return head
        
        # Find the length of the list
        tail = head
        sz = 1
        while tail.next:
            tail = tail.next
            sz += 1
        
        # Compute the effective rotations
        k = k % sz
        if k == 0:
            return head
        
        # Connect the tail to the head to make it circular
        tail.next = head
        
        # Find the new tail: (sz - k - 1)th node
        new_tail = head
        for _ in range(sz - k - 1):
            new_tail = new_tail.next
        
        # The new head is the next node
        new_head = new_tail.next
        
        # Break the circle
        new_tail.next = None
        
        return new_head
