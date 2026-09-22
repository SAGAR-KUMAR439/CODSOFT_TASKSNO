# Task 4 - Rock Paper Scissors

A simple command-line Rock Paper Scissors game developed in Python as part of the CodSoft Python Programming Internship.

## Features

- Player can choose Rock, Paper, or Scissors.
- Computer makes a random choice.
- Displays both player and computer choices.
- Determines the winner using standard game rules.
- Tracks the player's score.
- Tracks the computer's score.
- Handles invalid menu choices.
- Allows the player to exit the game.
- Displays the final score when exiting.

## How It Works

1. The player selects:
   - Rock
   - Paper
   - Scissors
   - Exit

2. The computer randomly selects one of the three choices.

3. The program compares both choices.

4. The result is displayed:
   - You Win
   - Computer Wins
   - It's a Tie

5. The score is updated after each round.

6. The game continues until the player selects Exit.

## Game Rules

| Player Choice | Beats |
|---|---|
| Rock | Scissors |
| Paper | Rock |
| Scissors | Paper |

If both the player and computer choose the same option, the result is a tie.

## Technologies Used

- Python
- `random` module
- Command Line Interface (CLI)

## How to Run

Open Command Prompt in the project directory and run:

```bash
python rock_paper_scissors.py