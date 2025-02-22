# Doubly linked-list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None

def convertArrToDoublyLL(arr):
    if not arr:  # If the array is empty, return None
        return None
    
    # Initialize the head of the list
    head = Node(arr[0])
    prev = head  # This will keep track of the previous node

    # Iterate through the rest of the array and link nodes
    for i in range(1, len(arr)):
        # Create a new node with the current array element
        temp = Node(arr[i])
        temp.back = prev  # Link the new node's back to the previous node
        prev.next = temp  # Link the previous node's next to the new node
        prev = temp  # Move the previous node pointer forward

    return head  # Return the head of the doubly linked list

# Example usage
arr = [1, 2, 3, 4, 5]
head = convertArrToDoublyLL(arr)

# Print linked list
def printDoublyLL(head):
    temp = head
    while temp is not None:
        print(temp.data, end="<->")
        temp = temp.next
    print(None)

print("Doubly linked list is:")
printDoublyLL(head)