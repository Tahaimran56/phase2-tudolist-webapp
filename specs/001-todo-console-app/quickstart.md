# Quickstart: Phase 1 Todo Console App

**Branch**: `001-todo-console-app` | **Date**: 2025-12-21

## Prerequisites

- Python 3.12 or higher
- No additional packages required (standard library only)

## Installation

```bash
# Clone the repository (if not already done)
git clone <repository-url>
cd todo

# Verify Python version
python --version  # Should show Python 3.12.x or higher
```

## Running the Application

```bash
# From the repository root
python -m src.cli.main
```

## Usage

### Main Menu

When you start the application, you'll see:

```
=== Todo App ===
1. Add Task
2. View Tasks
3. Mark Complete
4. Update Task
5. Delete Task
6. Exit

Select option:
```

### Adding a Task

1. Select option `1` from the menu
2. Enter a task title (required)
3. Enter a description (optional, press Enter to skip)

```
Select option: 1
Enter task title: Buy groceries
Enter description (optional): Milk, bread, eggs
✓ Task added successfully (ID: 1)
```

### Viewing Tasks

Select option `2` to see all tasks:

```
Select option: 2

=== Tasks ===
[1] [Pending] Buy groceries
    Description: Milk, bread, eggs
[2] [Complete] Call dentist
```

If no tasks exist:
```
Select option: 2
No tasks found.
```

### Marking a Task Complete

1. Select option `3` from the menu
2. Enter the task ID to mark complete

```
Select option: 3
Enter task ID to complete: 1
✓ Task marked as complete
```

### Updating a Task

1. Select option `4` from the menu
2. Enter the task ID to update
3. Enter the new title

```
Select option: 4
Enter task ID to update: 1
Enter new title: Buy groceries and snacks
✓ Task updated successfully
```

### Deleting a Task

1. Select option `5` from the menu
2. Enter the task ID to delete

```
Select option: 5
Enter task ID to delete: 2
✓ Task deleted successfully
```

### Exiting

Select option `6` to exit:

```
Select option: 6
Goodbye!
```

## Running Tests

```bash
# Install pytest (development only)
pip install pytest

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/unit/test_task.py
pytest tests/unit/test_todo_manager.py
pytest tests/integration/test_cli.py
```

## Project Structure

```
todo/
├── src/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py           # Task dataclass
│   ├── services/
│   │   ├── __init__.py
│   │   └── todo_manager.py   # Business logic
│   └── cli/
│       ├── __init__.py
│       └── main.py           # Entry point
├── tests/
│   ├── unit/
│   └── integration/
└── specs/
    └── 001-todo-console-app/
        ├── spec.md
        ├── plan.md
        └── ...
```

## Troubleshooting

### "Module not found" error

Ensure you're running from the repository root:
```bash
cd /path/to/todo
python -m src.cli.main
```

### Invalid input errors

- **Empty title**: Task titles must contain at least one character
- **Invalid option**: Enter a number 1-6 for menu selection
- **Task not found**: The task ID doesn't exist - use "View Tasks" to see valid IDs

## Limitations (Phase 1)

- **No persistence**: All tasks are lost when the application exits
- **Single user**: No authentication or multi-user support
- **No undo**: Deleted tasks cannot be recovered
- **No task prioritization**: Tasks displayed in creation order only
