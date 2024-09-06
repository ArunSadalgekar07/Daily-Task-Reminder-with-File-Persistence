# Daily Task Reminder with File Persistence

A Python-based daily task reminder system that allows you to create, manage, and set reminders for tasks with deadlines. Tasks are stored in a JSON file so that they persist across script runs, and desktop notifications will remind you when tasks are due within the next hour.

## Features

- **Add Tasks**: Easily create daily tasks with names and deadlines.
- **Persistent Storage**: Tasks are saved in `tasks.json`, so your task list is retained even if the script is closed and reopened.
- **Daily Reminders**: The system checks for tasks that are due every 5 minutes and sends a desktop notification if a task is due within the next hour.
- **Task Management**: Display your task list, remove completed tasks, and manage your tasks efficiently.

## Requirements

- Python 3.x
- Libraries:
  - `schedule`
  - `plyer`
  
  Install the required libraries using:
  ```bash
  pip install schedule plyer
  ```

## How to Use

### 1. Clone the Repository:
```bash
git clone https://github.com/ArunSadalgekar07/Daily-Task-Reminder-with-File-Persistence.git
```
```bash
cd Daily-Task-Reminder-with-File-Persistence
```


### 2. Run the Script:
```bash
python tasks_script.py
```

### 3. Task Manager Menu:
The menu helps you manage daily tasks:
```
Task Manager Menu:
1. Add a Task
2. Remove a Task
3. Display Tasks
4. Exit
```

#### **Add a Task**:
- Enter the task name.
- Provide a deadline in the format `YYYY-MM-DD HH:MM`. For example:
  ```
  Task: Morning workout
  Deadline: 2024-09-06 08:00
  ```

#### **Remove a Task**:
- Enter the task name to remove it from the list.

#### **Display Tasks**:
- View your saved daily tasks with their deadlines.

#### **Exit**:
- Exit the task manager. All tasks are saved, so they will be available when you restart the script.

### 4. Desktop Notifications:
Every 5 minutes, the system checks for tasks due in the next hour. You’ll receive a desktop notification for any tasks that are approaching their deadline.

### Task Persistence:
Your tasks are saved to a JSON file (`tasks.json`) in the project directory. This file ensures that tasks persist between script runs.

Example `tasks.json` file:
```json
[
    {
        "task_name": "Morning workout",
        "deadline": "2024-09-06 08:00"
    },
    {
        "task_name": "Team meeting",
        "deadline": "2024-09-06 10:00"
    }
]
```


## Example Workflow

1. **Add a task**:
   ```
   Enter the task name: Morning workout
   Enter the deadline (YYYY-MM-DD HH:MM format): 2024-09-06 08:00
   ```

2. **Receive a notification** when a task is due within the next hour:
   ```
   Task Reminder: Morning workout
   Task 'Morning workout' is due at 2024-09-06 08:00.
   ```

3. **Tasks are saved** in the `tasks.json` file and reloaded the next time the script runs.
