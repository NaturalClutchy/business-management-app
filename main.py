from modules.tasks import add_task, view_task, edit_task
from modules.storage import load_tasks, save_task
from modules.history import view_history


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
