class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            s = set()
            for j in range(len(board[0])):
                if board[i][j]!="." :
                    if board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j])
        for i in range(len(board[0])):
            s = set()
            for j in range(len(board)):
                if board[j][i]!="." :
                    if board[j][i] in s:
                        return False
                    else:
                        s.add(board[j][i])

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                s = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        if val != ".":
                            if val in s:
                                return False
                            s.add(val)
        return True
                    

