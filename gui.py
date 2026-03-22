from tkinter import ttk
import tkinter as tk
import calendar
from datetime import datetime
from modules.history import HISTORY_PATH
from modules.database import get_tasks_db
from services.task_service import (create_task, get_filtered_tasks,
                                   complete_task as complete_task_service,
                                   delete_task as delete_task_service,
                                   edit_task as edit_task_service)
from modules.calendar_view import open_calendar


window = tk.Tk()
window.title("Task Manager")
window.geometry("700x800")

window.grid_columnconfigure(0, weight=4)
window.grid_columnconfigure(1, weight=2)
window.grid_rowconfigure(1, weight=1)

stats_label = tk.Label(window, text="", anchor="w", bg="#dcdcdc")
stats_label.grid(row=3, column=0, columnspan=2, sticky="ew")

sort_column = None
sort_reverse = False


def update_statistics(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t[4] == 1)
    pending = total - completed

    stats_text = f"Total: {total} | Completed: {completed} | {pending} Pending"
    stats_label.config(text=stats_text)


def open_history_window():
    history_window = tk.Toplevel(window)
    history_window.title("Task History")
    history_window.geometry("500x400")

    text = tk.Text(history_window)
    text.pack(fill="both", expand=True)

    try:
        with open(HISTORY_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()[::-1]
            for line in lines:
                text.insert(tk.END, line)
    except:
        text.insert(tk.END, "No history available.")


def add_task_gui():
    title = title_entry.get()
    priority = priority_var.get()
    due_date = due_date_entry.get()
    if not title:
        status_label.config(text="Title cannot be empty.", fg="red")
        return

    success, message = create_task(title, priority, due_date)

    if success:
        status_label.config(text=message, fg="black")
        title_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
        load_tasks()
    else:
        status_label.config(text=message, fg="red")

    if calendar_window:
        try:
            calendar_window.refresh_calendar()
        except:
            pass


def update_column_headers():
    for col in columns:
        if col == sort_column:
            arrow = "▼" if not sort_reverse else "▲"
            task_tree.heading(
                col, text=f"{col} {arrow}", command=lambda c=col: sort_tasks(c))
        else:
            task_tree.heading(
                col, text=col, command=lambda c=col: sort_tasks(c))


def refresh_tasks():
    global sort_column, sort_reverse

    sort_column = None
    sort_reverse = False

    update_column_headers()
    load_tasks()


def sort_tasks(column):
    global sort_column, sort_reverse
    if sort_column == column:
        sort_reverse = not sort_reverse
    else:
        sort_column = column
        sort_reverse = False
    update_column_headers()
    load_tasks()


def load_tasks():
    global sort_column, sort_reverse
    tasks = get_filtered_tasks(
        keyword=search_entry.get(),
        priority=filter_priority_var.get(),
        status=completed_var.get(),
        overdue_only=overdue_var.get()
    )
    tasks.sort(key=lambda t: (
        t[4], {"High": 0, "Medium": 1, "Low": 2}.get(t[2], 3),))

    if sort_column:
        col_index_map = {"ID": 0,
                         "Status": 4,
                         "Title": 1,
                         "Priority": 2,
                         "Due Date": 3
                         }

        index = col_index_map.get(sort_column)
        if index is not None:
            tasks.sort(key=lambda t: t[index], reverse=sort_reverse)

    for row in task_tree.get_children():
        task_tree.delete(row)
    for task in tasks:
        task_id, title, priority, due_date, completed = task
        if due_date != "None":
            try:
                due = datetime.strptime(due_date, "%Y-%m-%d")
                due_date_display = due.strftime("%m/%d/%Y")
            except:
                due_date_display = due_date
        else:
            due_date_display = "None"
        status = "[✓]" if completed else "[ ]"

        row_id = task_tree.insert("", "end", values=(
            task_id, status, title, priority, due_date_display))

        tags = []

        if priority == "High":
            tags.append("high")
        elif priority == "Medium":
            tags.append("medium")
        elif priority == "Low":
            tags.append("low",)

        if due_date != "None" and not completed:
            try:
                due = datetime.strptime(due_date, "%Y-%m-%d")
                if due.date() < datetime.now().date():
                    tags.append("overdue")
            except:
                pass
        task_tree.item(row_id, tags=tuple(tags))

    update_statistics(tasks)


def get_selected_task_id():
    selected = task_tree.selection()
    if not selected:
        return None
    item = task_tree.item(selected[0])
    task_id = item["values"][0]
    return task_id


def complete_task_gui():
    task_id = get_selected_task_id()
    if task_id is None:
        return
    success, message = complete_task_service(task_id)
    if success:
        status_label.config(text=message, fg="black")
        load_tasks()
    else:
        status_label.config(text=message, fg="red")

    if calendar_window:
        try:
            calendar_window.refresh_calendar()
        except:
            pass


def delete_task_gui():
    task_id = get_selected_task_id()
    if task_id is None:
        return
    success, message = delete_task_service(task_id)
    if success:
        status_label.config(text=message, fg="black")
        load_tasks()
    else:
        status_label.config(text=message, fg="red")

    if calendar_window:
        try:
            calendar_window.refresh_calendar()
        except:
            pass


def open_edit_window(event):
    task_id = get_selected_task_id()
    if task_id is None:
        return

    tasks = get_tasks_db()

    for task in tasks:
        if task[0] == task_id:
            selected_task = task
            break

    edit_window = tk.Toplevel(window)
    edit_window.title("Edit Task")
    edit_window.geometry("300x200")

    title_entry_edit = tk.Entry(edit_window, width=30)
    title_entry_edit.insert(0, selected_task[1])
    title_entry_edit.pack(pady=5)

    priority_var_edit = tk.StringVar(value=selected_task[2])
    priority_menu_edit = tk.OptionMenu(
        edit_window, priority_var_edit, "High", "Medium", "Low"
    )
    priority_menu_edit.pack(pady=5)

    due_date_entry_edit = tk.Entry(edit_window)
    due_date_entry_edit.insert(0, selected_task[3])
    due_date_entry_edit.pack(pady=5)

    def save_changes():
        success, message = edit_task_service(
            task_id,
            title_entry_edit.get(),
            priority_var_edit.get(),
            due_date_entry_edit.get(),
        )
        if success:
            status_label.config(text=message, fg="black")
            load_tasks()
            edit_window.destroy()
        else:
            status_label.config(text=message, fg="red")
        if not title_entry_edit.get():
            return
        if calendar_window:
            try:
                calendar_window.refresh_calendar()
            except:
                pass
        edit_window.destroy()

    save_button = tk.Button(edit_window, text="Save", command=save_changes)
    save_button.pack(pady=10)


def on_filter_change(event=None):
    load_tasks()


def clear_filters():
    search_entry.delete(0, tk.END)
    filter_priority_var.set("All")
    completed_var.set("All")
    overdue_var.set(False)
    load_tasks()


left_frame = tk.Frame(window)
left_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

right_frame = tk.Frame(window)
right_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

tk.Label(right_frame, text="").pack(pady=5)

filter_frame = tk.LabelFrame(right_frame, text="Filters")
filter_frame.pack(fill="x", pady=10, padx=5)

action_frame = tk.LabelFrame(right_frame, text="Actions")
action_frame.pack(fill="x", pady=10, padx=5)

add_frame = tk.LabelFrame(right_frame, text="Add Task")
add_frame.pack(fill="x", pady=10, padx=5)

label = tk.Label(window, text="Task Manager", font=("Arial", 18))
label.grid(row=0, column=0, columnspan=2, pady=10)

columns = ("ID", "Status", "Title", "Priority", "Due Date")
task_tree = ttk.Treeview(left_frame, columns=columns, show="headings")
for col in columns:
    task_tree.heading(col, text=col, command=lambda c=col: sort_tasks(c))
    task_tree.column(col, anchor="center")
task_tree.pack(fill="both", expand=True, padx=5, pady=5)

task_tree.tag_configure("high", foreground="red")
task_tree.tag_configure("medium", foreground="orange")
task_tree.tag_configure("low", foreground="green")
task_tree.tag_configure("overdue", background="#ffcccc")

task_tree.column("ID", width=40)
task_tree.column("Status", width=60)
task_tree.column("Title", width=180)
task_tree.column("Priority", width=80)
task_tree.column("Due Date", width=100)


tk.Label(add_frame, text="Title:").pack(anchor="w")
title_entry = tk.Entry(add_frame)
title_entry.pack(fill="x", pady=5)

tk.Label(filter_frame, text="Search: ").pack(anchor="w")
search_entry = tk.Entry(filter_frame)
search_entry.pack(pady=3, fill="x")
search_entry.bind("<KeyRelease>", on_filter_change)

filter_priority_var = tk.StringVar(value="All")
filter_priority_menu = tk.OptionMenu(
    filter_frame, filter_priority_var, "All", "High", "Medium", "Low"
)
filter_priority_menu.pack(fill="x")
filter_priority_var.trace_add("write", lambda *args: on_filter_change())

completed_var = tk.StringVar(value="All")
completed_menu = tk.OptionMenu(
    filter_frame, completed_var, "All", "Completed", "Incomplete"
)
completed_menu.pack(fill="x")
completed_var.trace_add("write", lambda *args: on_filter_change())

overdue_var = tk.BooleanVar()
tk.Checkbutton(filter_frame, text="Overdue Only", variable=overdue_var).pack()
overdue_var.trace_add("write", lambda *args: on_filter_change())

priority_var = tk.StringVar(value="Medium")
priority_menu = tk.OptionMenu(
    add_frame, priority_var, "High", "Medium", "Low")
priority_menu.pack(pady=3, fill="x")

tk.Label(add_frame, text="Due Date:").pack(anchor="w")
due_date_entry = tk.Entry(add_frame)
due_date_entry.pack(fill="x", pady=5)


task_tree.bind("<Double-Button-1>", open_edit_window)

add_button = tk.Button(add_frame, text="Add Task", command=add_task_gui)
add_button.pack(pady=5)


tk.Button(filter_frame, text="Clear Filters",
          command=clear_filters).pack(pady=5, fill="x")

tk.Button(action_frame, text="Complete Task",
          command=complete_task_gui).pack(fill="x", pady=4, ipady=3)
tk.Button(action_frame, text="Delete Task",
          command=delete_task_gui).pack(fill="x", pady=4, ipady=3)
tk.Button(action_frame, text="Refresh",
          command=refresh_tasks).pack(fill="x", pady=4, ipady=3)

tk.Button(action_frame, text="View History",
          command=open_history_window).pack(fill="x", pady=4)
calendar_window = None


def open_calendar_gui():
    global calendar_window
    calendar_window = open_calendar(window)


tk.Button(action_frame, text="View Calendar",
          command=open_calendar_gui).pack(fill="x", pady=4)
status_label = tk.Label(
    window,
    text="Ready",
    anchor="w",
    bg="#eaeaea"
)
status_label.grid(row=2, column=0, columnspan=2, pady=5)


status_label.grid(row=2, column=0, columnspan=2, sticky="ew")
load_tasks()
window.mainloop()
