from player import Player


class HumanPlayer(Player):
    def __init__(self, name="John Doe", type="human"):
        super().__init__(name, type)

    def throw(self, pins_left, current_throw):
        # need validation future
        pins_thrown = int(input("How many pins did you knock down? "))
        print(
            "You knocked down",
            pins_thrown,
            "pins.",
            pins_left - pins_thrown,
            "pins left.",
        )
        if pins_thrown == pins_left:
            print("Strike" if current_throw == "first" else "Spare!")
        # add further print output for other scores... such as 0...8 etc...

        return pins_thrown
