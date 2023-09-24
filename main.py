import bowling
import human_player
import computer_player


def main():
    player_test = human_player.HumanPlayer("Rix")
    computer_player_test = computer_player.ComputerPlayer("Sans", "sans")
    game = bowling.Bowling([player_test, computer_player_test])
    game.start_game()


main()
