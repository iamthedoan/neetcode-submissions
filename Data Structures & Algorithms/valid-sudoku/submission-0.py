class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def valid_group(group):
            x = [x for x in group if x != "."]
            return len(x) == len(set(x)) and all(1 <= int(i) <= 9 for i in x)

        for r in range(9):
            if not valid_group(board[r]):
                return False

        for c in range(9):
            col = [board[r][c] for r in range(9)]
            if not valid_group(col):
                return False

        for box_r in range(0, 9, 3):
            for box_c in range(0, 9, 3):
                box = []
                for r in range(box_r, box_r + 3):
                    for c in range(box_c, box_c + 3):
                        box.append(board[r][c])
                if not valid_group(box):
                    return False

        return True


