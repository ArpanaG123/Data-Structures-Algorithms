# count sort

# When to Use Counting Sort:
# When the range of input values is small relative to the number of elements.
# When sorting integers or categorical data.

arr = [4, 2, 2, 8, 3, 3, 1]
n = len(arr)
mx = max(arr)

freq = [0]*(mx+1)

for i in range(0,n):
    freq[arr[i]] += 1

sorted_arr = []
for i in range(0,mx):
    for _ in range(freq[i]):
        sorted_arr.append(i)
print(sorted_arr)