import bowling


def main():
    bowling_test = bowling.Bowling()
    bowling_test.start_game()

    while True:
        user_input = input("please throw something or press exit to exit.")
        if user_input == "exit":
            break
        else:
            bowling_test.throw(int(user_input))


main()
