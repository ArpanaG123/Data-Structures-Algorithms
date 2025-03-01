# Odd Even Linked List
# Link - https://leetcode.com/problems/odd-even-linked-list/description/

# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]


# Approach1
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
head = Node(1)
second = Node(3)
head.next = second
third = Node(4)
second.next = third
fourth = Node(2)
third.next = fourth
fifth = Node(5)
fourth.next = fifth
sixth = Node(6)
fifth.next = sixth

def printLinkedList(head):
    temp = head
    
    while temp is not None:
        print(temp.data,end="->")
        temp = temp.next
    print(None)
    
print("original linked list is:")
printLinkedList(head)

def oddEvenList(head):
    temp = head
    arr = []
    
    while temp is not None and temp.next is not None:
        arr.append(temp.data)
        temp = temp.next.next
        
    if temp is not None:
        arr.append(temp.data)
        
    if head is not None:
        temp = head.next

    while temp is not None and temp.next is not None:
        arr.append(temp.data)
        temp = temp.next.next
        
    if temp is not None:
        arr.append(temp.data)
    
    i = 0
    temp = head
    while temp is not None:
        temp.data = arr[i]
        i += 1
        temp = temp.next
    return head

head = oddEvenList(head)
print("linked list after Segrregation:")
printLinkedList(head)

# TC = 0(2N)
# SC = 0(N)

# Approach2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Create the linked list
head = Node(1)
second = Node(3)
head.next = second
third = Node(4)
second.next = third
fourth = Node(2)
third.next = fourth
fifth = Node(5)
fourth.next = fifth
sixth = Node(6)
fifth.next = sixth

# Function to print the linked list
def printLinkedList(head):
    temp = head
    while temp is not None:
        print(temp.data, end="->")
        temp = temp.next
    print(None)

print("Original linked list is:")
printLinkedList(head)

# Function to segregate odd and even indexed nodes
def oddEvenList(head):
    if head is None or head.next is None:
        return head
    
    odd = head  # First odd-indexed node
    even = head.next  # First even-indexed node
    evenHead = even  # Keep track of the even list's head
    
    while even is not None and even.next is not None:
        odd.next = odd.next.next  # Connect the next odd node
        even.next = even.next.next  # Connect the next even node
        odd = odd.next  # Move odd pointer forward
        even = even.next  # Move even pointer forward
    
    odd.next = evenHead  # Attach the even list to the end of the odd list
    return head

# Call the function to reorder the list
head = oddEvenList(head)
print("Linked list after segregation (odd indices first, then even):")
printLinkedList(head)

# TC = 0(N)
# SC = 0(1)

