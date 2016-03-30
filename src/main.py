from board_state import BoardState
from state import StateUtils

class ConnectR():
    """class to create connect r """

    def __init__(self):
        self.depth = 5
        self.game = BoardState(5, 4, 3)
        self.game_setup()


    def game_setup(self):
        try:
            M = int(input('Enter the width: ')) # Columns
            N = int(input('Enter the height: ')) # Rows
            R = int(input('Enter the win requirement: '))
            ai = input('Red will go first. Enter AI color (r or b): ')
            assert ai == 'r' or ai == 'b'
            self.depth = int(input('Enter the max search depth (odd only): '))
            assert self.depth % 2 == 1
            self.game = BoardState(M, N, R)
            self.game.ai = ai
            if self.game.ai == 'r':
                self.game.opponent = 'b'
            else:
                self.game.opponent = 'r'
        except ValueError:
            print("Incorrect game setup...\n")
            self.game_setup()
        except AssertionError:
            print('Incorrect input for game ai....\n')
            self.game_setup()

    def prompt_move(self, state_util):
        player = self.game.current_player
        if player == self.game.ai:
            col = state_util.mini_max(self.game, state_util.max_depth)
            self.game.place_move(col, player)
        else:
            try:
                col = int(input(player + '\'s move: '))
                if col not in range(0, self.game.M):
                    raise Exception("Out of Bounds!")
                if self.game.col_is_full(col):
                    raise Exception("Column is Full!")
                self.game.place_move(col, player)
            except ValueError:
                print("Move must be an integer!")
                self.prompt_move(state_util)
            except Exception as e:
                print(e)
                self.prompt_move(state_util)

    def init(self):
        # represents one turn iteration
        state_util = StateUtils(self.game)
        state_util.max_depth = self.depth
        while not self.game.state_terminated:
            self.game.draw_board()
            print("Board Value: {}".format(self.game.check_status()))
            print("Current Player: {} AI: {}\n".format(self.game.current_player, self.game.ai))
            self.prompt_move(state_util)

        print(self.game.termination_message)
        self.game.draw_board()
        print("Board Value: ", self.game.check_status())

if __name__ == "__main__":

        game = ConnectR()
        game.init()