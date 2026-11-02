class Solution(object):
    def plusOne(self, digits):
        r = ""

        for i in range(len(digits)):
            r += str(digits[i])

        value = int(r) + 1

        result = []

        for ch in str(value):
            result.append(int(ch))

        return result