#  Reverse Linked List
# Link - https://leetcode.com/problems/reverse-linked-list/description/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
head = Node(2)
second = Node(5)
head.next = second
third = Node(7)
second.next = third
fourth = Node(10)
third.next = fourth

def printLinkedList(head):
    temp = head
    while temp is not None:
        print(temp.data, end="->")
        temp = temp.next
    print(None)
    
print("Original linked list is:")
printLinkedList(head)

# Iterative Approaches - 

# Approach1
def reverseLinkedList(head):
    stack = []
    temp = head
    
    while temp is not None:
        stack.append(temp)
        temp = temp.next
    
    head = stack.pop()
    temp = head
    while stack:
        temp.next = stack.pop()
        temp = temp.next
        
    temp.next = None #setting last node to None
    return head

head = reverseLinkedList(head)
print("Linked list after reverse:")
printLinkedList(head)

# TC = 0(N) for STEP1 and for STEP2 0(N) = 0(2N)
# SC = 0(N)

# Approach2
def reverseLinkedList(head):
    prev = None
    curr = head

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
    
# Reversing the linked list and updating the head
head = reverseLinkedList(head)

print("Linked list after reverse:")
printLinkedList(head)

# TC = 0(N)
# SC = 0(1)


