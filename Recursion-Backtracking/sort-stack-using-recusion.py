# sort a stack using recusion

def sort_stack(st):
    n = len(st)
    
    # Helper function that sorts the stack
    def helper(st):
        # Base case: A stack with one or zero elements is already sorted
        if n == 1:
            return
        
        #Remove the top element and recursively sort the remaining
        if st:
            top_element = st.pop()
            helper(st)
            # Insert the last element into the sorted portion of the array
            insert(st, top_element)
    
    # Helper function to insert an element in its correct position in a sorted order
    def insert(st, value):
        # If the stack is empty or value is greater than the last element, append it
        if not st or value >= st[-1]:
            st.append(value)
        else:
            # Recursively remove the top element, insert value, then put the last element back
            top = st.pop()
            insert(st, value)
            st.append(top)
    
    # Start the recursive sorting process
    helper(st)
    return st

# Example usage:
st = [3, 1, 4, 1, 5]
sorted_stack = sort_stack(st)
print(sorted_stack)