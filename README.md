Business Management Application
Python task-management desktop app | Tkinter | SQLite
Status: In development

A modular productivity application built to make everyday task tracking easier. I developed both a command-line interface and a Tkinter desktop interface, backed by SQLite for persistent storage. The project is also a way for me to practice organizing software into separate interface, service, and data layers.
Current features
- Task management: Create, edit, delete, complete, and review tasks.
- Persistence: Store task data using SQLite rather than relying on a temporary in-memory list.
- Priority tracking: High, Medium, and Low priorities, with visual cues in the desktop interface.
- Search and filtering: Search tasks and filter by priority, completion status, and overdue status.
- Calendar: Navigate a monthly calendar to inspect dated tasks and deadlines.
- Activity history: Review timestamped changes to tasks.
- Two interfaces: Use either the command-line program or the Tkinter GUI.
Tech stack
Area	Technology
Programming language	Python
Desktop user interface	Tkinter / ttk
Data storage	SQLite (sqlite3)
Version control	Git and GitHub


Project structure
business-management-app/
├── gui.py            # Desktop application entry point
├── main.py           # Command-line interface
├── modules/          # Database, calendar and supporting modules
├── services/         # Task operations and business logic
└── data/             # Local task data
Running the application
1. Install Python 3.
2. Clone the repository and open the project folder:
   git clone https://github.com/NaturalClutchy/business-management-app.git
   cd business-management-app
3. To launch the desktop interface:
   python gui.py
4. To use the command-line interface instead:
   python main.py
   
Note: The application is a work in progress. Depending on your Python installation, Tkinter may need to be installed separately. If you're testing a development branch, verify its database schema before using an older local database file.
What I learned
- Designing create/read/update/delete (CRUD) workflows around persistent data.
- Separating user-interface behavior from task services and database logic.
- Building interactive filtering, calendar views, and state updates.
- Debugging changes across modules and maintaining a repository with Git.
Future directions
Potential additions include a web API, more robust recurring-task behavior, and optional AI-powered task assistance. These are plans, not currently shipped features.
Created by Rene Garcia · GitHub profile
