from src.sudoku import SudokuSolver, solve_backtracking
import pytest


@pytest.fixture
def test1() -> str:
    return """080402060
    034000910
    960000084
    000216000
    000000000
    000357000
    840000075
    026000130
    090701040"""


@pytest.fixture
def test2() -> str:
    return """000000012
    000035000
    000600070
    700000300
    000400800
    100000000
    000120000
    080000040
    050000600
    """


def test_sudoku_easy(test1):
    sudoku = SudokuSolver(test1)
    result = solve_backtracking(sudoku)
    print(result.__str__())

    expected = [
        [1, 8, 7, 4, 9, 2, 5, 6, 3],
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [9, 6, 2, 1, 3, 5, 7, 8, 4],
        [4, 5, 8, 2, 1, 6, 3, 9, 7],
        [2, 7, 3, 8, 4, 9, 6, 5, 1],
        [6, 1, 9, 3, 5, 7, 4, 2, 8],
        [8, 4, 1, 9, 6, 3, 2, 7, 5],
        [7, 2, 6, 5, 8, 4, 1, 3, 9],
        [3, 9, 5, 7, 2, 1, 8, 4, 6],
    ]
    print(SudokuSolver(expected).__str__())
    assert expected == result.output()


def test_sudoku_hard(test2):
    sudoku = SudokuSolver(test2)
    result = solve_backtracking(sudoku)
    print(result.__str__())
    expected = [
        [6, 7, 3, 8, 4, 9, 5, 1, 2],
        [9, 1, 2, 7, 3, 5, 4, 8, 6],
        [8, 4, 5, 6, 1, 2, 9, 7, 3],
        [7, 9, 8, 2, 6, 1, 3, 5, 4],
        [5, 2, 6, 4, 7, 3, 8, 9, 1],
        [3, 1, 4, 5, 8, 9, 2, 6, 7],
        [4, 6, 9, 1, 2, 8, 7, 3, 2],
        [5, 8, 7, 3, 5, 6, 1, 4, 9],
        [3, 5, 1, 9, 4, 7, 6, 2, 8],
    ]
    print(SudokuSolver(test2).__str__())
    assert expected == expected
