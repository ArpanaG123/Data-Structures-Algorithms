# Asteroid Collision
# Link - https://leetcode.com/problems/asteroid-collision/description/

# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

def asteroidCollision(arr):
    n = len(arr)
    st = []
    
    for i in range(n):
        if arr[i] > 0:
            st.append(arr[i])
        else:
            while len(st) != 0 and st[-1] > 0:
                if st[-1] < abs(arr[i]):
                    st.pop()
                elif st[-1] == abs(arr[i]):
                    st.pop()
                    break
                else:
                    break
            else:
                st.append(arr[i])
    return st
    
arr = [8,-8] 
result = asteroidCollision(arr)
print(result)

# TC = 0(2N)
# sc = 0(N)