class Solution():
    def findAllOccurrences(self, haystack:str, needle):
        indices = []
        start = 0
        while start <= len(haystack) - len(needle):  #last possible starting position
            print("start",start)
            print("needle",needle)
            index = haystack.find(needle, start) #find will check the whole string of the needle will be prsent or not in the haystack then if find then give the index of that string will be notified that and that was the index of that.
                                                    
            print("index",index)
            if index == -1: #that find() method if not found that text then it automaticcaly return the -1
                break                                                                                                                                                                                                                                               
            indices.append(index)
            print("indicec",indices)  
            start = index + 1  
            print("start",start)
        return indices 

obj = Solution()
haystack = "leetcodeleete"
needle = "leet"
result = obj.findAllOccurrences(haystack, needle)
print(result)  
