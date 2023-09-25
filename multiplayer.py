import bowling
import human_player
import computer_player


def multiplayer():
    n_of_players = int(input("Enter number of players: \n"))
    valid_players = []
    for i in range(n_of_players):
        choice = int(input("Choice 1 for human 2 for computer: \n"))
        if choice == 1:
            valid_players.append(human_player.HumanPlayer(input("Enter your name: ")))
        else:
            diff_setting = input(
                "Choose difficulty: easy, normal, hard, sans(not recomended)"
            )
            if diff_setting == "easy":
                ai_name = "Wall-E"
            elif diff_setting == "normal":
                ai_name = "ChatGPT"
            elif diff_setting == "hard":
                ai_name = "GLaDOS"
            else:
                ai_name = "Sans"
            valid_players.append(computer_player.ComputerPlayer(ai_name, diff_setting))

    # first_player = human_player.HumanPlayer(input("Enter your name: "))
    # second_player = human_player.HumanPlayer(input("Enter your name: "))

    # difficulty_ai = input(
    #     "Choose difficulty: easy, normal, hard, sans(not recomended): "
    # )

    # computer = computer_player.ComputerPlayer(ai_name, difficulty_ai)

    game = bowling.Bowling(valid_players)
    game.start_game()


multiplayer()
