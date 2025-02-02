# Maximal Rectangle
# Link - https://leetcode.com/problems/maximal-rectangle/description/

# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.

class Solution:
    def previousSmallerElement(self,arr):
        n = len(arr)
        st = []
        pse = [-1] * n

        for i in range(n):
            while len(st) != 0 and arr[st[-1]] >= arr[i]:
                st.pop()
            if len(st) == 0:
                pse[i] = -1
            else:
                pse[i] = st[-1]
            st.append(i)
        return pse
    
    def nextSmallerElement(self,arr):
        n = len(arr)
        st = []
        nse = [n] * n

        for i in range(n):
            while len(st) != 0 and arr[st[-1]] > arr[i]:
                nse[st.pop()] = i
            st.append(i)
        return nse

    def largestRectangleArea(self, arr):
        n = len(arr)

        pse = self.previousSmallerElement(arr)
        nse = self.nextSmallerElement(arr)

        max_area = 0

        for i in range(n):
            width = nse[i] - pse[i] - 1
            area = arr[i] * width
            max_area = max(area,max_area)
        return max_area

    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        # Initialize height array
        heights = [0] * cols
        ans = 0

        # Iterate over each row in the matrix
        for r in range(rows):
            for c in range(cols):
                # If the current cell is '1', increase the height for that column, else reset to 0
                heights[c] = heights[c] + 1 if matrix[r][c] == '1' else 0
            
            # Find the largest rectangle in the histogram for the current row
            ans = max(ans, self.largestRectangleArea(heights))
        
        return ans

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]   
# result = maximalRectangle(matrix)
# print(result)

        