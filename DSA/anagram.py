def anagram(s1,s2):
    s3={}
    s4={}
    for i in s1:
        if i in s3:
            s3[i]+=1
        else:
            s3[i]=1
    for j in s2:
        if j in s4:
            s4[j]+=1
        else:
            s4[j]=1
    if s3==s4:
        return True
    else:
        return False
        
        
        
s1 = "listen"
s2 = "silent"
obj=anagram(s1,s2)
print(obj)

--------------------------------------------------------------------------------------------
def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    freq={}
    for i in s1:
        freq[i]=freq.get(i,0)+1
    for i in s2:
        if i not in freq:
            return False
        freq[i]-=1
    for value in freq.values():
        if value!=0:
            return False
    return True
        
        
s1 = "listen"
s2 = "silent"
obj=anagram(s1,s2)
print(obj)