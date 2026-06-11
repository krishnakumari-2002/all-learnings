arr = [0, 1, 0, 6, 0, 3]
 
k = 0  # position for next non-zero element
 
# Move non-zero elements forward
for i in range(len(arr)):
    if arr[i] != 0:
        arr[k] = arr[i]
        k += 1
 
# Fill remaining positions with zero
for i in range(k, len(arr)):
    arr[i] = 0
print(arr)