class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize an empty stack to store intermediate results.
        stack = []

        # Iterate through each token in the RPN expression.
        for token in tokens:
            # Check if the token is an addition operator.
            if token == '+':
                # Pop the top two elements from the stack.
                a, b = stack.pop(), stack.pop()
                # Perform addition and push the result back onto the stack.
                stack.append(a + b)
            # Check if the token is a subtraction operator.
            elif token == '-':
                # Pop the top two elements from the stack.
                a, b = stack.pop(), stack.pop()
                # Perform subtraction and push the result back onto the stack.
                stack.append(b - a)
            # Check if the token is a multiplication operator.
            elif token == '*':
                # Pop the top two elements from the stack.
                a, b = stack.pop(), stack.pop()
                # Perform multiplication and push the result back onto the stack.
                stack.append(b * a)
            # Check if the token is a division operator.
            elif token == '/':
                # Pop the top two elements from the stack.
                a, b = stack.pop(), stack.pop()
                # Perform integer division and push the result back onto the stack.
                stack.append(int(b / a))
            else:
                # The token is an operand, so convert it to an integer and push onto the stack.
                stack.append(int(token))
                
        # The final result will be on the top of the stack.
        return stack.pop()