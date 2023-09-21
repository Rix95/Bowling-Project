class Bowling:
    def __init__(self, players=1):
        self.start_game()

    def start_game(self):
        self.score = 0
        self.pins_thown_per_round = []
        self.round_score = []
        self.round = 0
        self.throw = "first"
        self.last_round_bonus = False
        self.last_last_round_bonus = True

    def throw(self, pins):
        # check if the game is over
        if is_game_over():
            return

        # if first thorw else second throw
        if self.throw == "first":
            self.pins_thown_per_round.append([pins])
        else:
            self.pins_thown_per_round[self.round].append(pins)

        self.update_score()
        self.adjust_bonuses()
        self.round_status()

    def round_status(self):
        if (
            sum(self.pins_thown_per_round[self.round]) == 10
            or len(self.pins_thown_per_round[self.round]) == 2
        ):  # ==2 or >1 ?
            self.round += 1
            self.throw = "first"
        elif round != 9:
            self.throw = "second"
        else:  # last round
            pass

    def update_score(self):
        if self.last_round_bonus[self.round] == 10:
            if self.round > 1 and self.last_round_bonus:
                self.round_score[round - 2] = (
                    10 + self.throw[round][0] + self.throw[round][1]
                )
            if self.round > 2 and self.last_last_round_bonus:
                self.round_score[round - 1] = 20 + self.throw[round][0]
        elif self.throw == "second":
            self.round_score[round] = sum(self.throw[round])

    def adjust_bonuses(self):
        self.last_last_round_bonus, self.last_round_bonus = (
            self.last_round_bonus,
            sum(self.pins_thown_per_round[self.round]) == 10,
        )
