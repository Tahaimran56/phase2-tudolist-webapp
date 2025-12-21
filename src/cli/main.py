"""
CLI entry point for the Todo application.

This module provides the command-line interface for the Todo application,
including the main menu loop and user interaction handling.
"""

from src.services.todo_manager import TodoManager


def add_task(manager: TodoManager) -> None:
    """
    Handle the add task flow.

    Prompts the user for a title and optional description,
    then creates a new task via the manager.

    Args:
        manager: The TodoManager instance to use for task creation.
    """
    print("\n--- Add Task ---")
    title = input("Enter task title: ")
    description = input("Enter description (optional): ")

    try:
        task = manager.add_task(title, description)
        print(f"✓ Task added successfully (ID: {task.id})")
    except ValueError as e:
        print(f"✗ Error: {e}")


def view_tasks(manager: TodoManager) -> None:
    """
    Handle the view tasks flow.

    Displays all tasks with their ID, status, title, and description.

    Args:
        manager: The TodoManager instance to use for listing tasks.
    """
    print("\n--- Tasks ---")
    tasks = manager.list_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "Complete" if task.is_completed else "Pending"
        print(f"[{task.id}] [{status}] {task.title}")
        if task.description:
            print(f"    Description: {task.description}")


def mark_complete(manager: TodoManager) -> None:
    """
    Handle the mark complete flow.

    Shows current tasks, prompts for task ID, and marks the selected task complete.

    Args:
        manager: The TodoManager instance to use for completing tasks.
    """
    print("\n--- Mark Complete ---")
    tasks = manager.list_tasks()

    if not tasks:
        print("No tasks found.")
        return

    # Show current tasks for selection
    for task in tasks:
        status = "Complete" if task.is_completed else "Pending"
        print(f"[{task.id}] [{status}] {task.title}")

    try:
        task_id = int(input("\nEnter task ID to complete: "))
    except ValueError:
        print("✗ Error: Invalid input - please enter a number")
        return

    task = manager.get_task(task_id)
    if task is None:
        print("✗ Error: Task not found")
        return

    if task.is_completed:
        print("Task is already complete.")
        return

    if manager.complete_task(task_id):
        print("✓ Task marked as complete")
    else:
        print("✗ Error: Task not found")


def update_task(manager: TodoManager) -> None:
    """
    Handle the update task flow.

    Shows current tasks, prompts for task ID and new title, updates the task.

    Args:
        manager: The TodoManager instance to use for updating tasks.
    """
    print("\n--- Update Task ---")
    tasks = manager.list_tasks()

    if not tasks:
        print("No tasks to update.")
        return

    # Show current tasks for selection
    for task in tasks:
        status = "Complete" if task.is_completed else "Pending"
        print(f"[{task.id}] [{status}] {task.title}")

    try:
        task_id = int(input("\nEnter task ID to update: "))
    except ValueError:
        print("✗ Error: Invalid input - please enter a number")
        return

    if manager.get_task(task_id) is None:
        print("✗ Error: Task not found")
        return

    new_title = input("Enter new title: ")

    try:
        if manager.update_task(task_id, new_title):
            print("✓ Task updated successfully")
        else:
            print("✗ Error: Task not found")
    except ValueError as e:
        print(f"✗ Error: {e}")


def delete_task(manager: TodoManager) -> None:
    """
    Handle the delete task flow.

    Shows current tasks, prompts for task ID, and deletes the selected task.

    Args:
        manager: The TodoManager instance to use for deleting tasks.
    """
    print("\n--- Delete Task ---")
    tasks = manager.list_tasks()

    if not tasks:
        print("No tasks to delete.")
        return

    # Show current tasks for selection
    for task in tasks:
        status = "Complete" if task.is_completed else "Pending"
        print(f"[{task.id}] [{status}] {task.title}")

    try:
        task_id = int(input("\nEnter task ID to delete: "))
    except ValueError:
        print("✗ Error: Invalid input - please enter a number")
        return

    if manager.delete_task(task_id):
        print("✓ Task deleted successfully")
    else:
        print("✗ Error: Task not found")


def display_menu() -> None:
    """Display the main menu options to the user."""
    print("\n=== Todo App ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Complete")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")
    print()


def main() -> None:
    """
    Main entry point for the Todo application.

    Runs the main menu loop, handling user input and dispatching
    to the appropriate operations.
    """
    manager = TodoManager()

    while True:
        display_menu()
        choice = input("Select option: ")

        if choice == "1":
            add_task(manager)
        elif choice == "2":
            view_tasks(manager)
        elif choice == "3":
            mark_complete(manager)
        elif choice == "4":
            update_task(manager)
        elif choice == "5":
            delete_task(manager)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("✗ Error: Invalid option - please enter a number 1-6")


if __name__ == "__main__":
    main()
