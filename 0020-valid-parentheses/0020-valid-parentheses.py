class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        brackets = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        
        stack = [] # O(n) SPACE 
        for char in s: # O(n) TIME 
            # if closing bracket
            if char in brackets: # O(3)
                # check whether the stack is empty and the closing bracket matches the latest                     open bracket in the stack
                if not (stack and brackets[char] == stack.pop()):
                    return False
            else:
                # if the character is open bracket append it to the stack
                stack.append(char)
        
        # the time complexity is O(n) space complixity O(n)
        # check if the stack is empty
        return len(stack) == 0