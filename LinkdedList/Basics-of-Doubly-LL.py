class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None

head = Node(1)
second = Node(2)
head.next = second
second.back = head
third = Node(3)
second.next = third
third.back = second
fourth = Node(4)
third.next = fourth
fourth.back = third
fifth = Node(5)
fourth.next = fifth
fifth.back = fourth

# Print linked list
def printDoublyLL(head):
    temp = head
    while temp is not None:
        print(temp.data, end="<->")
        temp = temp.next
    print(None)

print("Doubly linked list is:")
printDoublyLL(head)


# deletion in doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None
        
head = Node(1)
second = Node(2)
head.next = second
second.back = head
third = Node(3)
second.next = third
third.back = second
fourth = Node(4)
third.next = fourth
fourth.back = third
fifth = Node(5)
fourth.next = fifth
fifth.back = fourth

# Print linked list
def printDoublyLL(head):
    temp = head
    while temp is not None:
        print(temp.data, end="<->")
        temp = temp.next
    print(None)

print("Doubly linked list is:")
printDoublyLL(head)


# 1.delete head of doubly LL
def deleteHeadOfDoublyLL(head):
    if head is None:
        return None
    
    # if only one node is LL
    if head.next is None:
        return None
        
    
    new_head = head.next
    new_head.back = None
    head.next = None
    
    return new_head
    
head = deleteHeadOfDoublyLL(head)
print("Doubly linked list after deleting head:")
printDoublyLL(head)

# 2.Function to delete the tail node of the doubly linked list
def deleteTailOfDoublyLL(head):
    if head is None:
        return None  # Empty list case

    # If there is only one node in the list
    if head.next is None:
        return None  # Return None as the list becomes empty after deletion

    # Traverse to the last node
    temp = head
    while temp.next is not None:
        temp = temp.next

    # Now temp is the last node, we want to remove it
    prev = temp.back  # Get the second-to-last node
    prev.next = None # Break from the second-to-last node to the last node
    temp.back = None  # Clear the back reference of the node to be deleted 
    return head  # Return the head of the updated list

# Delete the tail node
head = deleteTailOfDoublyLL(head)

# Print the doubly linked list after deleting tail
print("Doubly linked list after deleting tail:")
printDoublyLL(head)

# 3.Deleting kth node in doubly linked list
def deleteKthNodeOfDoublyLL(head, k):
    if head is None or k <= 0:  # Handle invalid k values
        return None
    
    temp = head
    cnt = 1  # Start from 1 because k is typically 1-based
    
    # Traverse to the k-th node
    while temp is not None and cnt < k:
        temp = temp.next
        cnt += 1
    
    if temp is None:  # If k is out of bounds
        return head

    # If the k-th node is the head
    if temp.back is None:
        return deleteHeadOfDoublyLL(head)
    
    # If the k-th node is the tail
    if temp.next is None:
        return deleteTailOfDoublyLL(head)

    # General case: Deleting a node in the middle
    prev = temp.back
    front = temp.next
    
    prev.next = front
    front.back = prev
    
    # Cleanup the current node
    temp.next = None
    temp.back = None
    
    return head

head = deleteKthNodeOfDoublyLL(head,2)

# Print the doubly linked list after deleting kth node
print("Doubly linked list after deleting kth node:")
printDoublyLL(head)