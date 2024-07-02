import os

def list_all_lists():
    files = [f for f in os.listdir() if f.endswith('.txt')]
    if not files:
        print("No existing lists found.")
    else:
        print("Existing lists:")
        for file in files:
            print(f" - {file[:-4]}")  

def load_tasks(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + "\n")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def add_task(tasks, filename):
    task = input("Enter the new task: ")
    tasks.append(task)
    save_tasks(tasks, filename)
    print("Task added successfully.")

def update_task(tasks, filename):
    list_tasks(tasks)
    task_number = int(input("Enter the task number to update: "))
    if 1 <= task_number <= len(tasks):
        new_task = input("Enter the new description of the task: ")
        tasks[task_number - 1] = new_task
        save_tasks(tasks, filename)
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def delete_task(tasks, filename):
    list_tasks(tasks)
    task_number = int(input("Enter the task number to delete: "))
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        save_tasks(tasks, filename)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def manage_list(list_name):
    filename = f"{list_name}.txt"
    tasks = load_tasks(filename)

    while True:
        print(f"\nManaging List: {list_name}")
        print("1. List all tasks")
        print("2. Add a new task")
        print("3. Update an existing task")
        print("4. Delete a task")
        print("5. Return to main menu")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks, filename)
        elif choice == "3":
            update_task(tasks, filename)
        elif choice == "4":
            delete_task(tasks, filename)
        elif choice == "5":
            break
        else:
            print("Invalid choice, please choose from 1-5.")

def main():
    while True:
        print("\nMain Menu")
        list_all_lists()
        print("1. Manage an existing list")
        print("2. Create a new list")
        print("3. Exit")

        main_choice = input("Enter your choice (1-3): ")

        if main_choice == "1":
            list_name = input("Enter the name of the list to manage: ")
            manage_list(list_name)
        elif main_choice == "2":
            list_name = input("Enter the name for the new list: ")
            manage_list(list_name)  
        elif main_choice == "3":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please choose from 1-3.")

if __name__ == "__main__":
    main()