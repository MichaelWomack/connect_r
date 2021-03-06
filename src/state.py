from board_state import BoardState
import copy, random


# def MiniMax-Decision(state) returns an action

# def Max-Value(state) returns a utility value
# if terminal-test(state) then return utility(state)

# v --> -infinity
# for each action in actions(state)
# v --> Max(v, Min-Value(state, action))
# return v


# def Min-Value(state) returns a utility value
# if terminal-test(state) then return utility(state)

# v --> infinity
# for each action in actions(state)
# v--> Min(v, Max-Value(state, action))
# return v



# CREATE:
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
        self.max_depth = None
        self.root_state = game

    def mini_max(self, state, depth):
        child_values = []
        if depth > 1 and state.available_spaces():
            for col in range(state.M):
                if not state.col_is_full(col):
                    new_state = BoardState(self.root_state.M, self.root_state.N, self.root_state.R)
                    new_state.rows = copy.deepcopy(state.rows)
                    new_state.current_player = state.current_player
                    new_state.place_move(col, new_state.current_player)
                    next_depth = depth - 1
                    child_values.append(self.mini_max(new_state, depth=next_depth))
                else:
                    # just a placeholder to maintain branch/col indices
                    if depth % 2 == 1:
                        child_values.append(-100)
                    elif depth % 2 == 0:
                        child_values.append(100)

         # if depth is odd --> max, if depth even --> min
            # Max's turn
            if depth % 2 == 1:
                maximum = max(child_values)
                if depth == self.max_depth:
                    # if ai first, goes to middle position
                    if state.is_empty_state():
                        return int(state.M / 2)
                    elif child_values.count(maximum) < 2:
                        return child_values.index(maximum)
                    else:
                        # shake it up if more than one branch has the same max
                        maxima_indices = [index for index in range(len(child_values)) if child_values[index] == maximum]
                        return random.choice(maxima_indices)
                else:
                    return maximum
            # Min's turn
            elif depth % 2 == 0:
                minimum = min(child_values)
                return minimum
        else:
            return self.get_utility(state)


    def get_utility(self, state):
        # evaluate with utility function and return value
        ai_status = state.check_status(state.ai)
        opponent_status = state.check_status(state.opponent)
        if ai_status > opponent_status:
            return ai_status
        else:
            return -opponent_status
