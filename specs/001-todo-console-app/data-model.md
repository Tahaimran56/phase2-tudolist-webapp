# Data Model: Phase 1 Todo Console App

**Branch**: `001-todo-console-app` | **Date**: 2025-12-21

## Entities

### Task

Represents a single work item to be tracked by the user.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | `int` | Yes | Unique identifier, auto-incremented |
| `title` | `str` | Yes | Task title (1+ characters) |
| `description` | `str` | No | Optional task description (default: empty string) |
| `is_completed` | `bool` | Yes | Completion status (default: False) |

**Validation Rules**:
- `id`: Must be positive integer, assigned by system
- `title`: Must be non-empty string after whitespace strip
- `description`: Any string, including empty
- `is_completed`: Boolean only, no other states

**State Transitions**:
```
                    ┌──────────────┐
    [Create] ──────►│   Pending    │
                    │is_completed= │
                    │    False     │
                    └──────┬───────┘
                           │
                    [Mark Complete]
                           │
                           ▼
                    ┌──────────────┐
                    │   Complete   │
                    │is_completed= │
                    │    True      │
                    └──────────────┘
```

**Note**: Tasks cannot transition back from Complete to Pending in Phase 1 (no "uncomplete" operation per spec).

## Python Implementation Reference

```python
from dataclasses import dataclass, field

@dataclass
class Task:
    """
    Represents a single task in the todo application.

    Attributes:
        id: Unique identifier assigned by the system.
        title: Required task title.
        description: Optional task description.
        is_completed: Whether the task has been marked complete.
    """
    id: int
    title: str
    description: str = ""
    is_completed: bool = False
```

## Storage Model

### TaskStorage (In-Memory)

A simple list-based storage for Task objects.

| Aspect | Design |
|--------|--------|
| Structure | `list[Task]` |
| Ordering | Insertion order (creation sequence) |
| ID Generation | Counter incremented on each add |
| Lookup | Linear scan by ID |
| Persistence | None (session-scoped) |

**Operations**:
| Operation | Complexity | Notes |
|-----------|------------|-------|
| Add | O(1) | Append to list |
| List All | O(n) | Return copy of list |
| Get by ID | O(n) | Linear search |
| Update | O(n) | Find + modify |
| Delete | O(n) | Find + remove |
| Mark Complete | O(n) | Find + modify |

## Relationships

```
┌─────────────────────────────────────────────────────────────┐
│                      TodoManager                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  _tasks: list[Task]                                  │    │
│  │  _next_id: int = 1                                   │    │
│  └─────────────────────────────────────────────────────┘    │
│                           │                                  │
│                    manages                                   │
│                           │                                  │
│                           ▼                                  │
│            ┌──────────────────────────┐                     │
│            │         Task             │                     │
│            │ ─────────────────────    │                     │
│            │ id: int                  │                     │
│            │ title: str               │                     │
│            │ description: str         │                     │
│            │ is_completed: bool       │                     │
│            └──────────────────────────┘                     │
└─────────────────────────────────────────────────────────────┘
```

## Constraints & Invariants

1. **ID Uniqueness**: No two tasks can have the same ID within a session
2. **ID Immutability**: Task ID cannot be changed after creation
3. **Title Non-Empty**: Title must contain at least one non-whitespace character
4. **Status Binary**: Task is either Pending (False) or Complete (True)
5. **No Orphans**: All tasks exist only within TodoManager's list

## Example Data

```python
# After creating three tasks
tasks = [
    Task(id=1, title="Buy groceries", description="Milk, bread, eggs", is_completed=False),
    Task(id=2, title="Call dentist", description="", is_completed=True),
    Task(id=3, title="Finish report", description="Q4 summary", is_completed=False),
]
```
