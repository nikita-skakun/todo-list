import os

todo_file = "todo_list.txt"

def load_tasks():
    """Load tasks from file. Each task is stored as 'status|task' (0 = incomplete, 1 = complete)."""
    if not os.path.exists(todo_file):
        return []
    with open(todo_file, "r") as file:
        return [line.strip().split("|", 1) for line in file.readlines()]

def save_tasks(tasks):
    """Save tasks to file in the format 'status|task'."""
    with open(todo_file, "w") as file:
        file.writelines(f"{status}|{task}\n" for status, task in tasks)

def add_task(task):
    """Add a new task as incomplete (status = 0)."""
    tasks = load_tasks()
    tasks.append(["0", task])  # 0 means incomplete
    save_tasks(tasks)
    print(f"Added: {task}")

def list_tasks():
    """List all tasks with completion status."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for i, (status, task) in enumerate(tasks, 1):
            checkbox = "[✔]" if status == "1" else "[ ]"
            print(f"{i}. {checkbox} {task}")

def remove_task(index):
    """Remove a task by its index."""
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Removed: {removed[1]}")
    else:
        print("Invalid task number.")

def mark_task(index, complete=True):
    """Mark a task as complete (✔) or incomplete ([ ])."""
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        tasks[index - 1][0] = "1" if complete else "0"
        save_tasks(tasks)
        status = "completed" if complete else "incomplete"
        print(f"Marked as {status}: {tasks[index - 1][1]}")
    else:
        print("Invalid task number.")

def edit_task(index, new_task):
    """Edit an existing task without changing its completion status."""
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        old_task = tasks[index - 1][1]
        tasks[index - 1][1] = new_task
        save_tasks(tasks)
        print(f"Edited: '{old_task}' → '{new_task}'")
    else:
        print("Invalid task number.")

def main():
    while True:
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
            list_tasks()
            try:
                index = int(input("Enter task number to remove: "))
                remove_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            list_tasks()
            try:
                index = int(input("Enter task number to mark as complete: "))
                mark_task(index, complete=True)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            list_tasks()
            try:
                index = int(input("Enter task number to mark as incomplete: "))
                mark_task(index, complete=False)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "6":
            list_tasks()
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
