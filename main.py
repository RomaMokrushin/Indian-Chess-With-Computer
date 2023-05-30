import random
import time

WHITE = 1
BLACK = 2
Stalemate = False


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def print_board(board):
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col, end='    ')
    print()


def main():
    print('1: play with friend')
    print('2: play with computer')
    while True:
        answer = input()
        if answer == '1':
            play_with_friend()
            break
        if answer == '2':
            play_with_computer()
            break
        else:
            print('Incorrect input. Try again!')


def play_with_friend():
    board = Board()
    print('Игра с другом успешно начата!')
    while True:
        print_board(board)
        print('Команды:')
        print('    exit                               -- выход')
        print('    move <row> <col> <row1> <row1>     -- ход из клетки (row, col)')
        print('                                          в клетку (row1, col1)')
        if board.current_player_color() == WHITE:
            print('Ход белых:')
        else:
            print('Ход чёрных:')
        command = input()
        if command == 'exit':
            break
        move_type, row, col, row1, col1 = command.split()
        row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
        if board.move_piece(row, col, row1, col1):
            print('Ход успешен')
            if death(board) == 'wK':
                print('Король съеден!')
                print('Победа Черных!')
                break
            if death(board) == 'bK':
                print('Король съеден!')
                print('Победа Белых!')
                break
        else:
            print('Координаты некорректы! Попробуйте другой ход!')


def play_with_computer():
    # global Stalemate
    board = Board()
    win = False
    You_White = False
    You_Black = False
    print('Выбрать цвет: 1')
    print('Случайный цвет: 2')
    while True:
        answer = input()
        if answer == '1':
            print('Вы за черных: 1')
            print('Вы за белых: 2')
            while True:
                ans = input()
                if ans == '1':
                    print('Успешно выбран цвет!')
                    You_Black = True
                    break
                if ans == '2':
                    print('Успешно выбран цвет!')
                    You_White = True
                    break
                else:
                    print('Неверно указан цвет. Повторите попытку!')
            break
        if answer == '2':
            color = random.randint(1, 2)
            if color == 1:
                You_White = True
                print('Вы играете за белых!')
            if color == 2:
                You_Black = True
                print('Вы играете за черных!')
            break
        else:
            print('Incorrect input. Try again!')
    while True:
        if win:
            break
        # if Stalemate:
        # print('Ничья')
        # break
        print_board(board)
        print('Команды:')
        print('    exit                               -- выход')
        print('    move <row> <col> <row1> <row1>     -- ход из клетки (row, col)')
        print('                                          в клетку (row1, col1)')
        if board.current_player_color() == WHITE:
            print('Ход белых:')
        else:
            print('Ход чёрных:')
        if You_White and board.current_player_color() == WHITE:
            while True:
                command = input()
                if command == 'exit':
                    break
                move_type, row, col, row1, col1 = command.split()
                row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
                if board.move_piece(row, col, row1, col1):
                    print('Ход успешен')
                    if death(board) == 'wK':
                        print('Король съеден!')
                        print('Победа Черных!')
                        win = True
                        break
                    if death(board) == 'bK':
                        print('Король съеден!')
                        print('Победа Белых!')
                        win = True
                        break
                    break
                else:
                    print('Координаты некорректы! Попробуйте другой ход!')
        if You_Black and board.current_player_color() == BLACK:
            while True:
                command = input()
                if command == 'exit':
                    break
                move_type, row, col, row1, col1 = command.split()
                row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
                if board.move_piece(row, col, row1, col1):
                    print('Ход успешен')
                    if death(board) == 'wK':
                        print('Король съеден!')
                        print('Победа Черных!')
                        win = True
                        break
                    if death(board) == 'bK':
                        print('Король съеден!')
                        print('Победа Белых!')
                        win = True
                        break
                    break
                else:
                    print('Координаты некорректы! Попробуйте другой ход!')
        print_board(board)
        computer(board)
        time.sleep(5)


