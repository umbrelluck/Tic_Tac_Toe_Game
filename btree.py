from btnode import BTNode
from random import shuffle


class Btree:
    def __init__(self, board, cell=None):
        self.root = BTNode(board, cell)
        self.games = []

    def clear(self):
        self.root = None

    def search_best_move(self):
        def recurse(tree):
            free_cells = tree.root.board.free_cells()
            shuffle(free_cells)
            win = tree.root.check_win()
            if win == tree.root.board.DRAW:
                return 0, (0,)
            elif win != tree.root.board.NOT_FINISHED:
                return win, (0,)
            else:
                best_lst = []
                for cell in free_cells:
                    new_board = tree.root.move(cell)
                    tr = Btree(new_board, cell)
                    tree.games.append(tr)
                    best_lst.append(recurse(tr)[0])

                if tree.root.board.last_move == tree.root.board.CROSS:
                    tree.root.result = max(best_lst)
                    if not tree.root.cell:
                        tmp, helper = max(best_lst), []
                        for elem in tree:
                            if tmp == elem.root.result:
                                helper.append(elem)
                        while len(helper) > 1:
                            if len(helper[0]) >= len(helper[1]):
                                helper.pop(1)
                            else:
                                helper.pop(0)
                        tree.root.cell = helper[0].root.cell
                    return tree.root.result, tree.root.cell
                else:
                    tree.root.result = min(best_lst)
                    if not tree.root.cell:
                        tmp, helper = min(best_lst), []
                        for elem in tree:
                            if tmp == elem.root.result:
                                helper.append(elem)
                        while len(helper) > 1:
                            if len(helper[0]) >= len(helper[1]):
                                helper.pop(1)
                            else:
                                helper.pop(0)
                        tree.root.cell = helper[0].root.cell
                    return tree.root.result, tree.root.cell

        result = recurse(self)
        return result[1]

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
