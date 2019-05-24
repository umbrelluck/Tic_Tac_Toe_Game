from board import Board


class BTNode:
    def __init__(self, board, cell=None, result=0):
        self.board = board
        self.cell = cell
        self.result = result

    def move(self, where):
        return self.board.move(where)

    def check_win(self):
        return self.board.has_winner()


if __name__ == '__main__':
    bd = Board('X')
    bd.cells = [["O", 'X', 'O'], ['X', 'O', 'X'], ["O", 'X', 'O']]
    print(BTNode(bd).check_win())
