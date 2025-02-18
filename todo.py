tasks = []


def show_tasks():
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print("Task added!")


def remove_task():
    show_tasks()
    try:
        task_num = int(input("\nEnter the task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed = tasks.pop(task_num)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\nOptions: 1. View Tasks  2. Add Task  3. Remove Task  4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")