import os


def load_tasks(tasklist):
    os.makedirs("data", exist_ok=True)
    try:
        with open("data/task_list.txt", "r", encoding="utf-8") as file:
            for line in file:
                tasklist.append(line.strip())
    except FileNotFoundError:
        pass
    return tasklist


def save_task(tasklist):
    with open("data/task_list.txt", "w", encoding="utf-8") as file:
        for task in tasklist:
            file.write(f"{task}\n")
