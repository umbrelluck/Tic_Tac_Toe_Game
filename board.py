from copy import deepcopy


# code by Oles

def gen_combos():
    combinations = []
    for i in range(3):
        combination1 = []
        combination2 = []
        for j in range(3):
            combination1.append((i, j))
            combination2.append((j, i))
        combinations.append(combination1)
        combinations.append(combination2)

    combinations.append([(0, 0), (1, 1), (2, 2)])
    combinations.append([(0, 2), (1, 1), (2, 0)])
    return combinations


class Board:
    NOUGHT = 1
    CROSS = -1
    EMPTY = 0
    WIN_COMBOS = gen_combos()
    NOUGHT_WINNER = 1
    CROSS_WINNER = -1
    DRAW = 2
    NOT_FINISHED = 0

    def __init__(self, fl=False):
        self.cells = [[0] * 3 for i in range(3)]
        self.number_of_moves = 0
        # self.NOUGHT, self.CROSS = nought, -nought
        if fl:
            self.last_move = self.NOUGHT
        else:
            self.last_move = self.CROSS

        # self.NOUGHT_WINNER, self.CROSS_WINNER = nought, -nought

    def has_winner(self):
        for combo in self.WIN_COMBOS:
            lst = []
            for cell in combo:
                lst.append(self.cells[cell[0]][cell[1]])
            if max(lst) == min(lst) and max(lst) != self.EMPTY:
                return max(lst)
        if self.number_of_moves == 9:
            return Board.DRAW

        return self.NOT_FINISHED

    def human_move(self, cell):
        if self.number_of_moves == 9:
            return self.DRAW
        try:
            if self.cells[cell[0]][cell[1]] != self.EMPTY:
                raise IndexError
            # self.last_move = -self.last_move
            # self.number_of_moves += 1
            # self.cells[cell[0]][cell[1]] = self.last_move
            return True
        except IndexError:
            return False

    def __str__(self):
        result = ''
        for i in range(3):
            rs = ' | '
            for j in range(3):
                if self.cells[i][j] == self.CROSS:
                    rs += 'X'
                elif self.cells[i][j] == self.NOUGHT:
                    rs += 'O'
                else:
                    rs += ' '
                rs += ' | '
            result += rs + '\n'
        return result

    def free_cells(self):
        return [(i, j) for i in range(3) for j in range(3) if
                self.cells[i][j] == self.EMPTY]

    def move(self, where):
        new_board = deepcopy(self)
        new_board.last_move = -self.last_move
        new_board.cells[where[0]][where[1]] = new_board.last_move
        new_board.number_of_moves += 1
        return new_board
