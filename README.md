# Software Engineering 1 - *Bowling Assignment*

Submitted by: **Ricardo Elizondo**


## Features

The following **features** are added:

- [ ] ****
- [ ] **Bowling Class calculates cumulative score and current/final score**
- [ ] **User throw by entering input manually**
- [ ] **Partial GUI Implementation(20%)**

The following **additional** features are implemented:

- [ ] User can play versus a machine with a defined difficulty.
- [ ] Up to as many players per game




## Notes
This project started with a simple method that accomplished the task, however I used this opportunity to practice my design patterns and object oriented abilities.
Classes Added:
Bowling: Creates an instance of a bowling game that take numbe of players as parameter

Abstract Class Player: Abstract class that defines the model for human, computer and test player.
Human Class: Allows user to input number of pins thrown per round
Computer Class: Gets a random selection for number of pins thrown based on controlled probability based on luck
player Test Class: Test predefined test cases 


## Libraries/Modules used:
PySimpleGUI
ABC 
random



## License

    Copyright [2023] [Ricardo Elizondo]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
