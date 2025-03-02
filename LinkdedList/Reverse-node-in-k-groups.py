# Reverse Nodes in k-Group
# Link - https://leetcode.com/problems/reverse-nodes-in-k-group/description/

# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.


# Input: head = [1,2,3,4,5]
# k = 2
# Output: [2,1,4,3,5]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        # Helper function to find the k-th node from the current node
        def findKthNode(node, k):
            while node and k > 1:
                node = node.next
                k -= 1
            return node
        
        # Helper function to reverse a sublist starting from 'head'
        def reverseList(head):
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        temp = head
        prevLast = None
        new_head = None
        
        while temp:
            kthNode = findKthNode(temp, k)

            if not kthNode:
                break
            
            nextNode = kthNode.next
            kthNode.next = None  # Temporarily disconnect the group
            
            # Reverse the current group
            reversed_head = reverseList(temp)
            
            if not new_head:
                new_head = reversed_head
            
            if prevLast:
                prevLast.next = reversed_head
            
            prevLast = temp  # The original head of the current group becomes the tail after reversal
            temp = nextNode  # Move to the next group
        
        # After the loop, attach the remaining part (if any)
        if prevLast:
            prevLast.next = temp

        return new_head if new_head else head
