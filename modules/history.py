import os
from datetime import datetime
from modules.pagination import display_paginated
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HISTORY_PATH = os.path.join(BASE_DIR, "data", "task_history.txt")
# Import datetime for logging history with timestamps


def log_history(action, task):
    os.makedirs("data", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(HISTORY_PATH, "a", encoding="utf-8") as file:
            file.write(f"{timestamp} | {action} | {task}\n")
    except Exception as e:
        print(f"Error logging history: {e}")


def history_menu():
    while True:
        print("\n=== History Menu ===")
        print("1. View History")
        print("2. Clear History")
        print("3. Back to Main Menu")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            try:
                with open(HISTORY_PATH, "r", encoding="utf-8") as file:
                    history = file.readlines()[::-1]
                    if not history:
                        print("No history available.")
                        return

                    display_paginated(history)
            except FileNotFoundError:
                print("No history available.")
        elif choice == "2":
            sure = input("Are you sure you want to clear history? (yes/no): ")
            if sure.lower() != "yes":
                print("History clearing cancelled.")
                return
            else:
                clear_history()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


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
