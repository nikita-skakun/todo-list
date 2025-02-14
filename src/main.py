import os

todo_file = "todo_list.txt"

def load_tasks():
    if not os.path.exists(todo_file):
        return []
    with open(todo_file, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(todo_file, "w") as file:
        file.write("\n".join(tasks) + "\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Removed: {removed}")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Remove Task")
        print("4. Exit")
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
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
