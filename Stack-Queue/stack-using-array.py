# Implement stack using array
# Link - https://www.geeksforgeeks.org/problems/implement-stack-using-array/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=implement-stack-using-array

# Write a program to implement a Stack using Array. Your task is to use the class as shown in the comments in the code editor and complete the functions push() and pop() to implement a stack. The push() method takes one argument, an integer 'x' to be pushed into the stack and pop() which returns an integer present at the top and popped out from the stack. If the stack is empty then return -1 from the pop() method.
# Note: The input is given in form of queries. Since there are two operations push() and pop(), there is two types of queries as described below:
# (i) 1 x   (a query of this type means  pushing 'x' into the stack)
# (ii) 2     (a query of this type means to pop an element from the stack and print the popped element)
# Input contains separated by space and as described above. 

# Input: 1 2 1 3 2 1 4 2 
# Output: 3, 4
# Explanation: 
# push(2)    the stack will be {2}
# push(3)    the stack will be {2 3}
# pop()      poped element will be 3,
#            the stack will be {2}
# push(4)    the stack will be {2 4}
# pop()      poped element will be 4


class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        #add code here
        return self.arr.append(data)
    
    #Function to remove an item from top of the stack.
    def pop(self):
        #add code here
        if not self.arr:
            return -1
        else:
            return self.arr.pop()


# Approach1 - fixed size
class Stack:
    def __init__(self):
        self.top = -1
        self.size = 1000
        self.arr = [0] * self.size

    def push(self, x: int) -> None:
        if self.top == self.size - 1:
            print("stack overflow")
        else:
            self.top += 1
            self.arr[self.top] = x
      
    def pop(self) -> int:
        if self.top == -1:  # Check if stack is empty
            print("Stack underflow")
            return -1
        else:
            x = self.arr[self.top]  # Get the top element
            self.top -= 1  # Move the top pointer down
            return x
        
    def Top(self) -> int:
        if self.top == -1:
            return -1
        else:
            return self.arr[self.top]

    def Size(self) -> int:
        return self.top + 1

# Example usage
s = Stack()
s.push(6)
s.push(3)
s.push(7)
print("Top of stack:", s.Top())  # Output: 7
print("Size of stack:", s.Size())  # Output: 3
print("The element deleted is:", s.pop())  # Output: 7
print("Size of stack after deleting an element:", s.Size())  # Output: 2
print("Top of stack after deleting an element:", s.Top())  # Output: 3


# Approach2 - using dynamic size

class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty list to represent the stack

    # Push operation
    def push(self, x: int) -> None:
        self.stack.append(x)

    # Pop operation
    def pop(self) -> int:
        if not self.stack:
            print("Stack underflow")
            return -1
        return self.stack.pop()

    # Peek at the top element
    def Top(self) -> int:
        if not self.stack:
            print("Stack is empty")
            return -1
        return self.stack[-1]

    # Get current size of the stack
    def Size(self) -> int:
        return len(self.stack)

    # Check if the stack is empty
    def is_empty(self) -> bool:
        return len(self.stack) == 0


# Example usage
s = Stack()
s.push(6)
s.push(3)
s.push(7)
print("Top of stack:", s.Top())  # Output: 7
print("Size of stack:", s.Size())  # Output: 3
print("The element deleted is:", s.pop())  # Output: 7
print("Size of stack after deleting an element:", s.Size())  # Output: 2
print("Top of stack after deleting an element:", s.Top())  # Output: 3
