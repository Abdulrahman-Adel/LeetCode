class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char.lstrip('-').isdigit():
                stack.append(char)
            else:
                value_1 = stack.pop()
                value_2 = stack.pop()
                stack.append(int(eval(str(value_2) + char + str(value_1))))
        return int(stack.pop())