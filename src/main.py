import os
import json

TODO_FILE = "todo_list.json"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def load_tasks():
    """Load tasks from a JSON file. Returns a list of dictionaries."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    """Save tasks as a structured JSON list."""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(task):
    """Add a new task with default status as incomplete."""
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})  # Store as dict
    save_tasks(tasks)
    print(f"Added: {task}")


def list_tasks(pause: bool = True):
    """Display all tasks with their status."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            checkbox = "[✔]" if task["completed"] else "[ ]"
            print(f"{i}. {checkbox} {task['task']}")

    if pause:
        input("\nPress Enter to continue...")


def remove_task(index):
    """Remove a task by index."""
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Removed: {removed['task']}")
    else:
        print("Invalid task number.")


def mark_task(index, complete=True):
    """Mark a task as complete or incomplete."""
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        tasks[index - 1]["completed"] = complete
        save_tasks(tasks)
        status = "completed" if complete else "incomplete"
        print(f"Marked as {status}: {tasks[index - 1]['task']}")
    else:
        print("Invalid task number.")


def edit_task(index, new_task):
    """Edit a task without changing its completion status."""
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        old_task = tasks[index - 1]["task"]
        tasks[index - 1]["task"] = new_task
        save_tasks(tasks)
        print(f"Edited: '{old_task}' → '{new_task}'")
    else:
        print("Invalid task number.")


def main():
    while True:
        clear_screen()
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Complete")
        print("5. Mark Task as Incomplete")
        print("6. Edit Task")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks(False)
            try:
                index = int(input("Enter task number to remove: "))
                remove_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            list_tasks(False)
            try:
                index = int(input("Enter task number to mark as complete: "))
                mark_task(index, complete=True)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            list_tasks(False)
            try:
                index = int(input("Enter task number to mark as incomplete: "))
                mark_task(index, complete=False)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "6":
            list_tasks(False)
            try:
                index = int(input("Enter task number to edit: "))
                new_task = input("Enter the new task description: ")
                edit_task(index, new_task)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
