from modules.history import log_history
from modules.pagination import display_paginated
from modules.storage import save_tasks
from datetime import datetime


def is_overdue(due_date):
    if not due_date or due_date.lower() == "none":
        return False
    try:
        due = datetime.strptime(due_date, "%Y-%m-%d")
        today = datetime.today()
        return due.date() < today.date()
    except ValueError:
        return False


def sort_task(tasklist):
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    tasklist.sort(key=lambda task:  (
        task["completed"],
        priority_order.get(task["priority"].lower(), 4),
        task["due_date"]
    )
    )


def add_task(tasklist):
    title = input("Enter the task: ")
    priority = input("Enter the priority (High/Medium/Low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    task = {
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }
    tasklist.append(task)
    log_history("ADDED", title)
    print(f"Task '{title}' has been added to the list.")


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
                log_history("DELETED", removed_task["title"])
                print(f"Task '{removed_task['title']}' has been deleted.")
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
            task = tasklist[complete_task_number - 1]
            if not task["completed"]:
                task["completed"] = True
                log_history("COMPLETED", task["title"])
                print(
                    f"Task '{tasklist[complete_task_number - 1]['title']}' has been marked as completed.")
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
            return
        task = tasklist[task_number - 1]
        new_title = input(f"New title ({task['title']}): ") or task["title"]
        new_priority = input(
            f"New priority ({task['priority']}): ") or task["priority"]
        new_due_date = input(
            f"New due date ({task['due_date']}): ") or task["due_date"]
        task["title"] = new_title
        task["priority"] = new_priority
        task["due_date"] = new_due_date
        log_history("REVISED", new_title)
        print(f"Task updated.")
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


def view_task(tasklist):
    sort_task(tasklist)
    if not tasklist:
        print("No tasks in the list.")
        return
    formatted_task = []
    for task in tasklist:
        status = "[✓]" if task["completed"] else "[ ]"
        overdue = "⚠ OVERDUE " if is_overdue(task["due_date"]) else ""
        formatted_task.append(
            f"{status} {overdue}{task['title']} | Priority: {task['priority']} | Due: {task['due_date']}")
    display_paginated(formatted_task)


def clear_task(tasklist):
    confirm = input("Are you sure you want to clear all tasks? (yes/no): ")
    if confirm.lower() != "yes":
        print("Task clearing cancelled.")
        return
    tasklist.clear()
    save_tasks(tasklist)
    log_history("CLEARED", "All tasks cleared")
    print("All tasks have been cleared.")


def search_task(tasklist):
    keyword = input("Enter keyword to search: ").lower()
    results = []
    for task in tasklist:
        if keyword in task["title"].lower():
            results.append(task)
    if not results:
        print("No matching task found.")
        return
    formatted_results = []
    for task in results:
        status = "[✓]" if task["completed"] else "[ ]"
        formatted_results.append(
            f"{status} {task['title']} | Priority: {task['priority']} | Due: {task['due_date']}")
    display_paginated(formatted_results)


def task_statistics(tasklist):
    if not tasklist:
        print("\nNo task in the list")
        return
    total_task = len(tasklist)
    completed_task = sum(1 for task in tasklist if task["completed"])
    pending_task = total_task - completed_task
    overdue_task = sum(1 for task in tasklist if is_overdue(
        task["due_date"]) and not [task["completed"]])
    completion_rate = (completed_task / total_task) * \
        100 if total_task > 0 else 0

    print("\n=== Task Statistics ===")
    print(f"Total Tasks: {total_task}")
    print(f"Completed Tasks: {completed_task}")
    print(f"Pending Tasks: {pending_task}")
    print(f"Overdue Tasks: {overdue_task}")
    print(f"Completion Rate: {completion_rate:.1f}%)")
