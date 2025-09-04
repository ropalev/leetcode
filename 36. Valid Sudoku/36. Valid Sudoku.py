class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j]) - 1
                    box_idx = (i//3) * 3 + (j//3)
                    if rows[i][num] or cols[j][num] or boxes[box_idx][num]:
                        return False
                    rows[i][num] = True
                    cols[j][num] = True
                    boxes[box_idx][num]=True
        return True