# Insertion in doubly linked list

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


def insert_before_head(head, val):
    new_head = Node(val)
    
    if head is not None:  # List is not empty
        new_head.next = head
        head.back = new_head
    return new_head

head = insert_before_head(head, 11)
print("Doubly linked list after inserting new head before current head:")
printDoublyLL(head)

def insert_after_head(head, val):
    new_node = Node(val)
    if head is None:  # List is empty
        return new_node
    new_node.next = head.next
    new_node.back = head
    if head.next is not None:
        head.next.back = new_node
    head.next = new_node
    return head

head = insert_after_head(head, 12)
print("Doubly linked list after inserting new node after head:")
printDoublyLL(head)

# Function to insert a node before the tail
def insert_before_tail(tail, val):
    new_node = Node(val)
    if tail is None:  # List is empty
        return None
    elif tail.back is None:  # There's only one element in the list
        new_node.next = tail
        tail.back = new_node
        return new_node  # This becomes the new head
    else:
        node_before_tail = tail.back
        new_node.next = tail
        new_node.back = node_before_tail
        node_before_tail.next = new_node
        tail.back = new_node
    return tail

# Inserting before the current tail
tail = insert_before_tail(tail, 6)
print("Doubly linked list after inserting a node before the tail:")
printDoublyLL(head)

# Function to insert a node after the tail
def insert_after_tail(tail, val):
    new_node = Node(val)
    if tail is None:  # List is empty
        return new_node  # This becomes the new tail
    else:
        tail.next = new_node
        new_node.back = tail
    return new_node  # New node becomes the new tail

# Inserting after the current tail
tail = insert_after_tail(tail, 7)
print("Doubly linked list after inserting a node after the tail:")
printDoublyLL(head)

# Function to insert a node at the k-th position before the current position
def insert_at_kth_position_before(head, k, val):
    if head is None or k <= 0:  # List is empty or invalid k
        return head

    new_node = Node(val)
    current = head
    count = 1

    # Traverse the list to the k-th position
    while current is not None and count < k:
        current = current.next
        count += 1

    if current is None:  # k is greater than the length of the list
        return head

    # Insert before the current node
    if current.back is None:  # If we are at the head
        new_node.next = current
        current.back = new_node
        return new_node  # New node becomes the new head
    else:
        previous_node = current.back
        new_node.next = current
        new_node.back = previous_node
        previous_node.next = new_node
        current.back = new_node
    return head
    
head = insert_at_kth_position_before(head,3,13)
print("Doubly linked list after inserting new node before kth position:")
printDoublyLL(head)

# Function to insert a node at the k-th position after the current position
def insert_at_kth_position_after(head, k, val):
    if head is None or k <= 0:  # List is empty or invalid k
        return head

    new_node = Node(val)
    current = head
    count = 1

    # Traverse the list to the k-th position
    while current is not None and count < k:
        current = current.next
        count += 1

    if current is None:  # k is greater than the length of the list
        return head

    # Insert after the current node
    if current.next is None:  # If we are at the tail
        current.next = new_node
        new_node.back = current
    else:
        next_node = current.next
        new_node.next = next_node
        new_node.back = current
        current.next = new_node
        next_node.back = new_node
    return head
    
head = insert_at_kth_position_after(head,4,14)
print("Doubly linked list after inserting new node after kth position:")
printDoublyLL(head)
