import sys

from game import TicTacToe


def main():
    if "--ui" in sys.argv:
        print("Launching UI...")

    else:
        print("CLI mode...")
    

    state = tictactoe.get_initial_game_state()

if __name__ == "__main__":
    main()