def computer(board):
    global Stalemate
    attempts = 0
    while attempts < 1000000:
        if board.move_piece(random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7)):
            break
        attempts = attempts + 1
    # print('Пат')
    # Stalemate = True


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        if color == WHITE:
            c = 'w'
        else:
            c = 'b'
        return c + piece.char()

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]
        else:
            return None

    def move_piece(self, row, col, row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if self.field[row1][col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        elif self.field[row1][col1].get_color() == opponent(piece.get_color()):
            if not piece.can_attack(self, row, col, row1, col1):
                return False
        else:
            return False
        if piece.__class__.__name__ in ['Rook', 'King']:
            piece.move()
        self.field[row][col] = None
        self.field[row1][col1] = piece
        self.color = opponent(self.color)
        return True

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        if self.field[row][col].char() != 'P':
            return False
        piece = self.field[row][col]
        color = self.field[row][col].get_color()
        if piece.can_move(self, row, col, row1, col1) \
                or piece.can_attack(self, row, col, row1, col1):
            self.move_piece(row, col, row1, col1)
            if char == 'Q':
                self.field[row1][col1] = Queen(color)
            elif char == 'R':
                self.field[row1][col1] = Rook(color)
            elif char == 'B':
                self.field[row1][col1] = Bishop(color)
            elif char == 'N':
                self.field[row1][col1] = Knight(color)
            return True
        return False

    def castling0(self):
        if self.color == WHITE:
            if self.field[0][0] is None:
                return False
            if self.field[0][0].char() != 'R':
                return False
            if self.field[0][0].has_moved:
                return False
            if self.field[0][4] is None:
                return False
            if self.field[0][4].char() != 'K':
                return False
            if self.field[0][4].has_moved:
                return False
            if self.field[0][0].can_move(self, 0, 0, 0, 3):
                if self.field[0][3] is not None:
                    return False
                self.move_piece(0, 0, 0, 3)
                self.color = opponent(self.color)
                self.move_piece(0, 4, 0, 2)
                return True
        else:
            if self.field[7][0] is None:
                return False
            if self.field[7][0].char() != 'R':
                return False
            if self.field[7][0].has_moved:
                return False
            if self.field[7][4] is None:
                return False
            if self.field[7][4].char() != 'K':
                return False
            if self.field[7][4].has_moved:
                return False
            if self.field[7][0].can_move(self, 7, 0, 7, 3):
                if self.field[7][3] is not None:
                    return False
                self.move_piece(7, 0, 7, 3)
                self.color = opponent(self.color)
                self.move_piece(7, 4, 7, 2)
                return True
        return False

    def castling7(self):
        if self.color == WHITE:
            if self.field[0][7] is None:
                return False
            if self.field[0][7].char() != 'R':
                return False
            if self.field[0][7].has_moved:
                return False
            if self.field[0][4] is None:
                return False
            if self.field[0][4].char() != 'K':
                return False
            if self.field[0][4].has_moved:
                return False
            if self.field[0][7].can_move(self, 0, 7, 0, 5):
                if self.field[0][5] is not None:
                    return False
                self.move_piece(0, 7, 0, 5)
                self.color = opponent(self.color)
                self.move_piece(0, 4, 0, 6)
                return True
        else:
            if self.field[7][7] is None:
                return False
            if self.field[7][7].char() != 'R':
                return False
            if self.field[7][7].has_moved:
                return False
            if self.field[7][4] is None:
                return False
            if self.field[7][4].char() != 'K':
                return False
            if self.field[7][4].has_moved:
                return False
            if self.field[7][7].can_move(self, 7, 7, 7, 5):
                if self.field[7][5] is not None:
                    return False
                self.move_piece(7, 7, 7, 5)
                self.color = opponent(self.color)
                self.move_piece(7, 4, 7, 6)
                return True
        return False


class Rook:
    def __init__(self, color):
        self.color = color
        self.has_moved = False

    def move(self):
        self.has_moved = True

    def get_color(self):
        return self.color

    def char(self):
        return 'R'

    def can_move(self, board, row, col, row1, col1):
        color = board.get_piece(row, col).get_color()
        if row != row1 and col != col1:
            return False

        if row == row1 and col == col1:
            return False

        if row1 >= row:
            step = 1
        else:
            step = -1
        for r in range(row + step, row1, step):
            if not (board.get_piece(r, col) is None):
                return False

        if col1 >= col:
            step = 1
        else:
            step = -1
        for c in range(col + step, col1, step):
            if not (board.get_piece(row, c) is None):
                return False
        if board.get_piece(row1, col1) is not None:
            return board.get_piece(row1, col1).get_color() == opponent(color)
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Pawn:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'P'

    def can_move(self, board, row, col, row1, col1):
        if col != col1:
            return False
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
        if row + direction == row1:
            return board.get_piece(row1, col1) is None
        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return board.get_piece(row1, col1) is None
        return False

    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if (self.color == WHITE) else -1
        if (row + direction == row1
                and (col + 1 == col1 or col - 1 == col1)):
            return board.get_piece(row1, col1).get_color() == opponent(self.color)


class Knight:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'N'

    def can_move(self, board, row, col, row1, col1):
        if not correct_coords(row1, col1):
            return False
        if row1 == row or col1 == col:
            return False
        if abs(row - row1) + abs(col - col1) != 3:
            return False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class King:
    def __init__(self, color):
        self.color = color
        self.has_moved = False

    def get_color(self):
        return self.color

    def move(self):
        self.has_moved = True

    def char(self):
        return 'K'

    def can_move(self, board, row, col, row1, col1):
        if not correct_coords(row1, col1):
            return False
        if row1 == row and col1 == col:
            return False
        if abs(row - row1) > 1 or abs(row - row1):
            return False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Queen:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'Q'

    def can_move(self, board, row, col, row1, col1):
        color = board.get_piece(row, col).get_color()
        if abs(row1 - row) == abs(col1 - col) and (row1 != row or col1 != col) \
                or row1 == row and col1 != col or row1 != row and col1 == col:
            row_step = row1 - row
            if row_step != 0:
                row_step //= abs(row_step)
            col_step = col1 - col
            if col_step != 0:
                col_step //= abs(col_step)
            if row_step != 0:
                cur_col = col
                for cur_row in range(row + row_step, row1, row_step):
                    cur_col += col_step
                    if board.get_piece(cur_row, cur_col) is not None:
                        return False
            else:
                cur_row = row
                for cur_col in range(col + col_step, col1, col_step):
                    cur_row += row_step
                    if board.get_piece(cur_row, cur_col) is not None:
                        return False
            if board.get_piece(row1, col1) is not None:
                return board.get_piece(row1, col1).get_color() == opponent(color)
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Bishop:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return 'B'

    def can_move(self, board, row, col, row1, col1):
        color = board.get_piece(row, col).get_color()
        if not correct_coords(row1, col1):
            return False
        if row1 == row or col1 == col:
            return False
        if abs(row - row1) != abs(col - col1):
            return False
        if board.get_piece(row1, col1) is not None:
            return board.get_piece(row1, col1).get_color() == opponent(color)
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


def death(board):
    king = list()
    for row in range(7, -1, -1):
        for col in range(8):
            king.append(board.cell(row, col))
    if 'wK' not in king:
        return 'wK'
    if 'bK' not in king:
        return 'bK'


main()
