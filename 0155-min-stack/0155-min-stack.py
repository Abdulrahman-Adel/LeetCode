class MinStack:

    def __init__(self):
        self.stack = []
        self.min_so_far = float(inf)
    def push(self, val: int) -> None:
        if self.stack:
            self.min_so_far = self.stack[-1][1]
        if not self.stack:
            self.min_so_far = val
        elif val < self.min_so_far:
            self.min_so_far = val
        self.stack.append([val, self.min_so_far])
    def pop(self) -> None:
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1][0]
    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()