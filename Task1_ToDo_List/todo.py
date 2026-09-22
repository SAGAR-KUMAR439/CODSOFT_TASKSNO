
tasks = []

print("===================================")
print("     TO-DO LIST APPLICATION")
print("===================================")

while True:
    print("\n===== MAIN MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # -----------------------------
    # 1. ADD TASK
    # -----------------------------
    if choice == "1":
        task = input("Enter your task: ").strip()

        if task:
            tasks.append({
                "title": task,
                "completed": False
            })

            print("Task added successfully!")
        else:
            print("Task cannot be empty.")

    # -----------------------------
    # 2. VIEW TASKS
    # -----------------------------
    elif choice == "2":
        print("\n===== YOUR TASKS =====")

        if not tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(tasks, start=1):

                if task["completed"]:
                    status = "Completed"
                else:
                    status = "Pending"

                print(
                    f"{index}. {task['title']} [{status}]"
                )

    # -----------------------------
    # 3. UPDATE TASK
    # -----------------------------
    elif choice == "3":

        if not tasks:
            print("No tasks available to update.")

        else:
            print("\n===== YOUR TASKS =====")

            for index, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{index}. {task['title']} [{status}]")

            try:
                task_number = int(
                    input("\nEnter the task number you want to update: ")
                )

                if 1 <= task_number <= len(tasks):

                    new_task = input(
                        "Enter the new task: "
                    ).strip()

                    if new_task:
                        tasks[task_number - 1]["title"] = new_task
                        print("Task updated successfully!")
                    else:
                        print("Task cannot be empty.")

                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    # -----------------------------
    # 4. DELETE TASK
    # -----------------------------
    elif choice == "4":

        if not tasks:
            print("No tasks available to delete.")

        else:
            print("\n===== YOUR TASKS =====")

            for index, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{index}. {task['title']} [{status}]")

            try:
                delete_number = int(
                    input("\nEnter the task number you want to delete: ")
                )

                if 1 <= delete_number <= len(tasks):

                    deleted_task = tasks.pop(
                        delete_number - 1
                    )

                    print(
                        f"Task '{deleted_task['title']}' "
                        "deleted successfully!"
                    )

                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    # -----------------------------
    # 5. MARK TASK COMPLETE
    # -----------------------------
    elif choice == "5":

        if not tasks:
            print("No tasks available.")

        else:
            print("\n===== YOUR TASKS =====")

            for index, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{index}. {task['title']} [{status}]")

            try:
                task_number = int(
                    input(
                        "\nEnter the task number to mark as complete: "
                    )
                )

                if 1 <= task_number <= len(tasks):

                    tasks[task_number - 1]["completed"] = True

                    print("Task marked as completed!")

                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    # -----------------------------
    # 6. EXIT
    # -----------------------------
    elif choice == "6":
        print("\nThank you for using To-Do List Application!")
        print("Goodbye!")
        break

    # -----------------------------
    # INVALID CHOICE
    # -----------------------------
    else:
        print(
            "Invalid choice. "
            "Please select a number from 1 to 6."
        )

