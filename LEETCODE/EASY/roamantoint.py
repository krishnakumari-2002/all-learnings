class Solution(object):
    def romanToInt(self, s):
        b=0
        d={
            'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
        }
        i=len(s)-1
        while i>=0:
            if i>0 and d[s[i]]>d[s[i-1]]:
                b+=d[s[i]]-d[s[i-1]]
                i-=2
            else:
                b+=d[s[i]]
                i-=1
        return b


# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 