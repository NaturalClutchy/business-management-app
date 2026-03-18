from modules.history import log_history
from modules.pagination import display_paginated
from modules.database import add_task_db, get_tasks_db, update_task_db, delete_task_db, connect_db
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


def sort_task(tasks):
    priority_order = {"High": 0, "Medium": 1, "Low": 2}
    return sorted(tasks, key=lambda t: (
        t[4],  # completed (0 first, 1 last)
        priority_order.get(t[2], 3),  # priority
        t[3]  # due_date
    ))


def add_task():
    title = input("Enter the task: ")
    priority = input("Enter the priority (High/Medium/Low): ")
    while True:
        due_date = input(
            "Enter due date (YYYY-MM-DD), or press enter for no due date: ")
        if due_date == "":
            due_date = "None"
            break
        if is_valid_due_date(due_date):
            break
        else:
            print("Invalid date. Cannot be in the past or wrong format.")

    log_history("ADDED", title)
    add_task_db(title, priority, due_date)
    print(f"Task '{title}' has been added to the list.")


def delete_task():
    display_tasks_simple()
    try:
        task_id = int(input("Enter task ID to delete, or 0 to cancel: "))
        if task_id == 0:
            return
        tasks = get_tasks_db()
        for task in tasks:
            if task[0] == task_id:
                title = task[1]
                confirm = input(
                    (f"Are you sure you want to delete task '{title}'? (yes/no): ")).lower()
                if confirm == "yes":
                    delete_task_db(task_id)
                    log_history("DELETED", title)
                    print("Task deleted.")
                else:
                    print("Deletion cancelled.")
                return
    except ValueError:
        print("Please enter a valid number.")


def complete_task():
    display_tasks_simple()
    try:
        task_id = int(
            input("enter the ID of which task you want to complete, or 0 to cancel: "))
        if task_id == 0:
            print("Cancelled.")
            return
        tasks = get_tasks_db()
        for task in tasks:
            if task[0] == task_id:
                if task[4] == 1:
                    print("Task is already marked as complete")
                    return
                title, priority, due_date, = task[1], task[2], task[3]
                update_task_db(task_id, title, priority, due_date, 1)
                print("Task marked as complete.")
                log_history("COMPLETED", title)
                return
    except ValueError:
        print("Invalid Input.")


def edit_task():
    display_tasks_simple()
    try:
        task_id = int(input("Enter task ID to edit:"))
        tasks = get_tasks_db()
        for task in tasks:
            if task[0] == task_id:

                current_title, current_priority, current_due = task[1], task[2], task[3]

                new_title = input(
                    f"New title ({current_title}): ") or current_title
                new_priority = input(
                    f"New priority ({current_priority}): ") or current_priority
                while True:
                    new_due = input(
                        f"New due date ({current_due}): ") or current_due
                    if new_due == "":
                        new_due = None
                        break
                    if is_valid_due_date(new_due):
                        break
                    else:
                        print("Invalid date. Cannot be in the past or wrong format.")

                update_task_db(task_id, new_title,
                               new_priority, new_due, task[4])
                log_history("EDITED", new_title)
                print("Task updated.")
                return
        print("Task ID not found")
    except ValueError:
        print("Invalid input.")


def get_all_task():
    return get_tasks_db()


def view_task():
    tasks = get_all_task()
    if not tasks:
        print("\nNo tasks available.")
        return
    tasks = sort_task(tasks)
    formatted_tasks = format_tasks(tasks)
    display_paginated(formatted_tasks)


def display_tasks_simple():

    tasks = get_tasks_db()

    if not tasks:
        print("No tasks available.")
        return
    print("\n=========== Your Task List ===========")
    for task in tasks:
        task_id, title, priority, due_date, completed = task
        status = "[✓]" if completed else "[ ]"

        print(f"{task_id}. {status} {title} | Priority: {priority} | Due: {due_date}")


def search_task():
    keyword = input("Enter keyword to search: ").lower()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT * FROM tasks
                   WHERE title LIKE ?
                   """, (f"%{keyword}%",))
    results = cursor.fetchall()
    conn.close()
    formatted = format_tasks(results)
    display_paginated(formatted)


def search_task():
    print("\n=== Advanced Search ===")

    keyword = input("Enter keyword (press enter to skip): ").lower()
    priority = input(
        "Enter priority (High/Medium/Low or enter to skip): ").lower()
    status = input(
        "Enter status (completed/pending or enter to skip): ").lower()
    overdue_only = input("Show only overdue tasks? (yes/no): ").lower()

    query = "SELECT * FROM tasks WHERE 1=1"
    params = []

    if keyword:
        query += " AND title LIKE ?"
        params.append(f"%{keyword}%")

    if priority:
        query += " AND LOWER(priority)= ?"
        params.append(priority.lower())

    if status == "completed":
        query += " AND completed = 1"
    elif status == "pending":
        query += " AND completed = 0"

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(query, params)
    results = cursor.fetchall()

    conn.close()

    if overdue_only == "yes":
        filtered = []
        for task in results:
            due_date = task[3]

            if due_date and due_date != "None":
                try:
                    due = datetime.strptime(due_date, "%Y-%m-%d")
                    if due.date() < datetime.today().date():
                        filtered.append(task)
                except ValueError:
                    continue
        results = filtered

    if not results:
        print("No matching tasks found.")
        return

    formatted = format_tasks(results)
    display_paginated(formatted)


def format_tasks(tasks):
    formatted = []
    for task in tasks:
        task_id, title, priority, due_date, completed = task
        status = "[✓]" if completed else "[ ]"
        formatted.append(
            f"{task_id}. {status} {title} | Priority: {priority} | Due: {due_date}")
    return formatted


def is_valid_due_date(date_str):
    if date_str.lower() == "none":
        return True
    try:
        due = datetime.strptime(date_str, "%Y-%m-%d")
        today = datetime.today()
        return due.date() >= today.date()
    except ValueError:
        return False


def task_statistics():
    tasks = get_tasks_db()
    if not tasks:
        print("\nNo task in the list")
        return
    total = len(tasks)
    completed = sum(1 for t in tasks if t[4] == 1)
    pending = total - completed
    overdue = sum(1 for t in tasks if is_overdue(t[3]) and t[4] == 0)

    completion_rate = (completed/total) * 100 if total else 0

    print("\n=== Task Statistics ===")
    print(f"Total Tasks: {total}")
    print(f"Completed Tasks: {completed}")
    print(f"Pending Tasks: {pending}")
    print(f"Overdue Tasks: {overdue}")
    print(f"Completion Rate: {completion_rate:.1f}%)")
