class Solution(object):
    def longestCommonPrefix(self, strs):
        a=""
        length=[]
        for i in strs:
            length.append(len(i))
        min_value=min(length)
        for i in range(min_value):
            first=strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i]!=first:
                    return a
            a+=first
        return a


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.