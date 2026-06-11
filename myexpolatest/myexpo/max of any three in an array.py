class Solution():
    def max(self,s):
        length=len(s)
        if length<3:
            print("should have three elements")
            return
        max=0
        elements = ()
        for i in range(length-2):
            for j in range(i+1,length-1):
                for k in range(j+1,length):
                    current_max=s[i]+s[j]+s[k]
                    if max<current_max:
                        max=current_max
                        elements= (s[i], s[j], s[k])
        return max,elements

        
        
obj=Solution()
s=[2,8,9,12,6,1,3,9,8,55]
max,elements=obj.max(s)
print("elements",elements)
print("max",max)

