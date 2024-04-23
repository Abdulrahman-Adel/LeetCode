class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0]) 
        m = len(matrix)

        l = 0
        r = n * m - 1
        while(l <= r):
            m = (l + r) // 2 
            row = m // n
            col = m % n
            if target < matrix[row][col]:
                r = m - 1
            elif target > matrix[row][col]:
                l = m + 1
            else: 
                return True

        return False