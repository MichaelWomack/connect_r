from board_state import BoardState
from state import StateUtils

class ConnectR():
    """class to create connect r """

    def __init__(self):
        self.depth = 5
        #self.game_setup()
        self.game = BoardState(5, 4, 4)


    def game_setup(self):
        try:
            M = int(input('Enter the width: ')) # Columns
            N = int(input('Enter the height: ')) # Rows
            R = int(input('Enter the win requirement: '))
            self.depth = int(input('Enter the max search depth (odd only): '))
            self.game = BoardState(M, N, R)
        except ValueError:
            self.game_setup()

    def prompt_move(self):
        player = self.game.current_player
        try:
            col = int(input(player + '\'s move: '))
            if col not in range(0, self.game.M):
                raise Exception("Out of Bounds!")
            if self.game.col_is_full(col):
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
        state_util = StateUtils(self.game)
        while not self.game.state_terminated:
            self.game.draw_board()
            print("Board Value: ", self.game.check_status())
            player = self.game.current_player
            if player == 'r':
                self.prompt_move()
            else:
                move = state_util.generate_states(self.game, state_util.max_depth)
                self.game.place_move(move, 'b')
            print()
            self.game.toggle_turn()

        print(self.game.termination_message)
        self.game.draw_board()
        print("Board Value: ", self.game.check_status())

if __name__ == "__main__":

        game = ConnectR()
        game.init()