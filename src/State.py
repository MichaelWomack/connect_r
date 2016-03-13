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
game = Connect_R()
state = game.rows

def display_state(state):
    for i in range(game.N):
        print("  ".join(state[i]))


def generate_states(state):






if __name__ == "__main__":
    game = Connect_R()
    display_state(game.rows)
    # game.draw_board()
    # while not game.game_over:
    #     # Represents one iteration or turn
    #     game.prompt_move()
    #     game.draw_board()
    #     game.check_game_over(game.p1)
    #     game.check_game_over(game.p2)