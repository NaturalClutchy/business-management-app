# Business Management App (In Progress)

A modular Python-based productivity system designed to evolve into a full business management application.

## 🚀 Overview

This project started as a CLI Task Manager and has been upgraded into a GUI-based application using Tkinter. It is being built with scalability in mind, allowing future expansion into features like calendars, scheduling systems, and AI-powered tools.

---

## ✨ Features

### Task Management
- Add, edit, delete tasks
- Mark tasks as complete
- Priority levels (High, Medium, Low)
- Due date support with validation
- Overdue task detection
- History View (With timestamps)

### GUI (Tkinter)
- Interactive interface with Treeview table
- Live search and filtering
- Sorting by columns (with indicators ▲ ▼)
- Color-coded priorities
- Status feedback system

### Filtering System
- Search by keyword
- Filter by priority
- Filter by completion status
- Overdue-only filter

### Data Management
- SQLite database integration
- Persistent task storage
- Clean CRUD operations

### History System
- Task activity logging with timestamps
- Paginated history viewing

---

## 🧠 Architecture

The project follows a layered structure:

- **Modules Layer** → Database and core logic  
- **Services Layer** → Business logic and validation  
- **GUI Layer** → User interface  

This structure allows for easy expansion into future systems like calendars, APIs, and AI tools.

---

## 📂 Project Structure
business-management-app/
│
├── data/ # Database and history files
├── modules/ # Core logic (database, tasks, history)
├── services/ # Business logic layer
├── gui.py # GUI application
├── main.py # CLI application
└── README.md

---

## ▶️ How to Run

### CLI Version:
python main.py


### GUI Version:
python gui.py

---

## 🔮 Future Plans

- 📅 Calendar system with task integration
- 🤖 AI-powered task and email assistance
- 📧 Email & meeting integration
- 🌐 Web-based application
- ☁️ Cloud sync and multi-device support

---

## 🎯 Goal

To build a scalable, real-world business management system while developing strong software engineering skills.

---

## 👤 Author

Rene M. Garcia Jr
