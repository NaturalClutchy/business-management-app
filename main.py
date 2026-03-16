from modules.tasks import add_task, view_task, edit_task, search_task, task_statistics
from modules.storage import load_tasks, save_tasks
from modules.history import history_menu


def main():
    tasklist = load_tasks()
    try:
        while True:
            print("\n========= Task Manager =========")
            print("1. View Tasks"
                  "\n2. Add Task"
                  "\n3. Edit Task"
                  "\n4. History Menu"
                  "\n5. Search Tasks"
                  "\n6. Task Statistics"
                  "\n7. Save and Exit"
                  )
            choice = input("Enter your choice (1-7): ")
            if choice == "1":
                view_task(tasklist)
            elif choice == "2":
                add_task(tasklist)
            elif choice == "3":
                edit_task(tasklist)
            elif choice == "4":
                history_menu()
            elif choice == "5":
                search_task(tasklist)
            elif choice == "6":
                task_statistics(tasklist)
            elif choice == "7":
                save_tasks(tasklist)
                print("===   Tasks saved. Exiting...   ===")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
    except KeyboardInterrupt:
        print("\n=== Program Interrupted. Saving tasks and exiting... ===")
        save_tasks(tasklist)


if __name__ == "__main__":
    main()
