from connect_r import Connect_R


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

    def __init__(self, M, N):
        self.current_player = None
        self.depth = 0
        self.num_cols = M
        self.num_rows = N

def toggle_state_player(self, current_player):
    if current_player == 'r':
        return 'b'
    else:
        return 'r'

    # have to know player turn ????
    # generate state based on the current game state
        # pass in game current player
def generate_states(state, player=None):
    if player is None:
        player = toggle_state_player()
    for col in range(state.M):
        new_state = Connect_R()
        new_state.place_move(col, player)
        generate_states(new_state)



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