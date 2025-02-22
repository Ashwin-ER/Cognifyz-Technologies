import os
from datetime import datetime


class Task:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed
        self.created_at = datetime.now()


class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.tasks = {}
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    for line in file:
                        try:
                            id, desc, completed = line.strip().split('|')
                            self.tasks[int(id)] = Task(int(id), desc, completed == 'True')
                        except ValueError as e:
                            print(f"Error parsing line: {line.strip()} - {e}")
        except IOError as e:
            print(f"Error loading tasks from file: {e}")

    def save_tasks(self):
        """Save tasks to file"""
        try:
            with open(self.filename, 'w') as file:
                for task in self.tasks.values():
                    file.write(f"{task.id}|{task.description}|{task.completed}\n")
        except IOError as e:
            print(f"Error saving tasks to file: {e}")

    def create_task(self, description):
        """Create a new task"""
        if not description:
            raise ValueError("Task description cannot be empty")

        id = max(self.tasks.keys(), default=0) + 1
        new_task = Task(id, description)
        self.tasks[id] = new_task
        self.save_tasks()
        return id

    def read_tasks(self):
        """Return all tasks"""
        return self.tasks

    def update_task(self, id, description=None, completed=None):
        """Update an existing task"""
        if id not in self.tasks:
            raise ValueError("Task not found")

        task = self.tasks[id]
        if description is not None:
            task.description = description
        if completed is not None:
            task.completed = completed
        self.save_tasks()
        return True

    def delete_task(self, id):
        """Delete a task"""
        if id not in self.tasks:
            raise ValueError("Task not found")

        del self.tasks[id]
        self.save_tasks()
        return True


def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        try:
            if choice == '1':
                desc = input("Enter task description: ")
                id = task_manager.create_task(desc)
                print(f"Task created with ID: {id}")

            elif choice == '2':
                tasks = task_manager.read_tasks()
                if not tasks:
                    print("No tasks found")
                else:
                    for task in tasks.values():
                        status = "✓" if task.completed else "✗"
                        print(f"ID: {task.id} | {task.description} | Completed: {status} | Created: {task.created_at}")

            elif choice == '3':
                id = int(input("Enter task ID to update: "))
                desc = input("Enter new description (press enter to skip): ")
                complete = input("Mark as completed? (y/n, press enter to skip): ")

                desc = desc if desc else None
                completed = True if complete.lower() == 'y' else False if complete.lower() == 'n' else None
                task_manager.update_task(id, desc, completed)
                print("Task updated successfully")

            elif choice == '4':
                id = int(input("Enter task ID to delete: "))
                task_manager.delete_task(id)
                print("Task deleted successfully")

            elif choice == '5':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
