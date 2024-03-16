class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        brackets = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        
        stack = []
        for char in s:
            # if closing bracket
            if char in brackets:
                if not (stack and brackets[char] == stack.pop()):
                    return False
            else:
                stack.append(char)
        return len(stack) == 0