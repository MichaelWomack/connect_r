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

        self.M = width
        self.N = height
        self.R = win_req

        self.rows = [['*' for col in range(self.M)] for row in range(0, self.N)]
        self.state_terminated = False
        self.termination_message = None


    def draw_board(self):
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
                self.toggle_turn()
            else:
                bottom_index -= 1

    def col_is_full(self, col):
        return self.rows[0][col] != '*'

    def is_empty(self, row, col):
        return self.rows[row][col] == '*'

    def is_empty_state(self):
        row_index = self.N - 1
        for col in self.rows[row_index]:
            if self.is_empty(row_index, col):
                return False
        return True

    def toggle_turn(self):
        if self.current_player == 'r':
            self.current_player = 'b'
        elif self.current_player == 'b':
            self.current_player = 'r'

    def termination_status(self):
        return self.check_status() == 1

    def check_status(self):
        player = self.current_player
        value = 0
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
                index = col_index
                while index < col_index + self.R:
                    if row[index] == player:
                        num_to_win -= 1
                        if num_to_win == 0:
                            self.state_terminated = True
                            self.termination_message = "Row Win!: {}".format(player)
                            return 1
                        index += 1
                    else:
                        values.append(self.R - num_to_win)
                        # value += (self.R - num_to_win)/self.R
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
                            self.state_terminated = True
                            self.termination_message = "Column Win!: {}".format(player)
                            return 1
                        index -= 1
                    else:
                        values.append(self.R - num_to_win)
                        break

        # check diagonals L --> R high to low
        for col in range(self.M - self.R + 1):
            for row in reversed(range(self.N - self.R + 1)):
                col_index = col
                row_index = row
                num_to_win = self.R
                while col_index in range(self.M) and row_index in range(self.N):
                    if self.rows[row_index][col_index] == player:
                        num_to_win -= 1
                        if num_to_win == 0:
                            self.state_terminated = True
                            self.termination_message = "Diagonal Win!: {}".format(player)
                            return 1
                    else:
                        values.append(self.R - num_to_win)
                        num_to_win = 0
                    row_index += 1
                    col_index += 1

        # check diagonals L-->R low to high
        # for col in range(self.M - self.R + 1):
            for row in range(self.R - 1, self.N):
                col_index = col
                row_index = row
                num_to_win = self.R
                while col_index in range(self.M) and row_index in range(self.N):
                    if self.rows[row_index][col_index] == player:
                        num_to_win -= 1
                        if num_to_win == 0:
                            self.state_terminated = True
                            self.termination_message = "Diagonal Win!: {}".format(player)
                            return 1
                    else:
                        values.append(self.R - num_to_win)
                        num_to_win = 0
                    row_index -= 1
                    col_index += 1


        return sum(values)/len(values)


