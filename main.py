import bowling
import human_player
import player


def main():
    player_test = human_player.HumanPlayer("Rix")
    game = bowling.Bowling([player_test])
    game.start_game()


main()
