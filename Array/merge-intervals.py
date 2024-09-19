#  Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Link - https://leetcode.com/problems/merge-intervals/description/

intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Brute force

def merge_intervals(intervals):

    if not intervals:
        return []

    # Sort intervals based on the start time
    intervals.sort()
    
    n = len(intervals)
    ans = []
    
    # Iterate through intervals to merge overlapping ones
    for i in range(n):
        start = intervals[i][0]
        end = intervals[i][1]
        
        # Extend the current interval by checking subsequent intervals
        for j in range(i + 1, n):
            if intervals[j][0] <= end:  # Overlapping intervals found
                end = max(end, intervals[j][1])
            else:
                break
        
        # initially ans is empty so add first avalable interval and current interval does not overlap with the last interval.
        if not ans or ans[-1][1] < start:
            ans.append([start, end])
    
    return ans

intervals = [[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]
result = merge_intervals(intervals)
print(result)

# TC = 0(nlogn + n^2)
# sc = 0(n) = to store the ans

# Optimal approach
def merge_intervals(intervals):
    
    if not intervals:
        return []

    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])
    
    n = len(intervals)
    ans = []
    
    # Iterate through intervals to merge overlapping ones
    for i in range(n):
        # If ans is empty or the current interval does not overlap with the last added interval
        if not ans or intervals[i][0] > ans[-1][1]:
            ans.append(intervals[i])
        else:
            # There is an overlap, so merge the intervals by updating the end time
            ans[-1][0] = min(ans[-1][0], intervals[i][0])
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
        
    return ans

# Test case
intervals = [[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]
result = merge_intervals(intervals)
print(result)  # Expected Output: [[1, 6], [8, 11], [15, 18]]

# TC = 0(n + nlogn)
# sc = 0(1) + 0(n) = to return the ans