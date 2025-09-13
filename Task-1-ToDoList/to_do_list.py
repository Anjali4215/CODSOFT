list_of_tasks = []

def view_tasks():
    if not list_of_tasks:
        print("Your to-do list is empty!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(list_of_tasks, start=1):
            print(f"{i}. {task['task']} - [{task['status']}]")

def add_task():
    new_task = input("Enter a new task: ").strip()
    if new_task:
        list_of_tasks.append({"task": new_task, "status": "Pending"})
        print(f"✅ Task '{new_task}' added successfully!")
    else:
        print("⚠ Task cannot be empty!")

def update_task():
    view_tasks()
    if not list_of_tasks:
        return
    try:
        task_num = int(input("Enter the task number to update: "))
        if 1 <= task_num <= len(list_of_tasks):
            replaced_task = input("Enter the updated task: ").strip()
            if replaced_task:
                old_task = list_of_tasks[task_num - 1]["task"]
                list_of_tasks[task_num - 1]["task"] = replaced_task
                print(f"🔄 '{old_task}' updated to '{replaced_task}'")
            else:
                print("⚠ Task cannot be empty!")
        else:
            print("⚠ Invalid task number")
    except ValueError:
        print("⚠ Please enter a valid number")

def delete_task():
    view_tasks()
    if not list_of_tasks:
        return
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(list_of_tasks):
            deleted_task = list_of_tasks.pop(task_num - 1)
            print(f"🗑 Task '{deleted_task['task']}' deleted successfully!")
        else:
            print("⚠ Invalid task number")
    except ValueError:
        print("⚠ Please enter a valid number")

def mark_completed():
    view_tasks()
    if not list_of_tasks:
        return
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(list_of_tasks):
            list_of_tasks[task_num - 1]["status"] = "Completed"
            print(f"✅ Task '{list_of_tasks[task_num - 1]['task']}' marked as Completed!")
        else:
            print("⚠ Invalid task number")
    except ValueError:
        print("⚠ Please enter a valid number")

def main():
    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            mark_completed()
        elif choice == "6":
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
