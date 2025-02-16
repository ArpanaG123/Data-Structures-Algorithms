# Deletion in Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to print all the values in the linked list
def printAllLL(head):
    current = head
    while current is not None:
        print(current.data, end="->")
        current = current.next  # Move to the next node
    print("None")
    
# Creating a linked list with nodes
head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(60)
fifth = Node(70)
sixth = Node(80)

head.next = second  # Link first node to second
second.next = third  # Link second node to third
third.next = fourth  # Link third node to fourth
fourth.next = fifth # Link fourth node to fifth
fifth.next = sixth  # Link fifth node to sixth

# Print all linked list data
print("Original Linked List:")
printAllLL(head)

# Function to delete the head node of the linked list
def deleteHeadOfLL(head):
    if head is None:
        return None
    temp = head.next  # Save the next node
    head = None  # Free the old head
    return temp  # Return the new head
    
# Deleting the head node
head = deleteHeadOfLL(head)
print("After deleting the head:")
printAllLL(head)

# Function to delete the tail node of the linked list
def deleteTailOfLL(head):
    if head is None or head.next is None:
        return None

    temp = head
    
    # The loop continues until the second-last node
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None  # Remove the tail node
    return head
    
# Deleting the tail node
head = deleteTailOfLL(head)
print("After deleting the tail:")
printAllLL(head)

# Function to delete the k-th element in the linked list
def deleteKthElementInLL(head, k):
    if head is None:
        return None
        
    if k == 1:
        temp = head.next
        head = None
        return temp
        
    cnt = 1
    temp = head
    prev = None
    while temp is not None and cnt < k:
        prev = temp
        temp = temp.next
        cnt += 1
    if temp is not None:
        prev.next = temp.next
        temp = None
    return head


# Deleting the kth element (which is 20)
head = deleteKthElementInLL(head,1)
print("After deleting the kth element:")
printAllLL(head)

def deleteElementInLL(head,el):
    if head is None:
        return None
    
    if head.data == el:
        temp = head
        head = head.next
        temp = None
        return head
    
    prev = None
    temp = head
    
    while temp is not None:
        if temp.data == el:
            prev.next = temp.next
            temp = None
            return head
        prev = temp
        temp = temp.next
    return head

# Deleting a value from the linked list
head = deleteElementInLL(head, 60)
print("After deleting the value:")
printAllLL(head)