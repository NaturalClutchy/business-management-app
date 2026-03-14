

def load_tasks(tasklist):
    try:
        with open("task_list.txt", "r", encoding="utf-8") as file:
            for line in file:
                tasklist.append(line.strip())
    except FileNotFoundError:
        pass
    return tasklist


def log_history(action, task):
    try:
        with open("task_history.txt", "a", encoding="utf-8") as file:
            file.write(f"{action} - {task}\n")
    except Exception as e:
        print(f"Error logging history: {e}")


def save_task(tasklist):
    with open("task_list.txt", "w", encoding="utf-8") as file:
        for task in tasklist:
            file.write(f"{task}\n")


def add_task(tasklist):
    task = input("Enter the task you would like to add: ")
    tasklist.append(task)
    log_history("ADDED", task)
    print(f"Task '{task}' added to the list.")


def view_task(tasklist):
    if not tasklist:
        print("No tasks in the list.")
    else:
        print(" === Tasks in the list:")
        display_paginated(tasklist)


def delete_task(tasklist):
    if not tasklist:
        print("no task in the list.")
    else:
        view_task(tasklist)
        try:
            task_number = int(
                input("enter the number of which task you want to delete, or 0 to cancel: "))
            if task_number == 0:
                print("Task deletion cancelled.")
                return
            sure = input(
                f"are you sure you want to delete task {task_number}? (yes/no): ")
            if sure.lower() != 'yes':
                print("Task deletion cancelled.")
                return
            if 1 <= task_number <= len(tasklist):
                removed_task = tasklist.pop(task_number - 1)
                log_history("DELETED", removed_task)
                print(f"Task '{removed_task} ' has been deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def complete_task(tasklist):
    if not tasklist:
        print("No task in the list.")
        return

    view_task(tasklist)

    try:
        complete_task_number = int(
            input("enter the number of which task you want to complete, or 0 to cancel: "))
        if complete_task_number == 0:
            print("== Task completion cancelled. ==")
            return
        if 1 <= complete_task_number <= len(tasklist):
            if not tasklist[complete_task_number - 1].startswith("[✓] "):
                tasklist[complete_task_number - 1] = "[✓] " + \
                    tasklist[complete_task_number - 1]
                log_history("COMPLETED", tasklist[complete_task_number - 1])
                print(
                    f"Task '{tasklist[complete_task_number - 1]}' has been marked as completed.")
            else:
                print("Task is already marked as complete")
    except ValueError:
        print("Please enter a valid number.")


def revise_task(tasklist):
    if not (tasklist):
        print("== No tasks in the list. ==")
        return
    view_task(tasklist)
    try:
        task_number = int(
            input("enter the number of which task you want to revise, or 0 to cancel: "))
        if task_number == 0:
            print("== Task revision cancelled. ==")
            return
        if 1 <= task_number <= len(tasklist):
            new_task = input("enter the revised task: ")
            old_task = tasklist[task_number - 1]
            tasklist[task_number - 1] = new_task
            log_history("REVISED", old_task)
            print(
                f"Task '{old_task}' has been revised to '{new_task}'.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
        return


def edit_task(tasklist):
    if not tasklist:
        print("No tasks in the list.")
        return

    while True:
        print("======= Task Editor =======")
        print(" 1. Complete Task"
              "\n 2. Revise Task"
              "\n 3. Delete Task"
              "\n4. Cancel")
        task_choice = input("Enter your choice (1-4): ")
        if task_choice == "1":
            complete_task(tasklist)
        elif task_choice == "2":
            revise_task(tasklist)
        elif task_choice == "3":
            delete_task(tasklist)
        elif task_choice == "4":
            print("Task edit cancelled.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


def view_history():
    try:
        with open("task_history.txt", "r", encoding="utf-8") as file:
            history = file.readlines()
            if not history:
                print("No history available.")
                return

            display_paginated(history)
    except FileNotFoundError:
        print("No history available.")


def clear_history():
    try:
        with open("task_history.txt", "w", encoding="utf-8") as file:
            file.write("")
            print("Task history cleared.")
    except Exception as e:
        print(f"Error clearing history: {e}")


def clear_task():
    try:
        with open("task_list.txt", "w", encoding="utf-8") as file:
            file.write("")
            print("Task list cleared.")
    except Exception as e:
        print(f"Error clearing task list: {e}")


def display_paginated(items, items_per_page=5):
    for i in range(0, len(items), items_per_page):
        page = items[i:i + items_per_page]
        for index, item in enumerate(page, start=i + 1):
            print(f"{index}. {item.strip()}")
        if i + items_per_page < len(items):
            input(" === Press Enter to view the next page: ")


def main():
    tasklist = load_tasks([])
    while True:
        print("\n========= Task Manager =========")
        print("1. View Tasks"
              "\n2. Add Task"
              "\n3. Edit Task"
              "\n4. View History"
              "\n5. Save and Exit"
              )
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            view_task(tasklist)
        elif choice == "2":
            add_task(tasklist)
        elif choice == "3":
            edit_task(tasklist)
        elif choice == "4":
            view_history()
        elif choice == "5":
            save_task(tasklist)
            print("===   Tasks saved. Exiting...   ===")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
