# Find length of Loop
# Link - https://www.geeksforgeeks.org/problems/find-length-of-loop/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-length-of-loop

# Given the head of a linked list, determine whether the list contains a loop. If a loop is present, return the number of nodes in the loop, otherwise return 0.
# Note: 'c' is the position of the node which is the next pointer of the last node of the linkedlist. If c is 0, then there is no loop.


# Input: LinkedList: 25->14->19->33->10->21->39->90->58->45, c = 4
# Output: 7
# Explanation: The loop is from 33 to 45. So length of loop is 33->10->21->39-> 90->58->45 = 7. 
# The number 33 is connected to the last node of the linkedlist to form the loop because according to the input the 4th node from the beginning(1 based indexing) 
# will be connected to the last node for the loop.

# Approach1

class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(head):
        #Your code here
        temp = head
        cnt = 1
        visited = {}
        
        while temp is not None:
            if temp in visited:
                val = visited[temp]
                return cnt - val
            visited[temp] = cnt
            cnt += 1
            temp = temp.next
        return 0
    
# Approach2
class Solution:
    def lengthOfNode(self,slow,fast):
        cnt = 1
        fast = fast.next
        
        while slow != fast:
            cnt += 1
            fast = fast.next
        return cnt
        
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self,head):
        #Your code here
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return self.lengthOfNode(slow,fast)
                
        return 0