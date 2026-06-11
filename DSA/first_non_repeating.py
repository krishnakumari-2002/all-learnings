s = "aabbcdde"
result={}
output=[]
for i in s:
    if i in result:
        result[i]+=1
    else:
        result[i]=1
for key,value in result.items():
    if value==1:
        output.append(key)
        break
        
print(output)



-----------------------------------------------------------------------

s = "aabbcdde"
result={}
for i in s:
    result[i]=result.get(i,0)+1
ans=None
for i in s:
    if result[i]==1:
        ans=i
        break;
print(ans)
