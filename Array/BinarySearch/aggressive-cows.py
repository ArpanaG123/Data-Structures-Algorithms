# Aggressive cows
# Farmer John has built a new long barn, with N (2 <= N <= 100,000) stalls. The stalls are located along a straight line at positions x1 ... xN (0 <= xi <= 1,000,000,000).

# His C (2 <= C <= N) cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, FJ wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?

# Input
# t – the number of test cases, then t test cases follows.
# * Line 1: Two space-separated integers: N and C
# * Lines 2..N+1: Line i+1 contains an integer stall location, xi

# Output
# For each test case output one integer: the largest minimum distance.

# Link - https://www.spoj.com/problems/AGGRCOW/

# examples
arr = [0,3,4,7,10,9]
cows = 4

stalls = [0,3,4,7,10,9]
k = 4

def canWePlace(stalls,dist,cows) ->bool:
    n = len(stalls)
    cowsCnt = 1
    last = stalls[0]
    
    for i in range(1,n):
        if stalls[i] - last >= dist:
            cowsCnt += 1
            last = stalls[i]
    
    if cowsCnt >= cows:
        return True
    return False
    
def aggressivecows(stalls,k):
    n = len(stalls)
    
    stalls.sort()
    
    low = 1
    high = stalls[n-1] - stalls[0]
    
    while low <= high:
        mid = (low+high)//2
        
        if canWePlace(stalls,mid,k):
            low = mid + 1
        else:
            high = mid - 1
    return high
    
res = aggressivecows(stalls,k)
print(res)

# TC = 0(n* max(stalls[]-min(stalls))) + o(nlogn)
# SC = 0(1)