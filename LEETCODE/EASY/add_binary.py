class Solution(object):
    def addBinary(self, a, b):
        x = int(a, 2)
        y = int(b, 2)
        z=x+y
        value=bin(z)[2:]
        return value