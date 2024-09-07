# Power of 4

n = 64
# output = True

# Approach1
n = 4
# Output = True

if n <= 0:
    print(False)

while n % 4 == 0:
    n = n//4

if n == 1:
    print(True)
else:
    print(False)

# TC = 0(nlogn) - with base4
# SC = 0(1)

# Approach2
def is_power_of_4(n):
    if n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0:
        return True
    return False

# Test the function
n = 16  # Example
print(is_power_of_4(n))  # True, since 16 is a power of 4

