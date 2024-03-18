class Solution:
    def generateParent(self, s: str, n_open: int, n_close: int) -> None:
        # backtracking algorithm
        # brute force [try every possiblity and if the next step doesn't work go back                   (backtrack) to the previous step]
        # recursion
        open_brackets = '(' * n_open
        close_brackets = ')' * n_close

        if not n_open and not n_close:
            self.result.append(s)
        if s[-1] == ')':
            if open_brackets and n_close >= n_open:
                self.generateParent(s + "(", n_open - 1, n_close)
            if close_brackets:
                self.generateParent(s + ")", n_open, n_close - 1)
        elif s[-1] == "(":
            if open_brackets:
                self.generateParent(s + "(", n_open - 1, n_close)
            if close_brackets:
                self.generateParent(s + ")", n_open, n_close - 1)
                
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []
        
        # more efficien solution
        def backtrack(n_open:int, n_close):
            if n_open == n_close == n:
                result.append("".join(stack))
                return 
            if n_open < n:
                stack.append('(')
                backtrack(n_open + 1, n_close)
                stack.pop()
            if n_close < n_open:
                stack.append(')')
                backtrack(n_open, n_close + 1)
                stack.pop()
                
        backtrack(0, 0)
        return result