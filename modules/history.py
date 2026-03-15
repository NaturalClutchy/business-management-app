import os
from modules.pagination import display_paginated
# Inport datetime for logging history with timestamps


def log_history(action, task):
    os.makedirs("data", exist_ok=True)
    try:
        with open("data/task_history.txt", "a", encoding="utf-8") as file:
            file.write(f"{action} - {task}\n")
    except Exception as e:
        print(f"Error logging history: {e}")


def view_history():
    try:
        with open("data/task_history.txt", "r", encoding="utf-8") as file:
            history = file.readlines()
            if not history:
                print("No history available.")
                return

            display_paginated(history)
    except FileNotFoundError:
        print("No history available.")


def clear_history():
    try:
        with open("data/task_history.txt", "w", encoding="utf-8") as file:
            file.write("")
            print("Task history cleared.")
    except Exception as e:
        print(f"Error clearing history: {e}")
