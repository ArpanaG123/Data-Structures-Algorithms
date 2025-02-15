# Define class node
class Node:
    def __init__(self,data): #constructor method initialization
        self.data = data
        self.next = None
        
        
arr = [1, 2, 3, 4, 5]
y = Node(arr[0]) # Creating new node instance
print(y) # print memory location
print(y.data) # print actual value stored in node at position 0
x = Node(8)      
print(x.data)

# Define class node
class Node:
    def __init__(self,data): #constructor method initialization
        self.data = data
        self.next = None
        
# Returning head of the linked list from array
def convertArrToLinkedList(arr):
    n = len(arr)
    head = Node(arr[0])
    mover = head
    
    for i in range(1,n):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp
    return head
    
arr = [1, 2, 3, 4, 5]
linked_list_head = convertArrToLinkedList(arr)
print(linked_list_head.data)

# Array to LinkedList-----
# Define class node
class Node:
    def __init__(self,data): #constructor method initialization
        self.data = data
        self.next = None
        
# Returning head of the linked list from array
def convertArrToLinkedList(arr):
    n = len(arr)
    head = Node(arr[0])
    mover = head
    
    for i in range(1,n):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp
    return head
    
arr = [1, 2, 3, 4, 5]
# Priniting head of linked list
linked_list_head = convertArrToLinkedList(arr)
print(linked_list_head.data)

def printLinkedList(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Print the linked list
printLinkedList(linked_list_head)

# To print length of the linked list
def printLengthOfLinkedList(head):
    current = head
    count = 0
    while current is not None:
        count += 1  # Increment the count for each node
        current = current.next
    return count

print("Length of the linked list:", printLengthOfLinkedList(linked_list_head))

# Function to search for an element in the linked list
def searchLinkedList(head, target):
    current = head
    while current is not None:
        if current.data == target:
            return True  # Element found
        current = current.next
    return False  # Element not found
    
# Search for an element in the linked list
target = 3
if searchLinkedList(linked_list_head, target):
    print(f"Element {target} found in the linked list.")
else:
    print(f"Element {target} not found in the linked list.")
