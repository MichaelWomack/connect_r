from board_state import BoardState

class ConnectR():
    """class to create connect r """

    def __init__(self):
        #self.game_setup()
        self.game = BoardState(7, 6, 4)

    def game_setup(self):
        try:
            M = int(input('Enter the width: ')) # Columns
            N = int(input('Enter the height: ')) # Rows
            R = int(input('Enter the win requirement: '))
            self.game = BoardState(M, N, R)
        except ValueError:
            self.game_setup()

    def prompt_move(self):
        player = self.game.current_player
        try:
            col = int(input(player + '\'s move: '))
            if col not in range(0, self.game.M):
                raise Exception("Out of Bounds!")
            if not self.game.is_empty(0, col):
                raise Exception("Column is Full!")
            self.game.place_move(col, player)
        except ValueError:
            print("Move must be an integer!")
            self.prompt_move()
        except Exception as e:
            print(e)
            self.prompt_move()

    def init(self):
        # represents one turn iteration
        while not self.game.state_terminated:
            self.game.draw_board()
            self.prompt_move()
            self.game.check_status()
            self.game.toggle_turn()

        self.game.draw_board()
        print(self.game.termination_message)


if __name__ == "__main__":
        # Represents one iteration or turn
        game = ConnectR()
        game.init()