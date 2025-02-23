# Reverse doubly Linked list
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
tail = fifth

# Print linked list
def printDoublyLL(head):
    temp = head
    while temp is not None:
        print(temp.data, end="<->")
        temp = temp.next
    print(None)

print("Doubly linked list is:")
printDoublyLL(head)

# Approach1 - Brute force using stack
def reverseDoublyLLPointersUsingStack(head):
    stack = []
    temp = head
    
    # Push all the nodes onto the stack
    while temp is not None:
        stack.append(temp)
        temp = temp.next
    
    # Pop from the stack and adjust the next and back pointers
    new_head = stack.pop()  # The last node becomes the new head
    temp = new_head
    
    while stack:
        node = stack.pop()
        temp.next = node  # Set the next pointer
        node.back = temp  # Set the back pointer
        temp = node
    
    # Set the next pointer of the last node (new tail) to None
    temp.next = None
    
    return new_head

# Reversing the linked list pointers
head = reverseDoublyLLPointersUsingStack(head)
print("Doubly linked list after reverse (with pointers):")
printDoublyLL(head)

# TC = 0(2N)
# SC = 0(N)

# Approach2 - using swapping

def reverseDoublyLLPointers(head):
    
    if head is None or head.next is None:
        return head  # Return head directly, not None
    
    temp = None
    current = head
    
    # Swap next and back pointers for all nodes
    while current is not None:
        temp = current.back  # Store the back node
        current.back = current.next  # Swap next and back
        current.next = temp  # Move next pointer to the previous one (stored in temp)
        current = current.back  # Move to the next node in the original list (which is current.back now)
    
    # After the loop, temp will be pointing to the second-to-last node.
    # The new head is stored in temp.back (which is the original tail).
    if temp is not None:
        head = temp.back  # Update head to the new head (which is the original tail)
    
    return head

# Reversing the linked list using swapping
head = reverseDoublyLLPointers(head)
print("Doubly linked list after reverse:")
printDoublyLL(head)

# TC = 0(N)
# SC = 0(1)
