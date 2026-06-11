arr = [1, 2, 4, 5]
n=max(arr)
m=[]
for i in range(1,n+1):
    if i not in arr:
        m.append(i)
print(*m)

#that * unpack the list and give the number only