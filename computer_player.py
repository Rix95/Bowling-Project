import math
import random
from player import Player


class ComputerPlayer(Player):
    def __init__(self, name="ChatGPT", difficulty="normal", type="computer"):
        super().__init__(name, type)
        self.difficulty = difficulty
        self.difficulty_dict = {"easy": 0, "normal": 1, "hard": 2, "sans": 3}
        self.difficulty_weights_first_throw = [
            [5, 7, 10, 17, 15, 12, 10, 7, 6, 6, 5, 1],
            [3, 4, 5, 10, 13, 17, 13, 11, 9, 8, 7],
            [3, 4, 5, 10, 13, 17, 13, 11, 9, 8, 7],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 99],
        ]
        self.difficulty_weights_second_throw = [[85, 15], [75, 25], [50, 50], [0, 100]]

    def throw(self, pins_left, current_throw):
        if current_throw == "first":
            print("It's", self.name, "'s turn.")
            pins_thrown = self.get_random_first_throw()
            print(
                self.name,
                " knocked down",
                pins_thrown,
                "pins.",
                pins_left - pins_thrown,
                "pins left.",
            )
            if pins_thrown == pins_left:
                print("Robo-Strike")
        else:
            pins_thrown = self.get_random_second_throw(pins_left)
            print(
                self.name,
                " knocked down",
                pins_thrown,
                "pin(s).",
                pins_left - pins_thrown,
                "pins left.",
            )
            if pins_thrown == pins_left:
                print("Techno-Spare!")

        return pins_thrown

    def get_random_first_throw(self):
        difficulty = self.difficulty_dict[self.difficulty]
        return random.choices(
            range(11), weights=self.difficulty_weights_first_throw[difficulty]
        )[0]

    def get_random_second_throw(self, pins_left):
        difficulty = self.difficulty_dict[self.difficulty]
        determinant = random.choices(
            range(2), weights=self.difficulty_weights_second_throw[difficulty]
        )[0]

        if determinant == 0:
            # return random.randint(0, pins_left - 1)  # ensure its not an spare
            return random.choices(
                range(pins_left),
                weights=self.difficulty_weights_first_throw[difficulty][:pins_left],
            )[0]
        else:
            return pins_left
