
# Adding a Task

def add_task(task_list):
    task_title = input("Enter the task title: ")
    task_list.append({"title": task_title, "status": "Incomplete"})
    print("Task added successfully. ")

# View your tasks

def view_tasks(task_list):
    if not task_list:
        print("No tasks available. ")
    for index, task in enumerate(task_list):
        print(f"{index + 1}. {task['title']} - {task['status']}")


# Mark Complete

def mark_task_complete(task_list):
    view_tasks(task_list)
    try:
        task_number = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= task_number < len(task_list):
            task_list[task_number]["status"] = "complete"
            print("Task marked as complete. ")
        else:
            print("Invalid task number. ")
    
    except ValueError:
        print("Please enter a valid number. ")
    

# Delete

def delete_task(task_list):
    view_tasks(task_list)
    try:
        task_number = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_number < len(task_list):
            task_list.pop(task_number)
            print("Task deleted successfully. ")
        else:
            print("Invalid task number. ")
    except ValueError:
        print("Please enter a valid number. ")



# Handling Error
 
def get_user_choice():
    try:
        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        print("Invalid input. Please enter a number. ")
        return None


# Main Loop

def main():
    task_list = []
    while True:
        print("\nWelcome to the To-Do List App! ")
        print("Menu: ")
        print("1. Add a task ")
        print("2. View task ")
        print("3. Mark a task as complete ")
        print("4. Delete a task ")
        print("5. Quit ")

        choice = get_user_choice()
        if choice == 1:
            add_task(task_list)
        elif choice == 2:
            view_tasks(task_list)
        elif choice == 3:
            mark_task_complete(task_list)
        elif choice == 4:
            delete_task(task_list)
        elif choice == 5:
            print("Goodbye! ")
            break
        else:
            print("Please choose a valid option. ")

if __name__ == "__main__":
    main()