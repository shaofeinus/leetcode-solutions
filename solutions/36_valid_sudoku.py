class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def get_box_set_i(row, col):
            return row // 3 * 3 + col // 3

        col_sets, row_sets, box_sets = [[set() for i in range(9)] for j in range(3)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if not val == '.':
                    val = int(val)
                    box_set_i = get_box_set_i(row, col)
                    if val in col_sets[col] or val in row_sets[row] or val in box_sets[box_set_i]:
                        return False
                    col_sets[col].add(val)
                    row_sets[row].add(val)
                    box_sets[box_set_i].add(val)

        return True


print(Solution().isValidSudoku(
    [
        [".", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        ["3", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
))
