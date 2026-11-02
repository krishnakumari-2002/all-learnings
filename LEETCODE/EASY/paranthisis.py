class Solution(object):
    def isValid(self, s):
        stack=[]
        match={')':'(',']':'[','}':'{'}
        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ']})':
                if not stack or stack[-1] !=match[char]:
                    return False
                stack.pop()
        return len(stack)==0
        



# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false