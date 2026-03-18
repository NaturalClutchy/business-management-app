from modules.tasks import (add_task,
                           view_task,
                           edit_task,
                           search_task,
                           task_statistics,
                           complete_task,
                           delete_task)
from modules.history import view_history
from modules.database import initialize_db


def main():
    initialize_db()
    try:
        while True:
            print("\n========= Task Manager =========")
            print("1. View Tasks"
                  "\n2. Add Task"
                  "\n3. Edit Task"
                  "\n4. Complete Task"
                  "\n5. Delete Task"
                  "\n6. View History"
                  "\n7. Search Tasks"
                  "\n8. Task Statistics"
                  "\n9. Exit"
                  )
            choice = input("Enter your choice (1-9): ")
            if choice == "1":
                view_task()
            elif choice == "2":
                add_task()
            elif choice == "3":
                edit_task()
            elif choice == "4":
                complete_task()
            elif choice == "5":
                delete_task()
            elif choice == "6":
                view_history()
            elif choice == "7":
                search_task()
            elif choice == "8":
                task_statistics()
            elif choice == "9":
                print("===   Exiting...   ===")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")
    except KeyboardInterrupt:
        print("\n=== Program Interrupted. Saving tasks and exiting... ===")


if __name__ == "__main__":
    main()
