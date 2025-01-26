# Implement stack using queue
# Link - https://leetcode.com/problems/implement-stack-using-queues/description/

# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.

# Notes:
# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

# Example 1:
# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

class Stack:
    def __init__(self):
        self.queue = []

    def Push(self, x: int) -> None:
        self.queue.append(x)
        
        if len(self.queue) <= 1:
            return self.queue
        
        n = len(self.queue)
        
        for _ in range(0,n-1):
            store = self.queue[0]
            self.queue.pop(0)
            self.queue.append(store)
      
    def Pop(self) -> int:
        if not self.queue:
            return -1
        return self.queue.pop(0)

    def Top(self) -> int:
        if not self.queue:
            return -1
        return self.queue[0]
        
    def empty(self) -> bool:
        return not self.queue

    def Size(self) -> int:
        return len(self.queue)

s = Stack()
s.Push(6)
s.Push(3)
s.Push(7)
print("Top of stack:",s.Top())
print("Size of stack:",s.Size())
print("The element deleted is:",s.Pop())
print("Size of stack after deleting an element:",s.Size())
print("Top of stack after deleting an element:",s.Top())