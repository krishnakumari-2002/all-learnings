arr = [1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1]

count=1
max_count=1
element=arr[0]
for i in range(1,len(arr)):
    if arr[i]==arr[i-1]:
        count+=1
    else:
        count=1
    if count>max_count:
        max_count=count
        element=arr[i]
print("element",element)
print("count",max_count)
