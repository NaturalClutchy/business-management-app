from modules.database import add_task_db, get_tasks_db, update_task_db, delete_task_db, connect_db
from modules.history import log_history
from datetime import datetime


def create_task(title, priority, due_date):
    if not title:
        return False, "Title cannot be empty."
    if not priority:
        return False, "Priority must be selected."
    parsed_date = parse_date(due_date)
    if parsed_date is None:
        return False, "Invalid date format. Use MM/DD/YYYY."
    if parsed_date != "None":
        due = datetime.strptime(parsed_date, "%Y-%m-%d")
        if due.date() < datetime.today().date():
            return False, "Due date cannot be in the past."
    due_date = parsed_date

    add_task_db(title, priority, due_date)
    log_history("ADDED", title)

    return True, f"Task '{title}' added successfully."


def complete_task(task_id):
    tasks = get_tasks_db()
    for task in tasks:
        if task[0] == task_id:
            title, priority, due_date, completed = task[1], task[2], task[3], task[4]
            new_status = 0 if completed == 1 else 1
            update_task_db(task_id, title, priority, due_date, new_status)
            if new_status == 1:
                log_history("COMPLETED", title)
                return True, f"Task '{title}' marked as complete."
            else:
                log_history("UNCOMPLETED", title)
                return True, f"Task '{title}' marked as incomplete."
    return False, "Task ID not found."


def delete_task(task_id):
    tasks = get_tasks_db()
    for task in tasks:
        if task[0] == task_id:
            title = task[1]

            delete_task_db(task_id)
            log_history("DELETED", title)
            return True, f"Task '{title}' has been deleted."
    return False, "Task ID not found."


def edit_task(task_id, new_title, new_priority, new_due_date):
    tasks = get_tasks_db()
    for task in tasks:
        if task[0] == task_id:
            if not new_title:
                return False, "Title cannot be empty."
        if new_due_date:
            try:
                due = datetime.strptime(new_due_date, "%Y-%m-%d")
                if due.date() < datetime.today().date():
                    return False, "Due date cannot be in the past."
            except ValueError:
                return False, "Invalid date format. Use YYYY-MM-DD."
        else:
            new_due_date = "None"

        update_task_db(
            task_id,
            new_title,
            new_priority,
            new_due_date,
            task[4]
        )

        log_history("EDITED", new_title)
        return True, f"Task '{new_title}' has been updated."
    return False, "Task ID not found."


def get_filtered_tasks(keyword="", priority="All", status="All", overdue_only=False):
    tasks = get_tasks_db()
    filtered = []
    for task in tasks:
        task_id, title, task_priority, due_date, completed = task

        if keyword and keyword.lower() not in title.lower():
            continue
        if priority != "All" and task_priority != priority:
            continue

        if status == "Completed" and completed == 0:
            continue
        if status == "Incomplete" and completed == 1:
            continue

        if overdue_only:
            if due_date == "None":
                continue
            try:
                due = datetime.strptime(due_date, "%Y-%m-%d")
                if due >= datetime.today():
                    continue
            except:
                continue
        filtered.append(task)
    return filtered


def parse_date(date_str):
    if not date_str:
        return "None"
    try:
        parts = date_str.split("/")
        if len(parts) != 3:
            return "None"
        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])

        due = datetime(year, month, day)
        return due.strftime("%Y-%m-%d")
    except:
        return "None"
