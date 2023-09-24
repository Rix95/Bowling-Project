from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name="John Doe", type="human"):
        self.type = type
        self._score = 0
        self._pins_thrown_per_round = [[] for _ in range(10)]
        self._round_score = [0 for _ in range(10)]
        self._cumulative_round_score = [0 for _ in range(10)]
        self._round_bonus = [None for _ in range(10)]
        self.name = name
        print("Player created:", name)

    @abstractmethod
    def throw():
        pass

    @property
    def pins_thrown_per_round(self, round=-1):
        return self._pins_thrown_per_round

    @property
    def round_bonus(self, round=-1):
        return self._round_bonus

    @property
    def round_score(self):
        return self._round_score

    @property
    def cumulative_round_score(self):
        return self._cumulative_round_score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score_to_add):
        self._score = score_to_add

    def __str__(self) -> str:
        return self.name

    # @property
