import time
import schedule
from plyer import notification
from datetime import datetime
import json
import os

# File to save tasks
TASK_FILE = 'tasks.json'

# A list to store tasks
tasks = []

# Load tasks from the file
def load_tasks():
    global tasks
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            tasks = json.load(file)
    else:
        tasks = []

# Save tasks to the file
def save_tasks():
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to add a new task
def add_task(task_name, deadline):
    task = {
        'task_name': task_name,
        'deadline': deadline,
    }
    tasks.append(task)
    save_tasks()
    print(f"Task '{task_name}' added with deadline: {deadline}")

# Function to remove a completed task
def remove_task(task_name):
    global tasks
    tasks = [task for task in tasks if task['task_name'] != task_name]
    save_tasks()
    print(f"Task '{task_name}' removed.")

# Function to check for upcoming tasks and send a reminder
def check_tasks():
    current_time = datetime.now()
    for task in tasks:
        task_deadline = datetime.strptime(task['deadline'], '%Y-%m-%d %H:%M')
        time_difference = task_deadline - current_time
        if 0 <= time_difference.total_seconds() <= 3600:  # Remind if the task is due within the next hour
            send_reminder(task['task_name'], task['deadline'])

# Function to send a desktop notification
def send_reminder(task_name, deadline):
    notification.notify(
        title=f"Task Reminder: {task_name}",
        message=f"Task '{task_name}' is due at {deadline}.",
        timeout=10
    )

# Function to display the task list
def display_tasks():
    if not tasks:
        print("No tasks available.")
        return
    
    print("\nTask List:")
    for task in tasks:
        print(f"Task: {task['task_name']} | Deadline: {task['deadline']}")
    print()

# Function to get user input and manage tasks
def task_manager():
    while True:
        print("\nTask Manager Menu:")
        print("1. Add a Task")
        print("2. Remove a Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task_name = input("Enter the task name: ")
            deadline = input("Enter the deadline (YYYY-MM-DD HH:MM format): ")
            add_task(task_name, deadline)

        elif choice == '2':
            task_name = input("Enter the task name to remove: ")
            remove_task(task_name)

        elif choice == '3':
            display_tasks()

        elif choice == '4':
            print("Exiting Task Manager.")
            break

        else:
            print("Invalid option. Please choose again.")

# Scheduling task reminders
schedule.every(5).minutes.do(check_tasks)  # Check for tasks every 5 minutes

# Main function to run the task manager and reminder system
if __name__ == "__main__":
    print("Welcome to Task Manager with Reminders!")
    
    # Load tasks from the file at the start
    load_tasks()
    
    task_manager()

    # Keep running the scheduler in the background
    while True:
        schedule.run_pending()
        time.sleep(1)
