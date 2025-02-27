# Palindrome Linked List
# Link - https://leetcode.com/problems/palindrome-linked-list/description/

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false

# Approach1
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

def isPalindrome(head: ListNode) -> bool:
    stack = []
    temp = head

    # Traverse the linked list and push all values to the stack
    while temp:
        stack.append(temp.val)
        temp = temp.next

    # Traverse the linked list again and compare with the stack
    temp = head
    while temp:
        if temp.val != stack.pop():
            return False
        temp = temp.next

    return True

# Approach2
# Using two pointers approach (fast and slow) to find the middle of the list, then reversing the second half of the linked list, and finally comparing the two halves. This approach uses O(n) time and O(1) space.

# Here’s how the process works:
# Use the slow and fast pointers to find the middle of the list.
# Reverse the second half of the list.
# Compare the first half of the list with the reversed second half.
# If both halves match, the linked list is a palindrome.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev

def isPalindrome(head: ListNode) -> bool:
    if not head or not head.next:
        return True

    # Step 1: Use slow and fast pointers to find the middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the linked list
    second_half = reverseList(slow)

    # Step 3: Compare the first half and the reversed second half
    first_half, second_half_copy = head, second_half
    while second_half_copy:
        if first_half.val != second_half_copy.val:
            return False
        first_half = first_half.next
        second_half_copy = second_half_copy.next

    # Step 4: (Optional) Reverse the second half again to restore the original list
    reverseList(second_half)

    return True


