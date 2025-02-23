# Middle of the Linked List
# Link - https://leetcode.com/problems/middle-of-the-linked-list/description/

# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# Approach1 - 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(1)
second = Node(2)
head.next = second
third = Node(3)
second.next = third
fourth = Node(4)
third.next = fourth
fifth = Node(5)
fourth.next = fifth
tail = fifth
        

def printLinkedList(head):
    temp = head
    while temp is not None:
        print(temp.data,end = "->")
        temp = temp.next
    print(None)
    
print("Linked list:")
printLinkedList(head)

def middleNode(head):
    temp = head
    cnt = 0
    
    while temp is not None:
        cnt += 1
        temp = temp.next
    
    middleNode = cnt//2 + 1
    
    temp = head
    while temp is not None:
        middleNode -= 1
        if middleNode == 0:
            break
        temp = temp.next
    
    return temp

head = middleNode(head)
print("Middle Linked list:")   
printLinkedList(head)

# TC = 0(N + N/2)
# SC = 0(1)

# Approach2 - Tortoise and hare algorithm

# The Tortoise and Hare algorithm, also known as Floyd's Cycle Detection Algorithm, is a two-pointer technique used to detect cycles in a sequence or linked list. The algorithm is named after the idea of a race between a slow-moving "tortoise" and a fast-moving "hare."
# Algorithm Statement:
# Two pointers: The algorithm uses two pointers: a slow pointer (tortoise) and a fast pointer (hare).
# The slow pointer moves one step at a time.
# The fast pointer moves two steps at a time.
# Cycle detection:
# If there is no cycle, the fast pointer will reach the end of the sequence or linked list.
# If there is a cycle, at some point, the fast pointer will "lap" the slow pointer, meaning they will meet at the same node, confirming the presence of a cycle.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(1)
second = Node(2)
head.next = second
third = Node(3)
second.next = third
fourth = Node(4)
third.next = fourth
fifth = Node(5)
fourth.next = fifth
tail = fifth
        

def printLinkedList(head):
    temp = head
    while temp is not None:
        print(temp.data,end = "->")
        temp = temp.next
    print(None)
    
print("Linked list:")
printLinkedList(head)

def middleNode(head):
    slow = head
    fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    return slow

head = middleNode(head)
print("Middle Linked list:")   
printLinkedList(head)


# TC = 0(N/2)
# SC = 0(1)