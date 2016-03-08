import time
class Connect_R:
    'creates connect r'

    def __init__(self):
        # self.N = int(input('Enter the width: ')) # Columns
        # self.M = int(input('Enter the height: ')) # Rows
        # self.R = int(input('Enter the win requirement: '))

        self.N = 7
        self.M = 6
        self.R = 4

        self.rows = [[' * ' for i in range(0, self.N)] for j in range(0, self.M)]

    def draw_board(self):
        for i in range(0, self.M):
            print("".join(self.rows[i]))

    def place_move(self, col, char):
        # Get bottom most row (highest index), or where next index not ' * '
        if not self.is_empty(0, col):
            print("Column is full!")
            self.prompt_move()
        else:
            bottom_index = self.M - 1
            placed = False
            while bottom_index >= 0 and not placed:
                if self.is_empty(bottom_index, col):
                    self.rows[bottom_index][col] = ' ' + char + ' '
                    placed = True
                else:
                    bottom_index -= 1

    def prompt_move(self):
        col = int(input('col: '))
        if not (col in range(0, self.N)):
            print('Out of bounds!')
            self.prompt_move()
        else:
            self.place_move(col, 'B')


    def is_empty(self, row, col):
        return self.rows[row][col] == ' * '

game = Connect_R()
game.draw_board()

for i in range(0, 7):
    game.prompt_move()
    game.draw_board()


