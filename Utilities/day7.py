"""
Challenge: Terminal-Based Task List Manager

Create a Python Script that lets user manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
    - Add a task
    -View all tasks
    - Mark a task as completed 
    - Delete a task
    - Exit the app
2. Save all tasks in a text file named 'tasks.txt' so data persists between runs.
3. Display tasks with an index number and a ✔️ if completed.

Example menu:
1. Add task 
2. View task
3. Mark Task as completed
4. Delete task
5. Exit

Example Output:
Your tasks:

Buy groceries || not_done
Finish Python Project || done
Read a book || not_done

Bonus:
- Prevent empty tasks from being added
- Validate task numbers before completing/deleting
"""

import os

TASK_FILE = "tasks.txt"


def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if " || " in line:
                    text, status = line.strip().rsplit(" || ", 1)
                    tasks.append({
                        "text": text,
                        "done": status == "done"
                    })
    return tasks


def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else "not_done"
            f.write(f"{task['text']} || {status}\n")


def display_tasks(tasks):
    if not tasks:
        print("NO TASKS FOUND")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            checkbox = "✔️" if task["done"] else " "
            print(f"{i}. [{checkbox}] {task['text']}")
    print()


def task_manager():
    tasks = load_tasks()

    while True:
        print("\n----- Task List Manager -----")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        match choice:
            case "1":
                text = input("Enter your task: ").strip()
                if text:
                    tasks.append({"text": text, "done": False})
                    save_tasks(tasks)
                    print("Task added successfully.")
                else:
                    print("Task cannot be empty!")

            case "2":
                display_tasks(tasks)

            case "3":
                if not tasks:
                    print("No tasks to complete.")
                    continue

                display_tasks(tasks)
                try:
                    num = int(input("Enter task number: "))
                    if 1 <= num <= len(tasks):
                        tasks[num - 1]["done"] = True
                        save_tasks(tasks)
                        print("Task marked as DONE.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

            case "4":
                if not tasks:
                    print("No tasks to delete.")
                    continue

                display_tasks(tasks)
                try:
                    num = int(input("Enter task number to delete: "))
                    if 1 <= num <= len(tasks):
                        tasks.pop(num - 1)
                        save_tasks(tasks)
                        print("Task removed successfully.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

            case "5":
                print("Exiting Task Manager. Goodbye!")
                break

            case _:
                print("Please choose a valid option (1-5).")


if __name__ == "__main__":
    task_manager()
