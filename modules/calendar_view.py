import tkinter as tk
import calendar
from datetime import datetime
from modules.database import get_tasks_db


def open_calendar(parent,):
    cal_window = tk.Toplevel(parent)
    cal_window.title("Calendar")
    cal_window.geometry("400x400")

    current_date = datetime.now()
    current_year = current_date.year
    current_month = current_date.month

    def build_calendar(year, month):
        tasks = get_tasks_db()

        for widget in cal_window.winfo_children():
            if isinstance(widget, tk.Frame) or isinstance(widget, tk.Label):
                widget.destroy()

        cal = calendar.monthcalendar(year, month)

        task_days = {}
        overdue_days = set()
        today = datetime.now().date()
        for task in tasks:
            due_date = task[3]
            completed = task[4]
            if due_date != "None":
                try:
                    dt = datetime.strptime(due_date, "%Y-%m-%d")
                    if dt.year == year and dt.month == month:
                        existing = task_days.get(dt.day)
                        priority_order = {"High": 3, "Medium": 2, "Low": 1}
                        if not existing or priority_order[task[2]] > priority_order.get(existing, 0):
                            task_days[dt.day] = task[2]
                    if dt.year == year and dt.month == month:
                        if dt.date() < today and not completed:
                            overdue_days.add(dt.day)
                except:
                    pass

        nav_frame = tk.Frame(cal_window)
        nav_frame.pack(pady=5)

        def prev_month():
            nonlocal current_month, current_year

            current_month -= 1
            if current_month == 0:
                current_month = 12
                current_year -= 1
            build_calendar(current_year, current_month)

        def next_month():
            nonlocal current_month, current_year

            current_month += 1
            if current_month == 13:
                current_month = 1
                current_year += 1
            build_calendar(current_year, current_month)

        tk.Button(nav_frame, text="<", command=prev_month).pack(
            side="left", padx=10)
        tk.Button(nav_frame, text=">", command=next_month).pack(
            side="right", padx=10)

        header = tk.Label(
            cal_window, text=f"{calendar.month_name[month]} {year}", font=("Arial", 14))
        header.pack(pady=10)

        grid_frame = tk.Frame(cal_window)
        grid_frame.pack()

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        for col, day in enumerate(days):
            tk.Label(grid_frame, text=day, width=5).grid(
                row=0, column=col, padx=3, pady=3)

        for row_idx, week in enumerate(cal, start=1):
            for col_idx, day in enumerate(week):
                if day == 0:
                    tk.Label(grid_frame, text="").grid(
                        row=row_idx, column=col_idx)
                else:
                    bg_color = "SystemButtonFace"
                    if day in overdue_days:
                        bg_color = "#ff7f7f"
                    elif (day == current_date.day and month == current_date.month and year == current_date.year):
                        bg_color = "#7fbfff"
                    elif day in task_days:
                        priority = task_days[day]
                        if priority == "High":
                            bg_color = "#ffa6a6"
                        elif priority == "Medium":
                            bg_color = "#f5af4d"
                        elif priority == "Low":
                            bg_color = "#7fbf7f"
                        else:
                            bg_color = "SystemButtonFace"

                    btn = tk.Button(
                        grid_frame,
                        text=str(day),
                        width=5,
                        height=2,
                        bg=bg_color,
                        command=lambda d=day: show_tasks_for_day(
                            parent, tasks, year, month, d)
                    )
                    btn.grid(row=row_idx, column=col_idx)

    def refresh_calendar():
        build_calendar(current_year, current_month)

    cal_window.refresh_calendar = refresh_calendar

    build_calendar(current_year, current_month)
    return cal_window


def show_tasks_for_day(parent, tasks, year, month, day):
    selected_date = f"{year}-{month:02d}-{day:02d}"

    popup = tk.Toplevel(parent)
    popup.title(f"Tasks for {month}/{day}/{year}")
    popup.geometry("300x300")

    matching_tasks = []
    for task in tasks:
        if task[3] == selected_date:
            matching_tasks.append(task)

    if not matching_tasks:
        tk.Label(popup, text="No tasks for this day").pack(pady=10)
        return

    for task in matching_tasks:
        title = task[1]
        priority = task[2]
        completed = task[4]

        status = "✓" if completed else "✗"
        text = f"{status} {title} ({priority})"
        tk.Label(popup, text=text, anchor="w").pack(fill="x", padx=10, pady=2)
