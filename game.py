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

        if game_state[row][col] != 0:
            raise ValueError(f"{action} is already occupied.")

        game_state[row][col] = player
        return game_state

    def get_actions(self, game_state):
        return np.where(game_state.reshape(-1) == 0)[0].tolist()

    def win_check(self, game_state, action):
        row = action // self.cols
        col = action % self.cols
        player = game_state[row][col]

        return (
            np.sum(game_state[row, :]) == player * self.cols
            or np.sum(game_state[:, col]) == player * self.rows
            or np.sum(np.diag(game_state)) == player * self.rows
            or np.sum(np.diag(np.fliplr(game_state))) == player * self.rows
        )

    def get_result_and_termination(self, game_state, action):
        if self.win_check(game_state, action):
            return 1, True
        elif len(self.get_actions(game_state)) == 0:
            return 0, True
        else:
            return 0, False

    def get_opponent(self, player):
        return -player


tictactoe = TicTacToe()
player = 1

game_state = tictactoe.get_initial_game_state()

while True:
    print(game_state)

    valid_moves = tictactoe.get_actions(game_state)
    print("valid_moves", valid_moves)

    action = int(input(f" {player} enter your move: "))

    if action not in valid_moves:
        print("invalid")
        continue

    game_state = tictactoe.get_next_state(game_state, action, player)
    result, done = tictactoe.get_result_and_termination(game_state, action)

    if done:
        print(game_state)

        if result == 0:
            print("Draw")
        elif result == 1:
            print(f"Player {player} wins")

        break

    player = tictactoe.get_opponent(player)