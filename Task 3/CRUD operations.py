class Task:
    def __init__(self, id, title, description, status="Pending"):
        self.id = id
        self.title = title
        self.description = description
        self.status = status


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create_task(self, title, description):
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task created successfully with ID: {task.id}")

    def read_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nTask List:")
        print("-" * 50)
        for task in self.tasks:
            print(f"ID: {task.id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Status: {task.status}")
            print("-" * 50)

    def update_task(self, task_id, title=None, description=None, status=None):
        for task in self.tasks:
            if task.id == task_id:
                if title:
                    task.title = title
                if description:
                    task.description = description
                if status:
                    task.status = status
                print(f"Task {task_id} updated successfully.")
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                print(f"Task {task_id} deleted successfully.")
                return
        print(f"Task with ID {task_id} not found.")


def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Create Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.create_task(title, description)

        elif choice == "2":
            manager.read_tasks()

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to update: "))
                title = input("Enter new title (press Enter to skip): ")
                description = input("Enter new description (press Enter to skip): ")
                status = input("Enter new status (press Enter to skip): ")

                manager.update_task(
                    task_id,
                    title if title else None,
                    description if description else None,
                    status if status else None
                )
            except ValueError:
                print("Please enter a valid task ID.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID.")

        elif choice == "5":
            print("Thank you for using Task Manager!")
            break

        else:
            print("Invalid choice. Please try again.")


# Test scenarios
def test_application():
    manager = TaskManager()

    # Test Case 1: Create tasks
    print("Test Case 1: Creating tasks")
    manager.create_task("Buy groceries", "Milk, bread, eggs")
    manager.create_task("Finish report", "Complete quarterly report")
    manager.read_tasks()

    # Test Case 2: Update task
    print("\nTest Case 2: Updating task")
    manager.update_task(1, status="Completed")
    manager.read_tasks()

    # Test Case 3: Delete task
    print("\nTest Case 3: Deleting task")
    manager.delete_task(2)
    manager.read_tasks()

    # Test Case 4: Try to update/delete non-existent task
    print("\nTest Case 4: Attempting invalid operations")
    manager.update_task(999, title="Test")
    manager.delete_task(999)


if __name__ == "__main__":
    print("Running interactive mode...")
    main()

    # Uncomment the following line to run test scenarios instead
    # test_application()
