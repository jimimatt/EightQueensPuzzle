from collections.abc import Iterator
from enum import Enum


class DiagonalLeft(Enum):
    A1H8 = [0, 9, 18, 27, 36, 45, 54, 63]
    A2G7 = [8, 17, 26, 35, 44, 53, 62]
    A3F6 = [16, 25, 34, 43, 52, 61]
    A4E5 = [24, 33, 42, 51, 60]
    A5D4 = [32, 41, 50, 59]
    A6C3 = [40, 49, 58]
    A7B2 = [48, 57]
    A8 = [56]
    B1H7 = [1, 10, 19, 28, 37, 46, 55]
    C1H6 = [2, 11, 20, 29, 38, 47]
    D1H5 = [3, 12, 21, 30, 39]
    E1H4 = [4, 13, 22, 31]
    F1H3 = [5, 14, 23]
    G1H2 = [6, 15]
    H1 = [7]


class DiagonalRight(Enum):
    A1 = [0]
    A2B1 = [1, 8]
    A3C1 = [2, 9, 16]
    A4D1 = [3, 10, 17, 24]
    A5E1 = [4, 11, 18, 25, 32]
    A6F1 = [5, 12, 19, 26, 33, 40]
    A7G1 = [6, 13, 20, 27, 34, 41, 48]
    A8H1 = [7, 14, 21, 28, 35, 42, 49, 56]
    B8H2 = [15, 22, 29, 36, 43, 50, 57]
    C8H3 = [23, 30, 37, 44, 51, 58]
    D8H4 = [31, 38, 45, 52, 59]
    E8H5 = [39, 46, 53, 60]
    F8H6 = [47, 54, 61]
    G8H7 = [55, 62]
    H8 = [63]


