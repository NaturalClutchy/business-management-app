import os
from datetime import datetime
from modules.pagination import display_paginated
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HISTORY_PATH = os.path.join(BASE_DIR, "data", "task_history.txt")
# Import datetime for logging history with timestamps


def log_history(action, title):
    os.makedirs(os.path.dirname(HISTORY_PATH), exist_ok=True)

    with open(HISTORY_PATH, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {action}: {title}\n")


def view_history():
    try:
        with open(HISTORY_PATH, "r", encoding="utf-8") as file:
            history = file.readlines()[::-1]
        if not history:
            print("No history available.")
            return
        display_paginated(history)
    except FileNotFoundError:
        print("No history available.")


def clear_history():
    confirm = input("Clear all history? (yes/no): ")
    if confirm.lower() != "yes":
        print("History clearing cancelled.")
        return
    try:
        with open(HISTORY_PATH, "w", encoding="utf-8") as file:
            file.write("")
        print("History cleared.")
    except Exception as e:
        print(f"Error clearing history: {e}")
