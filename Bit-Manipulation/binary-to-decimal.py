# Binary to decimal conversion 

s = "10010"

n = len(s)
sm = 0
power = 1

for i in range(n-1,-1,-1):
    if s[i] == "1":
        sm = sm + power
    power = power * 2

print("Decimal of given binary is:",sm)

# TC = 0(nlogn)
# SC = 0(1)