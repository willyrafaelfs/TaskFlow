class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully!")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("\n--- Todo List ---")
            for i, task in enumerate(self.tasks, 1):
                status = "✓" if task["completed"] else " "
                print(f"{i}. [{status}] {task['task']}")
            print("-----------------\n")
    
    def mark_complete(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number-1]["completed"] = True
            print(f"Task {task_number} marked as complete!")
        else:
            print("Invalid task number.")
    
    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number-1)
            print(f"Task '{removed_task['task']}' deleted successfully!")
        else:
            print("Invalid task number.")
    
    def clear_all(self):
        self.tasks = []
        print("All tasks cleared!")

def main():
    todo_list = TodoList()
    
    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Clear All Tasks")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks()
            if todo_list.tasks:
                task_num = int(input("Enter task number to mark as complete: "))
                todo_list.mark_complete(task_num)
        elif choice == "4":
            todo_list.view_tasks()
            if todo_list.tasks:
                task_num = int(input("Enter task number to delete: "))
                todo_list.delete_task(task_num)
        elif choice == "5":
            confirm = input("Are you sure you want to clear all tasks? (y/n): ")
            if confirm.lower() == "y":
                todo_list.clear_all()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()