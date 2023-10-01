import bowling.bowling as bowling
import player.human_player as human_player
import player.computer_player as computer_player
import player.test_player as test_player


def main_test():
    # first_player = human_player.HumanPlayer(input("Enter your name: "))
    # second_player = human_player.HumanPlayer(input("Enter your name: "))

    # difficulty_ai = input(
    #     "Choose difficulty: easy, normal, hard, sans(not recomended): "
    # )
    # if difficulty_ai == "easy":
    #     ai_name = "Wall-E"
    # elif difficulty_ai == "normal":
    #     ai_name = "ChatGPT"
    # elif difficulty_ai == "hard":
    #     ai_name = "GLaDOS"
    # else:
    #     ai_name = "Sans"
    # computer = computer_player.ComputerPlayer(ai_name, difficulty_ai)
    choice = (
        int(
            input(
                "Choice a number to pick a test case from the following options: \n 1: All Zeroes \n 2: All Strikes \n 3: All Spares \n 4: Custom Unit Case: \n"
            )
        )
        - 1
    )
    name_of_test_case = ""
    if choice == 1:
        name_of_test_case = "Mr. Loser"
    elif choice == 2:
        name_of_test_case = "Ms. Striker"
    elif choice == 3:
        name_of_test_case = "Big Spare"
    else:
        name_of_test_case = "Mrs Unit Casey"

    test_subject = test_player.TestPlayer(name_of_test_case, choice, "test")

    game = bowling.Bowling([test_subject])
    game.start_game()


main_test()
