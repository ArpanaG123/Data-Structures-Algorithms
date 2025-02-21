# Linked list insertion

class Node:
    def __init__(self,data):
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
        print(temp.data,end="->")
        temp = temp.next
    print(None)
    
print("original linked list is:")
printLinkedList(head)


# 1.Insert at head of linked list
def insertAtHeadLL(head,val):
    temp_head = Node(val)
    temp_head.next = head
    return temp_head
    
head = insertAtHeadLL(head,1)
print("Linked list after inserting new head:")
printLinkedList(head)

# 2.Insert at tail of linked list
def insertAtTailLL(head,val):
    if head is None:
        return Node(val)
    
    temp = head
    while temp.next is not None:
        temp = temp.next
    
    newNode = Node(val)
    temp.next = newNode
    return head
    
head = head = insertAtTailLL(head,14)
print("Linked list after inserting at tail:")
printLinkedList(head)

# 3.Insert at specific position of LL
def insertAtKthPositionLL(head,val,idx):
    if head is None:
        return Node(val)
    
    if idx == 1:
        newHead = Node(val)
        newHead.next = head
        return newHead
    
    cnt = 1
    temp = head
    
    while temp is not None:
        cnt += 1
        temp = temp.next

        if cnt == idx-1:
            newNode = Node(val)
            newNode.next = temp.next
            temp.next = newNode
    
    return head
    
head = insertAtKthPositionLL(head,6,4)
print("Linked list after inserting at given position:")
printLinkedList(head)

# 4.Insert a node before the first occurrence of a given value
def insertValueInLL(head, new_val, before_val):
    # If the list is empty, return a new node with new_val
    if head is None:
        return Node(new_val)
    
    # If the first node's data matches before_val, insert new_val before it
    if head.data == before_val:
        new_head = Node(new_val)
        new_head.next = head
        return new_head

    # Traverse the list to find the node just before before_val
    temp = head
    while temp.next is not None and temp.next.data != before_val:
        temp = temp.next

    # If we find before_val, insert the new node
    if temp.next is not None:
        newNode = Node(new_val)
        newNode.next = temp.next
        temp.next = newNode

    return head


head = insertValueInLL(head, 9, 10)
print("Linked list after inserting before the given value:")
printLinkedList(head)
