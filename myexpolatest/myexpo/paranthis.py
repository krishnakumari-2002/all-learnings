def is_valid_parentheses(s):
    stack=[]
    matching = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            print("1",char)
            stack.append(char)  
        elif char in ')]}':
            print("2",char)
            if not stack or stack[-1] != matching[char]:
                return False    
            stack.pop() 
    return len(stack) == 0  
        


obj = is_valid_parentheses("()[]{}")  

if obj:
    print("True")
else:
    print("False")
