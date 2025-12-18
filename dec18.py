import json
import os
# Simple Task Manager
TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"desc": description, "done": False})
    save_tasks(tasks)
    print("Task added.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        print(f"{idx}. [{status}] {task['desc']}")

def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task marked as complete.")
    else:
        print("Invalid task number.")


def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            desc = input("Task description: ")
            add_task(desc)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            idx = int(input("Task number to complete: ")) - 1
            complete_task(idx)
        elif choice == "4":
            list_tasks()
            idx = int(input("Task number to delete: ")) - 1
            delete_task(idx)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()