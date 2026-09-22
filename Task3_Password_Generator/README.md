# Task 3 - Password Generator

A simple command-line password generator developed as part of the CodSoft Python Programming Internship.

## Features

- Allows the user to choose the desired password length
- Generates random passwords
- Uses letters, numbers, and special characters
- Handles invalid non-numeric input
- Validates password length
- User-friendly command-line interface

## How It Works

The program asks the user to enter the desired password length.

It then creates a random password using:

- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

The generated password is displayed on the screen.

## Technologies Used

- Python
- `random` module
- `string` module
- Command Line Interface (CLI)

## Error Handling

The program handles:

- Non-numeric input
- Zero or negative password length

## How to Run

Make sure Python is installed on your computer.

Run:

```bash
python password_generator.py