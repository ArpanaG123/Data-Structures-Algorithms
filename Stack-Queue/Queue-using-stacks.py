# Implement Queue using Stacks
# Link - https://leetcode.com/problems/implement-queue-using-stacks/description/

# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
# Implement the MyQueue class:
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.

# Notes:
# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

# Input:["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output:[null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false


class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def Push(self,x):
        while len(self.s1):
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        
        while len(self.s2):
            self.s1.append(self.s2.pop())
    
    def Pop(self):
        if not self.s1:
            return -1
        return self.s1.pop()
        
    def Top(self):
        if not self.s1:
            return -1
        return self.s1[-1]
        
    def empty(self):
        return not self.s1 and not self.s2
        
    def Size(self):
        return len(self.s1)
        

q = Queue()
q.Push(4)
q.Push(2)
q.Push(3)
q.Push(5)
print("Top element of queue:",q.Top())
print("The element deleted is:",q.Pop())
print("The element deleted is:",q.Pop())
q.Push(6)
print("Top element of queue:",q.Top())
print("Size of queue:",q.Size())      