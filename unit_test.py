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
    choice = int(input("Choice your test case from 1 to 4")) - 1

    test_subject = test_player.TestPlayer("Test Subject 12341", choice, "test")

    game = bowling.Bowling([test_subject])
    game.start_game()


main_test()
