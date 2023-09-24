MAX_PINS = 10
MAX_ROUNDS = 10


class Bowling:
    def __init__(self, players):
        self.players = players
        self.round = 0

    def start_game(self):
        # for each player call playrond sequentially

        while self.round < MAX_ROUNDS:
            for player in self.players:
                self.play_round(player)
            self.round += 1

    def play_round(self, player):
        # check if the game is over
        # if is_game_over():
        #   return

        # Current implementation
        print("ROUND", self.round + 1, "of", MAX_ROUNDS)
        if player.type == "human":
            pins_left = MAX_PINS
            current_throw = "first"
            while pins_left > 0 and len(player.pins_thrown_per_round[self.round]) < 2:
                pins_thrown = player.throw(pins_left, current_throw)
                pins_left -= pins_thrown
                player.pins_thrown_per_round[self.round].append(pins_thrown)
                self.update_score(player, current_throw)

                if pins_left == 0:
                    self.adjust_bonuses(player, current_throw)
                    player.round_bonus[self.round] = (
                        "strike" if current_throw == "first" else "spare"
                    )
                else:
                    current_throw = "second"

                print("Your score is: ", player.score)
        # automatic TBD

        # test

    def round_status(self):
        if (
            sum(self.pins_thown_per_round[self.round]) == 10
            or len(self.pins_thown_per_round[self.round]) == 2
        ) and self.round < 9:  # ==2 or >1 ?
            self.round += 1
            self.current_throw = "first"
        elif self.current_throw == "first":
            self.current_throw = "second"
        else:  # for last round only
            self.current_throw = "third"

    def update_score(self, player, current_throw):
        points_to_add = 0
        cumulative = player.cumulative_round_score
        round_score = player.round_score
        round_bonus = player.round_bonus

        if current_throw == "first":
            if self.round >= 1 and round_bonus[self.round - 1] == "spare":
                points_to_add = player.round_score[self.round - 1] = (
                    10 + player.pins_thrown_per_round[self.round][0]
                )
                cumulative[self.round - 1] = points_to_add + cumulative[self.round - 2]

            elif self.round >= 2 and round_bonus[self.round - 2] == "strike":
                print("we cool?")
                points_to_add = player.round_score[self.round - 2] = (
                    20 + player.pins_thrown_per_round[self.round][0]
                )
                cumulative[self.round - 2] = points_to_add + cumulative[self.round - 3]
        else:  # <- second throw
            # add points if previous round is a strike
            if self.round >= 1 and round_bonus[self.round - 1] == "strike":
                points_to_add = player.round_score[self.round - 1] = 10 + sum(
                    player.pins_thrown_per_round[self.round]
                )
                cumulative[self.round - 1] = points_to_add + cumulative[self.round - 2]
            # add points with no bonus, add previous as long as round > 0
            else:
                points_to_add = player.round_score[self.round] = sum(
                    player.pins_thrown_per_round[self.round]
                )
                cumulative[self.round] = points_to_add + cumulative[self.round - 1]

        player.score = sum(player.round_score)
        print("//////////")
        print(
            self.round,
            current_throw,
            player.round_score,
            player.cumulative_round_score,
        )
        print("////////////")

    def adjust_bonuses(self, player, current_throw):
        player.round_bonus[self.round] = (
            "strike" if current_throw == "first" else "spare"
        )
