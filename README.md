# Business Management App (In Progress)

<<<<<<< HEAD
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
=======
A modular Python-based productivity system designed to evolve into a full-scale business management SaaS platform.

---

## 🚀 Overview

This project began as a command-line task manager and has since evolved into a fully interactive desktop application using Tkinter and SQLite.

It is built with **scalability and system design in mind**, with the long-term goal of integrating task management, scheduling, and AI-powered business assistance into a unified platform.

---

## ✨ Features

### 📋 Task Management

* Create, edit, and delete tasks
* Mark tasks as complete/incomplete
* Priority levels (High, Medium, Low)
* Due date validation (prevents past dates)
* Overdue task detection
* Persistent storage using SQLite

---

### 🖥️ GUI System (Tkinter)

* Interactive task table (Treeview)
* Real-time search and filtering
* Column sorting with visual indicators (▲ ▼)
* Color-coded priorities
* Status feedback system

---

### 🔍 Advanced Filtering

* Keyword search (live)
* Filter by priority
* Filter by completion status
* Overdue-only filtering

---

### 📅 Calendar System (v6)

* Interactive monthly calendar view
* Month navigation with year transitions
* Real-time task synchronization
* Clickable days to view tasks
* Visual indicators:

  * 🔴 Overdue tasks
  * 🔵 Current day
  * 🔴/🟠/🟢 Priority-based coloring (High / Medium / Low)
* Intelligent color priority handling (overdue > today > task priority)

---

### 🕓 History Tracking

* Task activity logging:

  * Added, edited, deleted
  * Completed / uncompleted
* Timestamped records
* Reverse chronological display
* Paginated viewing (CLI)
>>>>>>> 422d1a2 (v6: Added interactive calendar system with real-time updates and priority-based visualization)

---

## 🧠 Architecture

<<<<<<< HEAD
The project follows a layered structure:

- **Modules Layer** → Database and core logic  
- **Services Layer** → Business logic and validation  
- **GUI Layer** → User interface  

This structure allows for easy expansion into future systems like calendars, APIs, and AI tools.
=======
This project follows a modular, layered architecture:

* **Modules Layer** → Database, history, and core utilities
* **Services Layer** → Business logic and validation
* **GUI Layer** → User interface and interaction

This separation improves:

* Maintainability
* Scalability
* Readability

…and prepares the system for future transition into a web-based application.
>>>>>>> 422d1a2 (v6: Added interactive calendar system with real-time updates and priority-based visualization)

---

## 📂 Project Structure
<<<<<<< HEAD
business-management-app/
│
├── data/ # Database and history files
├── modules/ # Core logic (database, tasks, history)
├── services/ # Business logic layer
├── gui.py # GUI application
├── main.py # CLI application
└── README.md
=======

```
business-management-app/
│
├── data/               # Database and history storage
├── modules/            # Core systems (database, calendar, history, etc.)
├── services/           # Business logic layer
├── gui.py              # Main GUI application
├── main.py             # CLI version
└── README.md
```
>>>>>>> 422d1a2 (v6: Added interactive calendar system with real-time updates and priority-based visualization)

---

## ▶️ How to Run

<<<<<<< HEAD
### CLI Version:
=======
### Run GUI Application

```
python gui.py
```

### Run CLI Version

```
>>>>>>> 422d1a2 (v6: Added interactive calendar system with real-time updates and priority-based visualization)
python main.py
```

<<<<<<< HEAD

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
=======
---

## 🔮 Future Roadmap

* 📅 Google Calendar integration (meetings & scheduling)
* 📧 Email integration and summarization
* 🤖 AI Business Assistant

  * Task suggestions
  * Email drafting
  * Workflow automation
* 🌐 Web-based application (Flask / FastAPI)
* ☁️ Cloud sync and multi-device support

---

## 🎯 Project Vision

To develop a unified business management system that combines:

* Task management
* Scheduling
* Communication tools
* AI-driven assistance

into a single, intelligent productivity platform.
>>>>>>> 422d1a2 (v6: Added interactive calendar system with real-time updates and priority-based visualization)

---

## 👤 Author

<<<<<<< HEAD
Rene M. Garcia Jr
=======
**Rene M. Garcia Jr**
>>>>>>> 422d1a2 (v6: Added interactive calendar system with real-time updates and priority-based visualization)
