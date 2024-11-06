# Pseudocode for backtracking algortihm to implement the Sudoku solver

# Pseudostructure for backtracking from https://en.wikipedia.org/wiki/Backtracking
from typing import Any, List, Tuple, Protocol


class Backtracking(Protocol):

    def accept(self) -> bool: ...

    def reject(self, value: Any, location: Tuple[int, int]) -> bool: ...

    def next(self, value: Any, location: Tuple[int, int]): ...

    def reset(self, location: Tuple[int, int]): ...

    def get_next_location(self) -> Tuple[int, int]: ...

    def possible_values(self, location: Tuple[int, int]) -> List: ...

    def output(self) -> Any: ...


class SudokuSolver:

    def __init__(self, data: str | List[List[int]]):
        if isinstance(data, str):
            self.board = self._to_board(data)
        else:
            self.board = data
        self.zeros = self._get_zeros()

    def _get_zeros(self) -> List[Tuple[int, int]]:
        return [(i, j) for i in range(9) for j in range(9) if self.board[i][j] == 0]

    @staticmethod
    def _to_board(data: str) -> List[List[int]]:
        """Returns a list of integers. Input format is a string with
        newlines. For a valid sudoku board, it expects 9 lines
        with 9 values. A zero marks an non-filled field.. Example:
        080402060
        034000910
        960000084
        000216000
        000000000
        000357000
        840000075
        026000130
        090701040
        """
        lines = data.rstrip("\n").replace(" ", "").splitlines()
        if len(lines) != 9:
            raise RuntimeError("input string does not contain 9 lines")
        for l in lines:
            if len(l) != 9:
                raise RuntimeError("input line does not contain 9 chars")
        return [[int(i) for i in line] for line in lines]

    def _get_block_indices(self, index: int):
        return list(range(index // 3 * 3, index // 3 * 3 + 3))

    def _get_values(
        self, row_index: int, col_index: int
    ) -> Tuple[List[int], List[int], List[int]]:
        col = [self.board[i][col_index] for i in range(9)]
        row = self.board[row_index]
        block = [
            self.board[i][j]
            for i in self._get_block_indices(row_index)
            for j in self._get_block_indices(col_index)
        ]
        return row, col, block

    def accept(self) -> bool:
        return sum([row.count(0) for row in self.board]) == 0

    def reject(self, value: int, location: Tuple[int, int]) -> bool:
        row, col, block = self._get_values(location[0], location[1])
        if (value in row) or (value in col) or (value in block):
            return True
        return False

    def next(self, value: int, location: Tuple[int, int]):
        self.board[location[0]][location[1]] = value

    def reset(self, location: Tuple[int, int]):
        self.board[location[0]][location[1]] = 0
        self.zeros = [location] + self.zeros

    def possible_values(self, location: Tuple[int, int]) -> List[int]:
        possible_values = [v for v in range(1, 10) if not self.reject(v, location)]
        return possible_values

    def get_next_location(self) -> Tuple[int, int]:
        location = self.zeros[0]
        self.zeros = self.zeros[1:]
        return location

    def _add_seperator(self, s: str, seperator: str) -> str:
        if len(s) != 9:
            raise RuntimeError("input line does not contain 9 chars")
        return (
            f"|{seperator}"
            + f"{seperator}".join(map(str, s[:3]))
            + f"{seperator}|{seperator}"
            + f"{seperator}".join(map(str, s[3:6]))
            + f"{seperator}|{seperator}"
            + f"{seperator}".join(map(str, s[6:9]))
            + f"{seperator}|"
            + "\n"
        )

    def __str__(self) -> str:
        board_str = "\n-----------------------\n"
        for i, v in enumerate(self.board):
            if i % 3 == 0 and i > 0 and i < 9:
                board_str += self._add_seperator("---------", "-")
            board_str += self._add_seperator("".join(map(str, v)), " ")
        board_str += "-----------------------\n"
        return board_str

    def output(self) -> List[List[int]]:
        return self.board


def solve_backtracking(problem: Backtracking) -> None | Backtracking:
    if problem.accept():
        return problem

    loc = problem.get_next_location()
    for v in problem.possible_values(loc):
        problem.next(v, loc)
        s = solve_backtracking(problem)
        if s:
            return s
    problem.reset(loc)
    return None
