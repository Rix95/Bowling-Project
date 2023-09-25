#!/usr/bin/env python
"""
    Example of (almost) all Elements, that you can use in PySimpleGUI.
    Edited by Ricardo for project
    Copyright 2021, 2022, 2023 PySimpleGUI
"""

import PySimpleGUI as sg
import bowling.bowling as bowling
import player.human_player as human_player
import player.computer_player as computer_player


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


def make_window(theme):
    sg.theme(theme)

    # Table Data

    data = [[], []]
    headings = ["Name", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Score"]

    difficulty_setup = [
        # [sg.Menu(menu_def, key='-MENU-')],
    ]

    logging_layout = [
        # [sg.Output(size=(60,15), font='Courier 8', expand_x=True, expand_y=True)]
    ]

    bowling_layout = [
        [
            sg.Table(
                values=data,
                headings=headings,
                max_col_width=50,
                background_color="white",
                auto_size_columns=False,
                display_row_numbers=False,
                justification="right",
                num_rows=2,
                alternating_row_color="gray",
                key="-TABLE-",
                row_height=50,
            )
        ],
        [sg.Text("Choose your rival difficulty")],
        [
            sg.Radio("Easy", "Difficulty", default=True, size=(10, 1), k="-easy-"),
            sg.Radio("Normal", "Difficulty", default=True, size=(10, 1), k="-normal-"),
            sg.Radio("Hard", "Difficulty", default=True, size=(10, 1), k="-hard-"),
            sg.Radio(
                "Sans(Not recommended)",
                "Difficulty",
                default=True,
                size=(20, 2),
                k="-sans-",
            ),
        ],
        [
            sg.Button("Start Game"),
        ],
        [sg.Text("Anything printed will display here!")],
        [
            sg.Multiline(
                size=(60, 15),
                font="Courier 8",
                expand_x=True,
                expand_y=True,
                write_only=True,
                reroute_stdout=True,
                reroute_stderr=True,
                echo_stdout_stderr=True,
                autoscroll=True,
                auto_refresh=True,
            )
        ],
    ]

    layout = [
        [
            sg.Text(
                "Bowling Match",
                size=(38, 1),
                justification="center",
                font=("Helvetica", 16),
                relief=sg.RELIEF_RIDGE,
                k="-TEXT HEADING-",
                enable_events=True,
            )
        ],
    ]
    layout += [
        [
            sg.TabGroup(
                [
                    [
                        sg.Tab("Bowling Match", bowling_layout),
                        sg.Tab("Output", logging_layout),
                    ]
                ],
                key="-TAB GROUP-",
                expand_x=True,
                expand_y=True,
            ),
        ]
    ]
    layout[-1].append(sg.Sizegrip())
    window = sg.Window(
        "Bowling Demo",
        layout,
        grab_anywhere=True,
        resizable=True,
        margins=(0, 0),
        use_custom_titlebar=True,
        finalize=True,
        keep_on_top=True,
    )
    window.set_min_size(window.size)
    return window


def gui():
    window = make_window(sg.theme())
    first_player = human_player.HumanPlayer(input("Enter your name: "))
    computer_name = ""
    difficulty = "easy"
    game_start = False
    #
    # This is an Event Loop
    while True:
        event, values = window.read(timeout=100)

        # keep an animation running so show things are happening
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            print("============ Event = ", event, " ==============")
            print("-------- Values Dictionary (key=value) --------")
            for key in values:
                print(key, " = ", values[key])
        if event in (None, "Exit"):
            print("[LOG] Clicked Exit!")
            break

        elif event == "Start Game":
            if values["-easy-"]:
                computer_name = "Wall-E"
                difficulty = "easy"

            elif values["-normal-"]:
                computer_name = "ChatGPT"
                difficulty = "normal"

            elif values["-hard-"]:
                computer_name = "GLaDOS"
                difficulty = "hard"

            elif values["-sans-"]:
                computer_name = "Sans"
                difficulty = "sans"
            comp = computer_player.ComputerPlayer(computer_name, difficulty)
            game = bowling.Bowling(
                [
                    first_player,
                    comp,
                ]
            )

            game.start_game()
            # print("Game Started\n")
            game_start = True

        if game_start:
            data = [
                [first_player.name]
                + first_player.cumulative_round_score
                + [first_player.score],
                [comp.name] + comp.cumulative_round_score + [comp.score],
            ]
            window["-TABLE-"].update(values=data, select_rows=[0, 1])

    window.close()
    exit(0)


if __name__ == "__gui__":
    sg.theme("blue mono")
    gui()
