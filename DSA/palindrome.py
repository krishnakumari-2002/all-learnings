def palindrome(s):
    for i in s:
        return s==s[::-1]
    
s="level"
obj=palindrome(s)
print(obj)


-------------------------------------------------------------------------------------


def palindrome(s):
    left=0
    right=len(s)-1
    
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True
        
s="level"
obj=palindrome(s)
print(obj)