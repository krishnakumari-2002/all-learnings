arr = [1, 2, 2, 3, 3, 3, 4,4,4,4,4]
dic_value={}
for i in arr:
    dic_value[i]=dic_value.get(i,0)+1
result=max(dic_value,key=dic_value.get)
print(result)