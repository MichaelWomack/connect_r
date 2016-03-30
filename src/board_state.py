import math

class BoardState:
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

    def __init__(self, width, height, win_req):
        self.current_player = 'r'
        self.ai = None

        self.M = width
        self.N = height
        self.R = win_req

        self.rows = [['*' for col in range(self.M)] for row in range(0, self.N)]
        self.state_terminated = False
        self.termination_message = None
        self.state_value = 0


    def draw_board(self):
        col_names = "  ".join([str(i) for i in range(self.M)])
        print(col_names)
        for i in range(0, self.N):
            print("  ".join(self.rows[i]))

    def place_move(self, col, player):
        bottom_index = self.N - 1
        placed = False

        while bottom_index >= 0 and not placed:
            if self.is_empty(bottom_index, col):
                self.rows[bottom_index][col] = player
                placed = True
                # Might need to move this termination function somewhere else
                self.check_status()
                if not self.state_terminated:
                    self.toggle_turn()
            else:
                bottom_index -= 1

    def col_is_full(self, col):
        return self.rows[0][col] != '*'

    def is_empty(self, row, col):
        return self.rows[row][col] == '*'

    def is_empty_state(self):
        row_index = self.N - 1
        for col in range(self.M):
            if not self.is_empty(row_index, col):
                return False
        return True

    def toggle_turn(self):
        if self.current_player == 'r':
            self.current_player = 'b'
        elif self.current_player == 'b':
            self.current_player = 'r'

    def check_status(self):
        player = self.current_player

        # stores tuple of values that represent number to win vs number of valid spots left to win
        values = []
        # M is num columns, N is num rows

        # check if board full for draw
        if '*' not in self.rows[0]:
            self.state_terminated = True
            self.termination_message = "Draw!"
            return 0

        # check rows
        for row in reversed(self.rows):
            for col_index in range(self.M - self.R + 1):
                num_to_win = self.R
                empty_spaces = 0
                index = col_index
                while index < col_index + self.R:
                    if row[index] == player:
                        num_to_win -= 1
                        if num_to_win == 0:
                            self.state_terminated = True
                            self.termination_message = "Row Win!: {}".format(player)
                            return 1
                    elif row[index] == '*':
                        empty_spaces += 1
                        if index == col_index + self.R - 1:
                            values.append((num_to_win, empty_spaces))
                    # add accumulated values if opponent's piece or last iteration of loop
                    else:
                        values.append((num_to_win, empty_spaces))
                        break
                    index += 1

        # check cols
        for col in range(self.M):
            for row in reversed(range(self.R - 1, self.N)):
                num_to_win = self.R
                empty_spaces = 0
                index = row
                while index > row - self.R:
                    if self.rows[index][col] == player:
                        num_to_win -= 1
                        if num_to_win == 0:
                            self.state_terminated = True
                            self.termination_message = "Column Win!: {}".format(player)
                            return 1
                    elif self.rows[index][col] == '*':
                        empty_spaces += 1
                        if index - num_to_win >= 0:
                            values.append((num_to_win, num_to_win))
                        # else:
                        #     values.append((num_to_win, empty_spaces))
                        break
                    else:
                        break
                    index -= 1

        # check diagonals L --> R high to low
        for col in range(self.M - self.R + 1):
            for row in reversed(range(self.N - self.R + 1)):
                col_index = col
                row_index = row
                num_to_win = self.R
                empty_spaces = 0
                while col_index in range(self.M) and row_index in range(self.N):
                    if self.rows[row_index][col_index] == player:
                        num_to_win -= 1
                        if num_to_win == 0:
                            self.state_terminated = True
                            self.termination_message = "Diagonal Win!: {}".format(player)
                            return 1
                    elif self.rows[row_index][col_index] == '*':
                        empty_spaces += 1
                    else:
                        values.append((num_to_win, empty_spaces))
                        num_to_win = self.R
                        empty_spaces = 0
                    row_index += 1
                    col_index += 1

        # check diagonals L-->R low to high
        # for col in range(self.M - self.R + 1):
            for row in range(self.R - 1, self.N):
                col_index = col
                row_index = row
                num_to_win = self.R
                empty_spaces = 0
                while col_index in range(self.M) and row_index in range(self.N):
                    if self.rows[row_index][col_index] == player:
                        num_to_win -= 1
                        if num_to_win == 0:
                            self.state_terminated = True
                            self.termination_message = "Diagonal Win!: {}".format(player)
                            return 1
                    elif self.rows[row_index][col_index] == '*':
                        empty_spaces += 1
                    else:
                        values.append((num_to_win, empty_spaces))
                        num_to_win = self.R
                        empty_spaces = 0
                    row_index -= 1
                    col_index += 1

        very_high = self.R - 1
        high = self.R - 2
        med = self.R - 3

    # (num to win, num empty spaces) tuple represents the ratio of pieces in a row available spaces to win
        very_high_count = values.count((1, 1))
        high_count = values.count((2, 2))
        med_count = values.count((3, 3))

        val = 0

        #print(values)
        if self.is_empty_state():
            return 0

        elif very_high_count > 0:
           val = ((very_high/self.R) * very_high_count) + (high/math.pow(self.R, 2)) * high_count

        elif high_count > 0:
            val = ((high/math.pow(self.R, 2)) * high_count) + med/(math.pow(self.R, 3)) * med_count

        elif med_count > 0:
            val = med/(math.pow(self.R, 3)) * med_count

        else:
            return 0

        return val
        #
        # if player == self.ai:
        #     return val
        # else:
        #     return -val




