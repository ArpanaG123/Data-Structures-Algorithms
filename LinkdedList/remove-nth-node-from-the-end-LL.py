# Remove Nth Node From End of List
# Link - https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

# Approach1
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        temp = head
        cnt = 0

        while temp is not None:
            cnt += 1
            temp = temp.next

        if cnt == n:
            return head.next
        
        res = cnt - n
        temp = head

        for i in range(res - 1):  # Stop just before the node to be removed
            temp = temp.next

        # Remove the nth node from the end by adjusting pointers
        temp.next = temp.next.next

        return head

# TC = 0(length of LL) + 0(length of ll - n(given))
# SC = 0(1)

# Approach2
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create a dummy node to handle edge cases like removing the first node
        
        fast = slow = head
        
        # Move the fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # If fast is None, it means we need to remove the head
        if fast is None:
            return head.next  # Remove the head by returning the next node as the new head

        # Move both fast and slow pointers until fast reaches the end
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node
        slow.next = slow.next.next
        
        # Return the head of the updated list
        return head
    
# TC = 0(len of LL)
# SC = 0(1)
