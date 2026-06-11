class Solution(object):
    def strStr(self, haystack, needle):
        indices = []
        for i in range(len(haystack) - len(needle) + 1):
            print("iiiiii",i)
            print("len",len(needle))
            print("haystack[i:i+len(needle)]",haystack[i:i+len(needle)])
            if haystack[i:i+len(needle)] == needle:
                print("___----append")
                indices.append(i)
        return indices

obj = Solution()
haystack = "hello world hello"  
needle = "hello"               
result = obj.strStr(haystack, needle)
print("ans", result)
