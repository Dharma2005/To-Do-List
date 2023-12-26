class Task:
    def __init__(self, title, description, status="Incomplete"):
        self.title = title
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        print("Tasks:")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task.title} - {task.description} ({task.status})")

    def mark_complete(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].status = "Complete"
            print("Task marked as complete.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nToDo List Application:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Complete")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            new_task = Task(title, description)
            todo_list.add_task(new_task)
            print("Task added successfully.")

        elif choice == "2":
            todo_list.display_tasks()

        elif choice == "3":
            task_index = int(input("Enter the task index to mark as complete: "))
            todo_list.mark_complete(task_index)

        elif choice == "4":
            print("Exiting ToDo List Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
