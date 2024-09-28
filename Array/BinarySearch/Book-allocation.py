# Allocate Books
# Given an array ‘arr’ of integer numbers, ‘arr[i]’ represents the number of pages in the ‘i-th’ book.
# There are ‘m’ number of students, and the task is to allocate all the books to the students.

# Allocate books in such a way that:
# 1. Each student gets at least one book.
# 2. Each book should be allocated to only one student.
# 3. Book allocation should be in a contiguous manner.


# You have to allocate the book to ‘m’ students such that the maximum number of pages assigned to a student is minimum.

# If the allocation of books is not possible, return -1.

n = 4 
m = 2 
arr = [12, 34, 67, 90]
# Output: 113

# Note - book allocation,painter's partition and split array - largest sum : all question and concept are same.
# Level:hard

# Brute force/linear search

arr = [25,46,28,49,24]
m = 4

def findNumberOfStduents(arr,pages):
    n = len(arr)
    students = 1
    pagesStudents = 0
    
    for i in range(n):
        if pagesStudents + arr[i] <= pages:
            pagesStudents += arr[i]
        else:
            students += 1
            pagesStudents = arr[i]
    
    return students
            
    
def findPages(arr,m):
    low = max(arr)
    high = sum(arr)
    
    for p in range(low,high+1):
        if findNumberOfStduents(arr,p) == m:
            return p
    return -1
    
res = findPages(arr,m)
print(res)

# TC = 0((max(arr)-sum(arr))*n)
# SC = 0(1)


# Optimal approach using binary search

arr = [25,46,28,49,24]
m = 4

def findNumberOfStduents(arr,pages):
    n = len(arr)
    students = 1
    pagesStudents = 0
    
    for i in range(n):
        if pagesStudents + arr[i] <= pages:
            pagesStudents += arr[i]
        else:
            students += 1
            pagesStudents = arr[i]
    
    return students
            
    
def findPages(arr,m):
    low = max(arr)
    high = sum(arr)
    
    while low <= high:
        mid = (low+high)//2
        
        cntStudents = findNumberOfStduents(arr,mid)
        
        if cntStudents > m:
            low = mid + 1
        else:
            high = mid - 1
            
    return low
    
res = findPages(arr,m)
print(res)

# TC = 0(log(max(arr) - sum(arr)) * 0(N))
# sc = 0(1)