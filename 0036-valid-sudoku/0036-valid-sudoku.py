from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        gridMap = defaultdict(list)
        
        # check for first and second rules
        # 1- each row must contain the digits 1-9 with out repetition
        # 2- each column must contain the digits 1-9 with out repetition
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c].isdigit():
                    if board[r][c] not in gridMap["row_" + str(r)] and board[r][c] not in   gridMap["column_" + str(c)]:
                        gridMap["row_" + str(r)].append(board[r][c])
                        gridMap["column_" + str(c)].append(board[r][c])
                    else:
                        return False
        
        subgridMap = defaultdict(list)
        
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c].isdigit():
                    if board[r][c] not in subgridMap["subgrid_(" + str(r // 3) + " , " + str(c // 3) + ")"]:
                        subgridMap["subgrid_(" + str(r // 3) + " , " + str(c // 3) + ")"].append(board[r][c])
                    else:
                        return False
        return True