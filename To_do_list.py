def display_menu():
    print("\n" + "=" * 25)
    print("      TO-DO LIST")
    print("=" * 25)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("=" * 25)

def main():
    # Dictionary inside a list to track task details (name & completion status)
    tasks = [] 
    
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        
        # 1. VIEW TASKS
        if choice == "1":
            if not tasks:
                print("\nYour to-do list is empty!")
            else:
                print("\n--- Current Tasks ---")
                for index, task in enumerate(tasks, 1):
                    status = "Done" if task["completed"] else "Pending"
                    print(f"{index}. {task['name']} [{status}]")
                    
        # 2. ADD TASK
        elif choice == "2":
            task_name = input("Enter the task description: ").strip()
            if task_name:
                tasks.append({"name": task_name, "completed": False})
                print(f"Added task: '{task_name}'")
            else:
                print("Task description cannot be empty.")
                
        # 3. MARK TASK AS COMPLETE
        elif choice == "3":
            if not tasks:
                print("\nNo tasks available to complete.")
                continue
                
            try:
                task_num = int(input("Enter task number to mark complete: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["completed"] = True
                    print(f" Task '{tasks[task_num - 1]['name']}' marked as complete!")
                else:
                    print(" Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        # 4. DELETE TASK
        elif choice == "4":
            if not tasks:
                print("\nNo tasks available to delete.")
                continue
                
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f" Removed task: '{removed['name']}'")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        # 5. EXIT
        elif choice == "5":
            print("\nGoodbye! Stay productive! ")
            break
            
        else:
            print(" Invalid entry. Please pick a number from 1 to 5.")

if __name__ == "__main__":
    main()
