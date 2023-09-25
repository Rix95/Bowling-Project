import bowling
import human_player
import computer_player
import test_player


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
    test_subject = test_player.TestPlayer("Test Subject 12341", 2, "test")

    game = bowling.Bowling([test_subject])
    game.start_game()


main_test()
