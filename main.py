### Tic-Tac-To ###
### *** REMEMBER TO REPLACE RANDOMPLAYER *** ###
import argparse

from game import TicTacToe
from players import Player, RandomPlayer


# --- GUI prep (commented out for now) ---
# def build_players(mode: str, seed: int | None) -> tuple[Player, Player]:
#     from players import HumanPlayer
#
#     if mode == "hvai":
#         return HumanPlayer(), RandomPlayer (seed=seed)
#     if seed is None:
#         return RandomPlayer(), RandomPlayer()
#     return RandomPlayer(seed=seed), RandomPlayer(seed=seed + 1)
#
#
# def launch_ui(mode: str | None, seed: int | None) -> None:
#     from gui import run_game
#
#     game = TicTacToe()
#     if mode is None:
#         from players import HumanPlayer
#
#         p1: Player = HumanPlayer()
#         p2: Player = RandomPlayer(seed=seed)
#         run_game(game, p1, p2, start_mode=None)
#     else:
#         p1, p2 = build_players(mode, seed)
#         run_game(game, p1, p2, start_mode=mode)


def run_cli() -> None:
    from game import tictactoe

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


def main() -> None:

    parser = argparse.ArgumentParser(description="Tic-Tac-Toe (CLI or GUI).")
    # parser.add_argument("--ui", action="store_true", help="launch pygame GUI")
    # parser.add_argument("--mode", choices=["hvai", "aiavai"], default=None,
    #                     help="GUI mode (skips title screen). hvai = Human vs AI, "
    #                          "aiavai = AI vs AI.")
    parser.add_argument("--seed", type=int, default=None,
                        help="RNG seed for the random bot(s).")
    args = parser.parse_args()

    # if args.ui:
    #     launch_ui(args.mode, args.seed)
    # else:
    run_cli()


if __name__ == "__main__":
    main()
