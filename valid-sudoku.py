"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # loop through rows
        for row in board:
            numbers = [k for k in row if k.isnumeric()]
            unique_numbers = set(numbers)
            if len(numbers) != len(unique_numbers):
                return False

        # loop through columns
        rows = [row for row in board]
        columns = zip(*rows)
        for column in columns:
            numbers = [k for k in column if k.isnumeric()]
            unique_numbers = set(numbers)
            if len(numbers) != len(unique_numbers):
                return False

        # loop through squares 3x3
        row_index = 0
        while row_index < len(board):

            items = board[row_index:row_index+3]
            for i in range(0, 9, 3):
                sub_squares = items[0][i:i+3] + items[1][i:i+3] + items[2][i:i+3]
                numbers = [k for k in sub_squares if k.isnumeric()]
                unique_numbers = set(numbers)
                if len(numbers) != len(unique_numbers):
                    return False
            row_index += 3

        return True


s = Solution()
res = s.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                       ["6",".",".","1","9","5",".",".","."],
                       [".","9","8",".",".",".",".","6","."],
                       ["8",".",".",".","6",".",".",".","3"],
                        ["4",".",".","8",".","3",".",".","1"],
                        ["7",".",".",".","2",".",".",".","6"],
                       [".","6",".",".",".",".","2","8","."],
                       [".",".",".","4","1","9",".",".","5"],
                       [".",".",".",".","8",".",".","7","9"]])
print(res)
