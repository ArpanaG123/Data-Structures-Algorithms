# Linked List Cycle
# Link - https://leetcode.com/problems/linked-list-cycle/description/

# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).


# Approach1
def hasCycle(head):
    visited = {}
    temp = head

    while temp is not None:
        if temp in visited:
            return True
         
        visited[temp] = True
        temp = temp.next
    return False

head = 4
hasCycle(head)

# TC = 0(N * 2(logN)) - as using map DS
# SC = 0(N)

# Approach2
# using tortoise and hare algorithm

def hasCycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
                
    return False

head = 4
hasCycle(head)

# TC = 0(N)
# SC = 0(1)


        
