class Solution:
    def isValid(self, s: str) -> bool:
        matchingBracks = {')':'(', '}':'{', ']':"["}
        openingBracks = "({["
        stack = []
        valid = True
        for char in s: 
            if char in openingBracks:
                stack.append(char)
            else: #char is a closing
                if stack != [] and matchingBracks[char] == stack[-1]:
                    stack.pop()
                else:
                    valid = False
        if stack != []:
            valid = False
            
        return valid