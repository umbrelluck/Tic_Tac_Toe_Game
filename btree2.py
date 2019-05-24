from btnode import BTNode
from random import shuffle


class Btree:
    def __init__(self, board, cell=None):
        self.root = BTNode(board, cell)
        self.games = []

    def clear(self):
        self.root = None

    def build(self):
        free_cells = self.root.board.free_cells()
        # shuffle(free_cells)
        for position in free_cells:
            new_board = self.root.move(position)
            new_tree = Btree(new_board, position)
            new_tree.build()
            self.games.append(new_tree)
        return None

    def calculate(self):
        win = self.root.board.has_winner()
        if win != self.root.board.NOT_FINISHED:
            if win != self.root.board.DRAW:
                self.root.result = win
        else:
            lst = []
            for game in self.games:
                game.calculate()
                lst.append(game.root.result)
            if self.root.board.last_move == self.root.board.CROSS:
                self.root.result = max(lst)
            else:
                self.root.result = min(lst)

    def search_best_move(self):
        self.build()
        self.calculate()
        best = None
        for game in self.games:
            if game.root.result == self.root.result and (not best or len(game) > len(best)):
                best = game
        # return best.root.result, best.root.cell
        return best.root.cell

    def __iter__(self):
        return self.games.__iter__()

    def __len__(self):
        def recurse(tree):
            if not tree.games:
                return 0
            else:
                return 1 + max([recurse(elem) for elem in tree.games])

        return recurse(self)

    def move(self, where):
        new_board = self.root.move(where)
        new_tree = Btree(new_board)
        new_tree.root.cell = None
        return new_tree

    def __str__(self):
        return str(self.root.result, self.root.board.last_move)
