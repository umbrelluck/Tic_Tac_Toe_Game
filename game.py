from btree2 import Btree
from board import Board
import random

transform = {1: 'You', -1: "PC"}


class Game:
    def __init__(self):
        self.player = random.choice((1, -1))
        if self.player > 0:
            board = Board(True)
        else:
            board = Board()
        self.tree = Btree(board)

    def _play(self):
        if self.player > 0:
            print('It is your turn now\n')
            print(self.tree.root.board, '\n')
            ans = input('Enter your position (if it is (1,1), enter 11)\n ==> ')
            while not self.tree.root.board.human_move((int(ans[0]) - 1, int(ans[1]) - 1)):
                print('Your input is incorrect')
                ans = input('Enter your position (if it is (1,1)), enter 11\n ==> ')
            self.tree = self.tree.move((int(ans[0]) - 1, int(ans[1]) - 1))
        else:
            print('I am thinking')
            cell = self.tree.search_best_move()
            self.tree = self.tree.move(cell)
            print('Done\n')

        win = self.tree.root.board.has_winner()
        if win == 2:
            print(self.tree.root.board)
            print('That`s a draw')
            return False
        elif win == 1:
            print(self.tree.root.board)
            print('You loose')
            return False
        elif win == -1:
            print(self.tree.root.board)
            print('You win')
            return False
        self.player = -self.player
        return True

    def play(self):
        fl = True
        while fl:
            fl = self._play()


if __name__ == '__main__':
    Game().play()
    # bd = Board()
    # bd.cells = [[-1, -1, 1], [-1, -1, 1], [1, 0, 0]]
    # bd.number_of_moves=7
    # tree = Btree(bd)
    # print(tree.search_best_move())
