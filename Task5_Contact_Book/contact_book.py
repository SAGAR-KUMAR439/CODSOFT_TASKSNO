print("===== CONTACT BOOK =====")

contacts = []

while True:
    print("\n===== MENU =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # Add Contact
    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        email = input("Enter email: ").strip()
        address = input("Enter address: ").strip()

        if name == "":
            print("Name cannot be empty.")
        else:
            contact = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }

            contacts.append(contact)
            print("Contact added successfully!")

    # View Contacts
    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            print("\n===== ALL CONTACTS =====")

            for index, contact in enumerate(contacts, start=1):
                print(f"\nContact {index}")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("Address:", contact["address"])

    # Search Contact
    elif choice == "3":
        search_name = input("Enter name to search: ").strip().lower()
        found = False

        for contact in contacts:
            if search_name in contact["name"].lower():
                print("\nContact Found!")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("Address:", contact["address"])
                found = True

        if not found:
            print("Contact not found.")

    # Update Contact
    elif choice == "4":
        search_name = input("Enter name to update: ").strip().lower()
        found = False

        for contact in contacts:
            if search_name == contact["name"].lower():
                print("\nEnter new details:")

                new_name = input("Enter name: ").strip()
                new_phone = input("Enter phone: ").strip()
                new_email = input("Enter email: ").strip()
                new_address = input("Enter address: ").strip()

                if new_name == "":
                    print("Name cannot be empty.")
                else:
                    contact["name"] = new_name
                    contact["phone"] = new_phone
                    contact["email"] = new_email
                    contact["address"] = new_address

                    print("Contact updated successfully!")

                found = True
                break

        if not found:
            print("Contact not found.")

    # Delete Contact
    elif choice == "5":
        search_name = input("Enter name to delete: ").strip().lower()
        found = False

        for contact in contacts:
            if search_name == contact["name"].lower():
                contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break

        if not found:
            print("Contact not found.")

    # Exit
    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice. Please select 1-6.")