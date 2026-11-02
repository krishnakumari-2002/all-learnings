class Solution(object):
    def lengthOfLastWord(self, s):
        words=s.split()
        k=words[-1]
        return len(k)
