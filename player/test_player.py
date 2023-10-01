from player.player import Player


available_tests = [
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[10], [10], [10], [10], [10], [10], [10], [10], [10], [10, 10, 10]],
    [[9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1, 9]],
    [[10], [10], [10], [1, 9], [8, 1], [0, 0], [7, 0], [10], [10], [8, 1]],
]


class TestPlayer(Player):
    def __init__(
        self,
        name="John Doe",
        test_selected=0,
        type="test",
    ):
        super().__init__(name, type)
        self.current_round = 0
        self.test = available_tests[test_selected].copy()

    def throw(self, pins_left, current_throw):
        # need validation future
        if self.test[self.current_round] == []:
            self.current_round += 1
        print(
            "Test Player is throwing",
            self.test[self.current_round][0],
            " pins",
            pins_left - self.test[self.current_round][0],
            "pins left.",
        )
        return self.test[self.current_round].pop(0)
