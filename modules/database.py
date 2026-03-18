import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "task.db")


def connect_db():
    return sqlite3.connect(DB_PATH)


def initialize_db():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS tasks (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT,
                   priority TEXT,
                   due_date TEXT,
                   completed INTEGER
                   )
                   """)

    conn.commit()
    conn.close()


def add_task_db(title, priority, due_date):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
                   INSERT INTO tasks (title, priority, due_date, completed)
                   VALUES (?, ?, ?, ?)
                   """, (title, priority, due_date, 0))

    conn.commit()
    conn.close()


def get_tasks_db():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    task = cursor.fetchall()
    conn.close()
    return task


def update_task_db(task_id, title, priority, due_date, completed):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
                   UPDATE tasks
                   SET title = ?, priority = ?, due_date = ?, completed = ?
                   WHERE id = ?
                   """, (title, priority, due_date, completed, task_id))
    conn.commit()
    conn.close()


def delete_task_db(task_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