class ChessBoard:
    coord_diag_mapping: dict[int, tuple[DiagonalLeft, DiagonalRight]] = {
        # first row
        0: (DiagonalLeft.A1H8, DiagonalRight.A1),
        1: (DiagonalLeft.B1H7, DiagonalRight.A2B1),
        2: (DiagonalLeft.C1H6, DiagonalRight.A3C1),
        3: (DiagonalLeft.D1H5, DiagonalRight.A4D1),
        4: (DiagonalLeft.E1H4, DiagonalRight.A5E1),
        5: (DiagonalLeft.F1H3, DiagonalRight.A6F1),
        6: (DiagonalLeft.G1H2, DiagonalRight.A7G1),
        7: (DiagonalLeft.H1, DiagonalRight.A8H1),
        # second row
        8: (DiagonalLeft.A2G7, DiagonalRight.A2B1),
        9: (DiagonalLeft.A1H8, DiagonalRight.A3C1),
        10: (DiagonalLeft.B1H7, DiagonalRight.A4D1),
        11: (DiagonalLeft.C1H6, DiagonalRight.A5E1),
        12: (DiagonalLeft.D1H5, DiagonalRight.A6F1),
        13: (DiagonalLeft.E1H4, DiagonalRight.A7G1),
        14: (DiagonalLeft.F1H3, DiagonalRight.A8H1),
        15: (DiagonalLeft.G1H2, DiagonalRight.B8H2),
        # third row
        16: (DiagonalLeft.A3F6, DiagonalRight.A3C1),
        17: (DiagonalLeft.A2G7, DiagonalRight.A4D1),
        18: (DiagonalLeft.A1H8, DiagonalRight.A5E1),
        19: (DiagonalLeft.B1H7, DiagonalRight.A6F1),
        20: (DiagonalLeft.C1H6, DiagonalRight.A7G1),
        21: (DiagonalLeft.D1H5, DiagonalRight.A8H1),
        22: (DiagonalLeft.E1H4, DiagonalRight.B8H2),
        23: (DiagonalLeft.F1H3, DiagonalRight.C8H3),
        # fourth row
        24: (DiagonalLeft.A4E5, DiagonalRight.A4D1),
        25: (DiagonalLeft.A3F6, DiagonalRight.A5E1),
        26: (DiagonalLeft.A2G7, DiagonalRight.A6F1),
        27: (DiagonalLeft.A1H8, DiagonalRight.A7G1),
        28: (DiagonalLeft.B1H7, DiagonalRight.A8H1),
        29: (DiagonalLeft.C1H6, DiagonalRight.B8H2),
        30: (DiagonalLeft.D1H5, DiagonalRight.C8H3),
        31: (DiagonalLeft.E1H4, DiagonalRight.D8H4),
        # fifth row
        32: (DiagonalLeft.A5D4, DiagonalRight.A5E1),
        33: (DiagonalLeft.A4E5, DiagonalRight.A6F1),
        34: (DiagonalLeft.A3F6, DiagonalRight.A7G1),
        35: (DiagonalLeft.A2G7, DiagonalRight.A8H1),
        36: (DiagonalLeft.A1H8, DiagonalRight.B8H2),
        37: (DiagonalLeft.B1H7, DiagonalRight.C8H3),
        38: (DiagonalLeft.C1H6, DiagonalRight.D8H4),
        39: (DiagonalLeft.D1H5, DiagonalRight.E8H5),
        # sixth row
        40: (DiagonalLeft.A6C3, DiagonalRight.A6F1),
        41: (DiagonalLeft.A5D4, DiagonalRight.A7G1),
        42: (DiagonalLeft.A4E5, DiagonalRight.A8H1),
        43: (DiagonalLeft.A3F6, DiagonalRight.B8H2),
        44: (DiagonalLeft.A2G7, DiagonalRight.C8H3),
        45: (DiagonalLeft.A1H8, DiagonalRight.D8H4),
        46: (DiagonalLeft.B1H7, DiagonalRight.E8H5),
        47: (DiagonalLeft.C1H6, DiagonalRight.F8H6),
        # seventh row
        48: (DiagonalLeft.A7B2, DiagonalRight.A7G1),
        49: (DiagonalLeft.A6C3, DiagonalRight.A8H1),
        50: (DiagonalLeft.A5D4, DiagonalRight.B8H2),
        51: (DiagonalLeft.A4E5, DiagonalRight.C8H3),
        52: (DiagonalLeft.A3F6, DiagonalRight.D8H4),
        53: (DiagonalLeft.A2G7, DiagonalRight.E8H5),
        54: (DiagonalLeft.A1H8, DiagonalRight.F8H6),
        55: (DiagonalLeft.B1H7, DiagonalRight.G8H7),
        # eighth row
        56: (DiagonalLeft.A8, DiagonalRight.A8H1),
        57: (DiagonalLeft.A7B2, DiagonalRight.B8H2),
        58: (DiagonalLeft.A6C3, DiagonalRight.C8H3),
        59: (DiagonalLeft.A5D4, DiagonalRight.D8H4),
        60: (DiagonalLeft.A4E5, DiagonalRight.E8H5),
        61: (DiagonalLeft.A3F6, DiagonalRight.F8H6),
        62: (DiagonalLeft.A2G7, DiagonalRight.G8H7),
        63: (DiagonalLeft.A1H8, DiagonalRight.H8),
    }

    row_positions: list[int] = [0, 1, 2, 3, 4, 5, 6, 7]

    solutions: list[list[int]] = []

    def __init__(self) -> None:
        self.diagonal_left: set[DiagonalLeft] = set()
        self.diagonal_right: set[DiagonalRight] = set()
        self.rows: list[int] = []

    @staticmethod
    def get_coord(row: int, col: int) -> int:
        return row * 8 + col

    def next_valid_positions(self) -> Iterator[int]:
        valid_cols = [queen_pos for queen_pos in ChessBoard.row_positions if queen_pos not in self.rows]
        positions = [ChessBoard.get_coord(len(self.rows), col) for col in valid_cols]
        positions = [pos for pos in positions if self.coord_diag_mapping[pos][0] not in self.diagonal_left]
        positions = [pos for pos in positions if self.coord_diag_mapping[pos][1] not in self.diagonal_right]
        return (pos % 8 for pos in positions)

    def push_queen(self, pos: int) -> None:
        diags = self.coord_diag_mapping[len(self.rows) * 8 + pos]
        self.diagonal_left.add(diags[0])
        self.diagonal_right.add(diags[1])
        self.rows.append(pos)

    def pop_queen(self) -> None:
        pos = self.rows.pop() + len(self.rows) * 8
        self.diagonal_left.remove(self.coord_diag_mapping[pos][0])
        self.diagonal_right.remove(self.coord_diag_mapping[pos][1])

    def solve(self) -> None:
        if len(self.rows) == 8:
            ChessBoard.solutions.append(self.rows.copy())
            return

        for pos in self.next_valid_positions():
            self.push_queen(pos)
            self.solve()
            self.pop_queen()

    @staticmethod
    def print_solutions() -> None:
        for solution_count, solution in enumerate(ChessBoard.solutions, 1):
            print(f"Solution {solution_count}:")
            board = [["."] * 8 for _ in range(8)]
            for i, pos in enumerate(solution):
                row = i
                col = pos % 8
                board[row][col] = "Q"
            print("\n".join(" ".join(row) for row in board))
            print()


if __name__ == "__main__":
    from time import time

    chess_board = ChessBoard()
    start_time = time()
    chess_board.solve()
    end_time = time()
    ChessBoard.print_solutions()
    print(f'Time taken to find {len(ChessBoard.solutions)} solutions: {end_time - start_time:.4f} seconds')
