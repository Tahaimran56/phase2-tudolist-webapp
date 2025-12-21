# Research: Phase 1 Todo Console App

**Branch**: `001-todo-console-app` | **Date**: 2025-12-21

## Overview

This document captures research decisions for the Phase 1 Todo Console App. Since the technical direction was provided in the planning input and aligns with the project constitution, no external research was required. All decisions are documented below with rationale.

## Technology Decisions

### 1. Data Model: Python Dataclass

**Decision**: Use Python `dataclass` decorator for the Task model

**Rationale**:
- Built into Python 3.7+ (we require 3.12+)
- Automatic `__init__`, `__repr__`, `__eq__` generation
- Type hints are native and enforced
- Immutable option available via `frozen=True` if needed
- No external dependencies

**Alternatives Considered**:
| Alternative | Why Rejected |
|-------------|--------------|
| Plain class | More boilerplate, manual `__init__` |
| NamedTuple | Less flexible for mutable state |
| Pydantic | External dependency (violates constitution) |
| attrs | External dependency |

### 2. Task Identifier: Integer Auto-increment

**Decision**: Use simple integer IDs with auto-increment

**Rationale**:
- User input from planning suggested UUID, but integers are simpler for CLI selection
- Users type "1" not "a1b2c3d4-e5f6-..." to select tasks
- Sequential IDs are sufficient for single-session, single-user scope
- No collision concerns in in-memory storage

**Alternatives Considered**:
| Alternative | Why Rejected |
|-------------|--------------|
| UUID | Harder for users to type/select in CLI |
| Timestamp-based | Unnecessary complexity |
| Hash-based | Overkill for in-memory storage |

### 3. Storage: Python List

**Decision**: Use a Python list to store Task objects

**Rationale**:
- Simplest data structure for ordered collection
- Constitution requires standard Python data structures
- O(n) lookup is acceptable for <100 tasks
- No persistence requirement (Phase 1 scope)

**Alternatives Considered**:
| Alternative | Why Rejected |
|-------------|--------------|
| Dictionary by ID | Slight overkill, list is simpler |
| SQLite in-memory | External complexity not needed |
| JSON file | Persistence out of Phase 1 scope |

### 4. Business Logic: TodoManager Class

**Decision**: Single `TodoManager` class encapsulates all CRUD operations

**Rationale**:
- Clear single responsibility: manage tasks
- Testable in isolation from CLI
- Encapsulates storage implementation details
- Follows constitution's modularity principle

**Methods**:
- `add_task(title: str, description: str = "") -> Task`
- `list_tasks() -> list[Task]`
- `get_task(task_id: int) -> Task | None`
- `update_task(task_id: int, title: str) -> bool`
- `delete_task(task_id: int) -> bool`
- `complete_task(task_id: int) -> bool`

### 5. CLI Architecture: Main Loop Pattern

**Decision**: Simple while loop with numbered menu

**Rationale**:
- Matches requirement FR-001 (menu-driven interface)
- Easy to understand and maintain
- No framework dependencies
- User input handling via standard `input()`

**Menu Structure**:
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

### 6. Input Validation Strategy

**Decision**: Validate at CLI layer, TodoManager assumes valid input

**Rationale**:
- CLI is the system boundary per constitution
- Keeps TodoManager focused on business logic
- Error messages displayed to user immediately
- Empty title validation before calling manager

**Validation Rules**:
- Title: Must be non-empty string (1+ characters after strip)
- Menu selection: Must be valid integer 1-6
- Task selection: Must be valid existing task ID
- Description: Optional, can be empty

### 7. Output Formatting

**Decision**: Consistent format with headers and indicators

**Rationale**:
- Constitution UI/UX Standards require clear, consistent output
- Success messages prefixed with ✓
- Error messages prefixed with ✗
- Task list shows ID, status indicator, title, description

**Format Examples**:
```
✓ Task added successfully (ID: 1)
✗ Error: Title cannot be empty
```

```
=== Tasks ===
[1] [Pending] Buy groceries
    Description: Get milk and bread
[2] [Complete] Call dentist
```

## Conclusion

All technical decisions align with the project constitution:
- Python 3.12+ with standard library only
- Type-hinted dataclass and class structures
- Modular design with clear separation of concerns
- Input validation at system boundaries
- Consistent CLI output formatting

No unresolved items. Ready to proceed to Phase 1: Design & Contracts.
