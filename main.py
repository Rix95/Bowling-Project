import bowling
import human_player
import computer_player


def main():
    first_player = human_player.HumanPlayer(input("Enter your name: "))
    second_player = human_player.HumanPlayer(input("Enter your name: "))

    difficulty_ai = input(
        "Choose difficulty: easy, normal, hard, sans(not recomended): "
    )
    if difficulty_ai == "easy":
        ai_name = "Wall-E"
    elif difficulty_ai == "normal":
        ai_name = "ChatGPT"
    elif difficulty_ai == "hard":
        ai_name = "GLaDOS"
    else:
        ai_name = "Sans"

    computer = computer_player.ComputerPlayer(ai_name, difficulty_ai)
    game = bowling.Bowling([first_player, second_player, computer])
    game.start_game()


main()
