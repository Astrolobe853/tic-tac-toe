import numpy as np

class TicTacToe:
    def __init__(self):
        self.rows = 3
        self.cols = 3
        self.actions = self.rows * self.cols

    def get_initial_game_state(self):
        return np.zeros((self.rows, self.cols))

    def get_next_state(self, game_state, action, player):
        row = action // self.cols
        col = action % self.cols
        game_state[row][col] = player
        return game_state

    def get_actions(self, game_state):
        return (game_state.reshape(-1) == 0).nonzero()

    def win_check(self, game_state, action):
        row = action // self.cols
        col = action % self.cols
        player = game_state[row][col]

        return (
            np.sum(game_state[row, :]) == player * self.cols
            or np.sum(game_state[:, col]) == player * self.rows

        )