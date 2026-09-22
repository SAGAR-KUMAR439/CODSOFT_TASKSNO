# Task 5 - Contact Book

A simple command-line Contact Book application developed in Python as part of the CodSoft Python Programming Internship.

## Features

- Add new contacts.
- View all saved contacts.
- Search contacts by name.
- Update existing contact details.
- Delete contacts.
- Store name, phone number, email, and address.
- Handles empty contact lists.
- Handles invalid menu choices.
- Provides a simple and user-friendly command-line interface.

## Contact Information

Each contact stores:

- Name
- Phone Number
- Email
- Address

## How It Works

The program displays a menu with six options:

1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit

The user selects an option and provides the required information.

Contacts are stored using Python dictionaries inside a list.

## Technologies Used

- Python
- Lists
- Dictionaries
- Loops
- Conditional Statements
- Command Line Interface (CLI)

## Error Handling

The program handles:

- Empty contact lists.
- Empty contact names.
- Invalid menu choices.
- Contact names that are not found.

## How to Run

Open Command Prompt in the project directory and run:

```bash
python contact_book.py