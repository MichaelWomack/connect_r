from board_state import BoardState
import time
import copy

#def MiniMax-Decision(state) returns an action

#def Max-Value(state) returns a utility value
    #if terminal-test(state) then return utility(state)

    #v --> -infinity
    #for each action in actions(state)
        # v --> Max(v, Min-Value(state, action))
    # return v


#def Min-Value(state) returns a utility value
    # if terminal-test(state) then return utility(state)

    # v --> infinity
    # for each action in actions(state)
        # v--> Min(v, Max-Value(state, action))
    # return v



#CREATE:
    # function that takes in state and generates all possible states
    # given the valid rules.

    # Utility function that takes in state and player, then generates
    # a numeric value denoting the quality of the state for the player.

    # Terminal test function that takes state and returns whether the game
    # is over or not.

    # Recursive min - max function.
# game = Connect_R()
# state = game.rows

# def display_state(state):
#     for i in range(game.N):
#         print("  ".join(state[i]))


# Shared Functions of State and Connect_R:
    # draw_board()/print_state()
    # place_move()
    # is_empty()
    # toggle_turn()



class StateUtils():
    """class to generate game states and handle utilities"""

    def __init__(self, game):
        self.max_depth = 3
        self.root_state = game

    # have to know player turn ????
    # generate state based on the current game state
        # pass in game current player
    def generate_states(self, state, depth):
        if depth != 0:
            for col in range(state.M):
                if not state.col_is_full(col):
                    new_state = BoardState(self.root_state.M, self.root_state.N, self.root_state.R)
                    new_state.rows = copy.deepcopy(state.rows)
                    new_state.current_player = state.current_player
                    new_state.place_move(col, new_state.current_player)
                    new_state.draw_board()
                    print()
                    print("State Depth: ", depth)
                    current_depth = depth
                    self.generate_states(new_state, depth=current_depth-1)
        else:
            print("Next State Build: ")












# if __name__ == "__main__":
#     game = Connect_R()
#     game.draw_board()
#     # game.draw_board()
#     # while not game.game_over:
#     #     # Represents one iteration or turn
#     #     game.prompt_move()
#     #     game.draw_board()
#     #     game.check_game_over(game.p1)
#     #     game.check_game_over(game.p2)