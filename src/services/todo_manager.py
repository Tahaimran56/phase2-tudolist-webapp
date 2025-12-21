"""
TodoManager service for the Todo application.

This module contains the TodoManager class that handles all CRUD operations
for tasks, including adding, viewing, updating, deleting, and completing tasks.
"""

from src.models.task import Task


class TodoManager:
    """
    Manages todo tasks with CRUD operations.

    This class encapsulates all business logic for task management,
    storing tasks in an in-memory list for the duration of the session.

    Attributes:
        _tasks: Internal list storing all Task objects.
        _next_id: Counter for generating unique task IDs.
    """

    def __init__(self) -> None:
        """Initialize the TodoManager with an empty task list."""
        self._tasks: list[Task] = []
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Create a new task with the given title and optional description.

        Args:
            title: The task title (must be non-empty after stripping whitespace).
            description: Optional task description (defaults to empty string).

        Returns:
            The created Task object with an assigned unique ID.

        Raises:
            ValueError: If title is empty or contains only whitespace.
        """
        stripped_title = title.strip()
        if not stripped_title:
            raise ValueError("Title cannot be empty")

        task = Task(
            id=self._next_id,
            title=stripped_title,
            description=description.strip(),
            is_completed=False,
        )
        self._tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self) -> list[Task]:
        """
        Get all tasks.

        Returns:
            A list of all Task objects (empty list if none exist).
        """
        return list(self._tasks)

    def get_task(self, task_id: int) -> Task | None:
        """
        Get a task by its ID.

        Args:
            task_id: The unique identifier of the task to retrieve.

        Returns:
            The Task object if found, None otherwise.
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def complete_task(self, task_id: int) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id: The unique identifier of the task to complete.

        Returns:
            True if the task was marked complete, False if task not found.
        """
        task = self.get_task(task_id)
        if task is None:
            return False
        task.is_completed = True
        return True

    def update_task(self, task_id: int, title: str) -> bool:
        """
        Update a task's title.

        Args:
            task_id: The unique identifier of the task to update.
            title: The new title (must be non-empty after stripping whitespace).

        Returns:
            True if the task was updated, False if task not found.

        Raises:
            ValueError: If title is empty or contains only whitespace.
        """
        stripped_title = title.strip()
        if not stripped_title:
            raise ValueError("Title cannot be empty")

        task = self.get_task(task_id)
        if task is None:
            return False
        task.title = stripped_title
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task.

        Args:
            task_id: The unique identifier of the task to delete.

        Returns:
            True if the task was deleted, False if task not found.
        """
        task = self.get_task(task_id)
        if task is None:
            return False
        self._tasks.remove(task)
        return True
