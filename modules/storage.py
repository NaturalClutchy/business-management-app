import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "tasks.json")


def load_tasks():
    os.makedirs(os.path.join(BASE_DIR, "data"), exist_ok=True)
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks


def save_tasks(tasklist):
    with open(DATA_PATH, "w", encoding="utf-8") as file:
        json.dump(tasklist, file, indent=4)
