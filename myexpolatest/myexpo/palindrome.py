class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        for i in range(0,len(x)):
            print("i",i)
            if x[i]!=x[len(x)-i-1]:
                return False
           
        return True   
    
obj=Solution()
result=obj.isPalindrome("madam")
print(result)