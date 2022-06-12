from typing import List


class Solution:
    def __init__(self) -> None:
        self.blanks = []
        self.res = []

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        sudokusets = {
            "rows": [set() for _ in range(9)],
            "cols": [set() for _ in range(9)],
            "grids": [set() for _ in range(9)],
        }

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    self.blanks.append((r, c))
                else:
                    sudokusets["rows"][r].add(board[r][c])
                    sudokusets["cols"][c].add(board[r][c])

                    g = self.rctog(r, c)

                    # print(r, c, g)

                    sudokusets["grids"][g].add(board[r][c])

        # print("#blanks {}".format(len(self.blanks)))

        self.bt([], sudokusets)

        for i, d in enumerate(self.res):

            r, c = self.blanks[i]

            board[r][c] = str(d)

    def bt(self, solution, sudokusets):

        if len(self.res) >= len(self.blanks):
            return

        if len(solution) == len(self.blanks):
            self.res = solution[:]
            return
        # print(solution)
        for digit in map(str, range(1, 10)):

            r, c = self.blanks[len(solution)]
            g = self.rctog(r, c)

            solution.append(digit)

            if self.isValid(sudokusets, digit, r, c, g):

                sudokusets["rows"][r].add(digit)
                sudokusets["cols"][c].add(digit)
                sudokusets["grids"][g].add(digit)

                self.bt(solution, sudokusets)

                sudokusets["rows"][r].remove(digit)
                sudokusets["cols"][c].remove(digit)
                sudokusets["grids"][g].remove(digit)

            solution.pop()

    def isValid(self, sudokusets, digit, row, col, grid):

        if digit in sudokusets["rows"][row]:
            return False

        if digit in sudokusets["cols"][col]:
            return False

        if digit in sudokusets["grids"][grid]:
            return False

        return True

    def rctog(self, r, c):

        return (r // 3) * 3 + c // 3

    def printsets(self, asets):

        for i in range(9):

            print(sorted(list(asets[i])))

        print("")


if __name__ == "__main__":

    s = Solution()

    sudoku = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    s.solveSudoku(sudoku)

    for sudoku_row in sudoku:
        print(sudoku_row)
