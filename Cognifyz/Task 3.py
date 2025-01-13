class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}, Completed: {self.completed}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self):
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Task '{title}' created successfully!\n")

    def read_tasks(self):
        if not self.tasks:
            print("No tasks available.\n")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
            print()

    def update_task(self):
        self.read_tasks()
        try:
            task_id = int(input("Enter the task number you want to update: ")) - 1
            if task_id < 0 or task_id >= len(self.tasks):
                print("Invalid task number.\n")
                return

            task = self.tasks[task_id]
            new_title = input(f"Enter new title (current: {task.title}): ")
            new_description = input(f"Enter new description (current: {task.description}): ")
            task.title = new_title
            task.description = new_description
            print(f"Task '{task_id + 1}' updated successfully!\n")
        except ValueError:
            print("Invalid input.\n")

    def delete_task(self):
        self.read_tasks()
        try:
            task_id = int(input("Enter the task number you want to delete: ")) - 1
            if task_id < 0 or task_id >= len(self.tasks):
                print("Invalid task number.\n")
                return

            removed_task = self.tasks.pop(task_id)
            print(f"Task '{removed_task.title}' deleted successfully!\n")
        except ValueError:
            print("Invalid input.\n")


def main():
    task_manager = TaskManager()

    while True:
        print("Task Manager:")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task_manager.create_task()
        elif choice == '2':
            task_manager.read_tasks()
        elif choice == '3':
            task_manager.update_task()
        elif choice == '4':
            task_manager.delete_task()
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1-5.\n")


if __name__ == "__main__":
    main()
