# Delete the Middle Node of a Linked List
# Link - https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/

# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.


# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Explanation:
# The above figure represents the given linked list. The indices of the nodes are written below.
# Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
# We return the new list after removing this node. 


# Input: head = [1,2,3,4]
# Output: [1,2,4]
# Explanation:
# The above figure represents the given linked list.
# For n = 4, node 2 with value 3 is the middle node, which is marked in red.

# Input: head = [2,1]
# Output: [2]
# Explanation:
# The above figure represents the given linked list.
# For n = 2, node 1 with value 1 is the middle node, which is marked in red.
# Node 0 with value 2 is the only node remaining after removing node 1.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create the linked list
head = Node(1)
second = Node(2)
head.next = second
third = Node(3)
second.next = third
fourth = Node(4)
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

print("Linked list:")
printLinkedList(head)

# Brute force approach to delete the middle node
def deleteMiddleNode(head):
    if head is None or head.next is None:
        return None  # If there's only one or zero nodes, return None (no middle node to delete)
    
    # Step 1: Count the total number of nodes
    temp = head
    count = 0
    while temp is not None:
        count += 1
        temp = temp.next
    
    # Step 2: Find the middle node position (1-based index)
    middle = count // 2  # Middle node's index (0-based)
    
    # If there is only one node or no middle node to delete
    if middle == 0:
        return head.next  # In case of a single node, just return None
    
    # Step 3: Traverse the list again to the node just before the middle node
    temp = head
    for i in range(middle - 1):
        temp = temp.next
    
    # Step 4: Remove the middle node
    if temp is not None and temp.next is not None:
        temp.next = temp.next.next  # Skip over the middle node
    
    return head

# Delete the middle node
head = deleteMiddleNode(head)
print("Linked list after deleting the middle node:")
printLinkedList(head)

# Approach2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create the linked list
head = Node(1)
second = Node(2)
head.next = second
third = Node(3)
second.next = third
fourth = Node(4)
third.next = fourth
fifth = Node(5)
fourth.next = fifth

# Function to print the linked list
def printLinkedList(head):
    temp = head
    while temp is not None:
        print(temp.data, end="->")
        temp = temp.next
    print(None)

print("Linked list:")
printLinkedList(head)

# Function to delete the middle node
def deleteMiddleNode(head):
    if head is None or head.next is None:
        return None  # If there's only one or zero nodes, return None (no middle node to delete)
    
    slow = head
    fast = head
    prev = None
    
    # Move `fast` by 2 steps and `slow` by 1 step to find the middle
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        prev = slow
        slow = slow.next
    
    # `slow` now points to the middle node, `prev` points to the node before `slow`
    prev.next = slow.next  # Remove the middle node by skipping over it
    
    return head

# Delete the middle node
head = deleteMiddleNode(head)
print("Linked list after deleting middle node:")
printLinkedList(head)

