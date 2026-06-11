arr = [2, 7, 11, 15,3,6]
target = 9
result=set()
for i in arr:
    value=target-i
    if value in result:
        print([value,i])
    result.add(i)


