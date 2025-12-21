# Contracts: Phase 1 Todo Console App

**Branch**: `001-todo-console-app` | **Date**: 2025-12-21

## Status: Not Applicable

This feature is a standalone CLI application with no external API surface. Therefore, API contracts (OpenAPI, GraphQL schemas) are not applicable.

## Internal Interface Contract

While there's no external API, the internal interface between CLI and TodoManager is documented here for implementation guidance.

### TodoManager Interface

```python
class TodoManager:
    """Manages todo tasks with CRUD operations."""

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Create a new task.

        Args:
            title: Task title (must be non-empty)
            description: Optional task description

        Returns:
            The created Task object with assigned ID

        Raises:
            ValueError: If title is empty or whitespace-only
        """

    def list_tasks(self) -> list[Task]:
        """
        Get all tasks.

        Returns:
            List of all Task objects (empty list if none exist)
        """

    def get_task(self, task_id: int) -> Task | None:
        """
        Get a task by ID.

        Args:
            task_id: The task's unique identifier

        Returns:
            Task if found, None otherwise
        """

    def update_task(self, task_id: int, title: str) -> bool:
        """
        Update a task's title.

        Args:
            task_id: The task's unique identifier
            title: New title (must be non-empty)

        Returns:
            True if task was updated, False if task not found

        Raises:
            ValueError: If title is empty or whitespace-only
        """

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task.

        Args:
            task_id: The task's unique identifier

        Returns:
            True if task was deleted, False if task not found
        """

    def complete_task(self, task_id: int) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id: The task's unique identifier

        Returns:
            True if task was marked complete, False if task not found
        """
```

## Future Considerations

If a REST API is added in future phases, contracts should be generated in:
- `contracts/openapi.yaml` - OpenAPI 3.0 specification
- `contracts/schemas/` - Reusable schema definitions
