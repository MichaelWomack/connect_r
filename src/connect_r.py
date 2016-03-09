class Connect_R:
    'creates connect r'

    # Generate entire state space (to depth), evaluate the bottom (utility or heuristic)
    # Go from bottom to top
    # Can't generate entire space and move along, generate it every time (no memory)
    #       Every 2 moves, generate tree again
    # M: columns, N: rows
    # ask for M, ask for N, ask for R,
    # Red goes first
    # ask for time in microcycles,
    # Extra credit, implement timer in clock ticks
    # Depthometer

    # Block other person from winning,

    def __init__(self):
        # self.M = int(input('Enter the width: ')) # Columns
        # self.N = int(input('Enter the height: ')) # Rows
        # self.R = int(input('Enter the win requirement: '))

        self.p1 = 'r'
        self.p2 = 'b'
        self.p1_turn = True

        self.M = 7
        self.N = 6
        self.R = 4

        self.rows = [[' * ' for col in range(self.M)] for row in range(0, self.N)]
        self.game_over = False

    def draw_board(self):
        for i in range(0, self.N):
            print("".join(self.rows[i]))

    def place_move(self, col, char):
        # Get bottom most row (highest index), or where next index not ' * '
        if not self.is_empty(0, col):
            print("Column is full!")
            self.prompt_move()
        else:
            bottom_index = self.N - 1
            placed = False

            while bottom_index >= 0 and not placed:
                if self.is_empty(bottom_index, col):
                    self.rows[bottom_index][col] = ' ' + char + ' '
                    placed = True
                    self.p1_turn = not self.p1_turn
                else:
                    bottom_index -= 1

    def prompt_move(self):
        player = self.current_players_turn()
        col = int(input(player + '\'s move: '))
        if not (col in range(0, self.M)):
            print('Out of bounds!')
            self.prompt_move()
        else:
            self.place_move(col, player)

    def is_empty(self, row, col):
        return self.rows[row][col] == ' * '

    def current_players_turn(self):
        if self.p1_turn:
            return self.p1
        else:
            return self.p2

    def check_game_over(self, player):
        player = ' ' + player + ' '
        # M is num columns, N is num rows

        # check rows
        for row in reversed(self.rows):
            for col_index in range(self.M - self.R + 1):
                num_to_win = self.R
                index = col_index
                while index < col_index + self.R:
                    if row[index] == player:
                        num_to_win -= 1
                        if num_to_win == 0:
                            self.game_over = True
                            return self.game_over
                        index += 1
                    else:
                        break

        # check cols
        for col in range(self.M):
            for row in reversed(range(self.R - 1, self.N)):
                num_to_win = self.R
                index = row
                while index > row - self.R - 1:
                    if self.rows[index][col] == player:
                        num_to_win -= 1
                        if num_to_win == 0:
                            self.game_over = True
                            return self.game_over
                        index -= 1
                    else:
                        break



game = Connect_R()
game.draw_board()

while not game.game_over:
    # Represents one iteration or turn
    game.prompt_move()
    game.draw_board()
    game.check_game_over(game.p1)
    game.check_game_over(game.p2)
