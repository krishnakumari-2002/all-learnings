class Solution(object):
    def longestCommonPrefix(self, strs):
        a=''
        lengths = [] 
        for i in strs:
            lengths.append(len(i))  

        min_value = min(lengths)  
        for i in range(min_value):
            first=strs[0][i] #-------->firts word first character in 0th index(flower)
            for j in range(1,len(strs)): #--------->second word  first character in 0th position(flow)
                if strs[j][i]!=first: #match the first word firts character and the second
                    return a
            a+=first            
        return a
                
obj=Solution()
strs = ["flower","flow","flight"]
result=obj.longestCommonPrefix(strs)
print("count",result)