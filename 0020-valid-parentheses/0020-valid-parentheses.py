class Solution:
    def isValid(self, s: str) -> bool:
        open_parent = "([{"
        close_parent = ")]}"
        
        stack = list()
        counter = 0
        for char in s:
            if char in open_parent:
                stack.append(char)
            else:
                if not stack:
                    return False
                opens = stack.pop()
                close_idx = close_parent.index(char)
                if open_parent[close_idx] != opens:
                    return False
                counter += 2
        return counter == len(s)