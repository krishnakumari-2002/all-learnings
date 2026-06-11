arr = [1, 7, 0, 3, 12, 0, 12,0]
pos=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[pos],arr[i]=arr[i],arr[pos]
        pos+=1
print(arr)