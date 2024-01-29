class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = tokens[:2]
        for token in tokens[2:]:
            if token.strip('-').isnumeric():
                num_stack.append(token)
            else:
                n1, n2 = num_stack.pop(),  num_stack.pop()
                res = int(eval(n2 + token + n1))
                print(f"{n2} {token} {n1} = {res}")
                num_stack.append(str(res))
        return int(num_stack.pop())