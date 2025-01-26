# Implement queue using arrays
# Link - https://www.geeksforgeeks.org/problems/implement-queue-using-array/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=implement-queue-using-array

# Queries in the Queue are of the following type:
# (i) 1 x   (a query of this type means  pushing 'x' into the queue)
# (ii) 2     (a query of this type means to pop an element from the queue and print the popped element. If the queue is empty then return -1)
# We just have to implement the functions push and pop and the driver code will handle the output.

# Examples:
# Input: Queries = 1 2 1 3 2 1 4 2
# Output: 2 3
# Explanation: For query 1 2 the queue will be {2} 1 3 the queue will be {2 3} 2   poped element will be 2 the queue will be {3} 1 4 the queue will be {3 4} 2 poped element will be 3 

class Queue:
    def __init__(self,size):
        self.size = size
        self.arr = [0] * self.size
        self.front = -1
        self.rear = -1


    def Push(self, x: int) -> None:
        if self.rear == self.size - 1:
            print("Queue overflow")
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.arr[self.rear] = x
      
    def Pop(self) -> int:
        if self.front == -1:
            print("Queue underflow")
        else:
            x = self.arr[self.front]  # Get the top element
            if self.front == self.rear:
                self.front = self.rear = -1
            self.front += 1
            return x

    def Top(self) -> int:
        if self.front == -1:
            return -1
        else:
            return self.arr[self.front]
    
    def Rear(self):
        if self.front == -1:
            return -1
        else:
            return self.arr[self.rear]


    def Size(self) -> int:
        return self.rear - self.front + 1


q = Queue(10)
q.Push(6)
q.Push(3)
q.Push(7)
print("Top of queue:",q.Top())
print("Rear of queue:",q.Rear())
print("Size of queue:",q.Size())
print("The element deleted is:",q.Pop())
print("Size of queue after deleting an element:",q.Size())
print("Top of queue after deleting an element:",q.Top())