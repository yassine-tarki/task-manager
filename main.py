# Task Manager - a simple console application to manage daily tasks.
# Course: Collaborative Tools with Git / GitHub - Part 1

# The list that holds all the tasks.
# Each task is a dictionary, for example: {"title": "Review Python"}
# A task's number is its position in the list (the first task is number 1).
tasks = []


def show_menu():
    print()
    print("=== TASK MANAGER ===")
    print("1. Add a task   2. Display   3. Search   0. Exit")


def add_task():
    title = input("Task title: ").strip()
    if title == "":
        print("Error: the title cannot be empty.")
        return
    tasks.append({"title": title})
    print("Task added successfully.")


def display_tasks():
    if len(tasks) == 0:
        print("The task list is empty.")
        return
    print("--- Your tasks ---")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task['title']}")


def search_tasks():
    keyword = input("Keyword: ").strip()
    if keyword == "":
        print("Error: the keyword cannot be empty.")
        return
    found = False
    for number, task in enumerate(tasks, start=1):
        # Compare in lowercase so that "python" also finds "Python".
        if keyword.lower() in task["title"].lower():
            if not found:
                print("--- Tasks found ---")
            print(f"{number}. {task['title']}")
            found = True
    if not found:
        print(f'No task contains "{keyword}".')


def main():
    choice = ""
    while choice != "0":
        show_menu()
        choice = input("Your choice: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            search_tasks()
        elif choice == "0":
            print("Goodbye!")
        else:
            print("Error: invalid option. Please choose 1, 2, 3 or 0.")


main()
