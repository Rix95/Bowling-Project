class Bowling:
    def __init__(self, players=1):
        self.players = players

    def start_game(self):
        self.score = 0
        self.pins_thown_per_round = []
        self.round_score = [0 for _ in range(10)]
        self.round_bonus = [None for _ in range(10)]
        self.round = 0
        # self.last_round_bonus = False
        # self.last_last_round_bonus = False

    def play_round(self):
        # check if the game is over
        # if is_game_over():
        #   return

        # manual
        first_throw = int(
            user_input("please make your first throw or press exit to exit.")
        )
        self.throw(first_throw, "first")

        if first_throw == 10:
            self.round_bonus[self.round] = "strike"
        else:
            second_throw = int(
                user_input("please make your second throw or press exit to exit.")
            )
            self.throw(second_throw, "second")
            if first_throw + second_throw == 10:
                self.round_bonus[self.round] = "spare"
        if self.get_round_pins() == 10:
            self.adjust_bonuses()

        # automatic TBD

        # test

    def throw(self, pins, current_throw):
        # if first thorw else second throw
        if current_throw == "first":
            self.pins_thown_per_round.append([pins])  # use getter here ?
        else:
            self.pins_thown_per_round[self.round].append(pins)

        self.update_score(current_throw)

        # self.round_status()
        # print(
        #     "pin tracker, ",
        #     self.pins_thown_per_round,
        #     "round score: ",
        #     self.round_score,
        #     " round: ",
        #     self.round,
        #     self.last_last_round_bonus,
        #     self.last_round_bonus,
        # )

    def get_round_pins(self):
        return sum(self.pins_thown_per_round[self.round])

    def get_bonus_at_round(self, round):  # self. or input?
        return self.round_bonus[round]

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

    def update_score(self, current_throw):
        if current_throw == "first":
            if self.round >= 1 and self.get_bonus_at_round(self.round - 1) == "spare":
                self.round_score[self.round - 1] = (
                    10
                    + self.pins_thown_per_round[self.round][0]
                    + self.round_score[self.round - 2]
                )
            elif (
                self.round >= 2 and self.get_bonus_at_round(self.round - 2) == "strike"
            ):
                self.round_score[self.round - 2] = (
                    20
                    + self.pins_thown_per_round[self.round][0]
                    + self.round_score[self.round - 3]
                )
        else:  # <- second throw
            # add points if previous round is a strike
            if self.round >= 1 and self.get_bonus_at_round(self.round - 1) == "strike":
                self.round_score[self.round - 1] = (
                    10
                    + sum(self.pins_thown_per_round[self.round])
                    + self.round_score[self.round - 2]
                )
            # add points with no bonus, add previous as long as round > 0
            else:
                self.round_score[self.round] = sum(
                    self.pins_thown_per_round[self.round]
                ) + (0 if self.round == 0 else self.round_score[self.round - 1])

        # if first and
        # if prev-2 strike
        # if prev-1 spare
        # if second
        # if prev-1 strike
        #  else add as basic :(

        # print(self.round, self.pins_thown_per_round)
        # two consecutive strikes
        # if self.round >= 2 and self.get_bonus_at_round(self.round - 2) == "strike":
        #     self.round_score[self.round - 2] = (
        #         20
        #         + self.pins_thown_per_round[self.round][0]
        #         + self.round_score[self.round - 3]
        #     )

        # if self.round >= 1 and (
        #     (
        #         self.get_bonus_at_round(self.round - 1) == "strike"
        #         and current_throw == "second"
        #     )
        #     or self.get_bonus_at_round(self.round - 1) == "spare"
        # ):
        #     self.round_score[self.round - 1] = (
        #         10
        #         + sum(self.pins_thown_per_round[self.round])
        #         + self.round_score[self.round - 2]
        #     )

        # self.round_score[self.round] = sum(self.pins_thown_per_round[self.round]) + (
        #     0 if self.round == 0 else self.round_score[self.round - 1]
        # )

    def adjust_bonuses(self, current_throw):
        self.round_bonus[self.round] = "strike" if current_throw == "first" else "spare"


bowling_test = Bowling()
while True:
    user_input = input("please throw something or press exit to exit.")
    if user_input == "exit":
        break
    else:
        bowling_test.throw(int(user_input))
