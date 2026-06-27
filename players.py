

from typing import Protocol, runtime_checkable

import numpy as np

from game import TicTacToe


@runtime_checkable
class Player(Protocol):

    def select_action(
        self, game: TicTacToe, state: np.ndarray, player: int
    ) -> int: ...


class HumanPlayer:
    def __init__(self) -> None:
        self._pending_action: int | None = None

    def set_pending(self, action: int) -> None:
        self._pending_action = action

    def select_action(
        self, game: TicTacToe, state: np.ndarray, player: int
    ) -> int:
        if self._pending_action is None:
            raise RuntimeError("HumanPlayer.select_action called with no pending click")
        action = self._pending_action
        self._pending_action = None
        return action


class RandomPlayer:
    # Picks uniformly from legal actions. A placeholder bot
    # until the engine is ready. Reproducible
    # demos (e.g. `--seed 42`).

    def __init__(self, seed: int | None = None) -> None:
        self._rng = np.random.default_rng(seed)

    def select_action(
        self, game: TicTacToe, state: np.ndarray, player: int
    ) -> int:
        actions = game.get_actions(state)
        return int(self._rng.choice(actions))
