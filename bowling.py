class Bowling:
    def __init__(self, players=1):
        self.start_game()

    def start_game(self):
        self.score = 0
        self.pins_thown_per_round = []
        self.round_score = [0 for _ in range(10)]
        self.round = 0
        self.current_throw = "first"
        self.last_round_bonus = False
        self.last_last_round_bonus = False

    def throw(self, pins):
        # check if the game is over
        # if is_game_over():
        #   return

        # if first thorw else second throw
        if self.current_throw == "first":
            self.pins_thown_per_round.append([pins])
        else:
            self.pins_thown_per_round[self.round].append(pins)

        self.update_score()

        self.adjust_bonuses()

        self.round_status()
        print(
            "pin tracker, ",
            self.pins_thown_per_round,
            "round score: ",
            self.round_score,
            " round: ",
            self.round,
            self.last_last_round_bonus,
            self.last_round_bonus,
        )

    def round_status(self):
        if (
            sum(self.pins_thown_per_round[self.round]) == 10
            or len(self.pins_thown_per_round[self.round]) == 2
        ):  # ==2 or >1 ?
            self.round += 1
            self.current_throw = "first"
        else:
            self.current_throw = "second"

    def update_score(self):
        # print(self.round, self.pins_thown_per_round)
        # two consecutive strikes
        if self.round >= 2 and self.last_last_round_bonus:
            self.round_score[self.round - 2] = (
                20
                + self.pins_thown_per_round[self.round][0]
                + self.round_score[self.round - 3]
            )

        if self.round >= 1 and self.last_round_bonus:
            self.round_score[self.round - 1] = (
                10
                + sum(self.pins_thown_per_round[self.round])
                + self.round_score[self.round - 2]
            )

        self.round_score[self.round] = sum(self.pins_thown_per_round[self.round]) + (
            0 if self.round == 0 else self.round_score[self.round - 1]
        )

    def adjust_bonuses(self):
        self.last_last_round_bonus = False
        if self.current_throw == "first":
            if sum(self.pins_thown_per_round[self.round]) == 10:
                if self.last_round_bonus == True:
                    self.last_last_round_bonus = True
                self.last_round_bonus = True
            elif (
                len(self.pins_thown_per_round[self.round - 1]) == 2
            ):  # didnt throw all pins
                self.last_round_bonus = False
        else:  # second throw
            self.last_round_bonus = (
                True if sum(self.pins_thown_per_round[self.round]) == 10 else False
            )


bowling_test = Bowling()
while True:
    user_input = input("please throw something or press exit to exit.")
    if user_input == "exit":
        break
    else:
        bowling_test.throw(int(user_input))
