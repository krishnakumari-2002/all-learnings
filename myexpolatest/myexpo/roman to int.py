class Solution(object):
    def romanToInt(self, s):
        b = 0
        d = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        i = len(s) - 1 

        while i >= 0: 
            if i > 0 and d[s[i]] > d[s[i-1]]:  
                b += (d[s[i]] - d[s[i-1]])
                i -= 2 
            else:
                b += d[s[i]]  
                i -= 1 

        return b  


obj = Solution()
result = obj.romanToInt("MCMXCIV")  
print(result)  

