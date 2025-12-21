# Tasks: Phase 1 Todo Console App

**Input**: Design documents from `/specs/001-todo-console-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md

**Tests**: Tests are NOT explicitly requested in the feature specification. Test tasks are omitted.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4, US5)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below follow the plan.md structure

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directory structure: src/, src/models/, src/services/, src/cli/, tests/
- [x] T002 [P] Create package markers: src/__init__.py, src/models/__init__.py, src/services/__init__.py, src/cli/__init__.py
- [x] T003 [P] Create tests package markers: tests/__init__.py, tests/unit/__init__.py, tests/integration/__init__.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Create Task dataclass with id, title, description, is_completed fields in src/models/task.py
- [x] T005 Create TodoManager class skeleton with _tasks list and _next_id counter in src/services/todo_manager.py
- [x] T006 Create CLI main.py skeleton with main() function and menu display in src/cli/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks with title and optional description

**Independent Test**: Launch app, select "Add Task", enter title and description, verify task appears in list with "Pending" status

### Implementation for User Story 1

- [x] T007 [US1] Implement TodoManager.add_task(title, description) method in src/services/todo_manager.py
- [x] T008 [US1] Add title validation (non-empty after strip) with ValueError in src/services/todo_manager.py
- [x] T009 [US1] Implement CLI add_task flow: prompt for title, prompt for description, call manager in src/cli/main.py
- [x] T010 [US1] Add success message display after task creation in src/cli/main.py
- [x] T011 [US1] Add error message display for empty title validation in src/cli/main.py

**Checkpoint**: User Story 1 complete - users can add tasks with title and description

---

## Phase 4: User Story 2 - View All Tasks (Priority: P2)

**Goal**: Enable users to view all tasks with their status

**Independent Test**: Add tasks, select "View Tasks", verify all tasks displayed with ID, title, description, and status

### Implementation for User Story 2

- [x] T012 [US2] Implement TodoManager.list_tasks() method returning list[Task] in src/services/todo_manager.py
- [x] T013 [US2] Implement CLI view_tasks flow: call manager, format and display each task in src/cli/main.py
- [x] T014 [US2] Add empty list handling with "No tasks found" message in src/cli/main.py
- [x] T015 [US2] Format task display: [ID] [Status] Title + Description in src/cli/main.py

**Checkpoint**: User Stories 1 AND 2 complete - users can add and view tasks

---

## Phase 5: User Story 3 - Mark Task Complete (Priority: P3)

**Goal**: Enable users to mark pending tasks as complete

**Independent Test**: Add a task, select "Mark Complete", choose the task, verify status changes to "Complete"

### Implementation for User Story 3

- [x] T016 [US3] Implement TodoManager.get_task(task_id) method returning Task | None in src/services/todo_manager.py
- [x] T017 [US3] Implement TodoManager.complete_task(task_id) method returning bool in src/services/todo_manager.py
- [x] T018 [US3] Implement CLI mark_complete flow: show tasks, prompt for ID, call manager in src/cli/main.py
- [x] T019 [US3] Add handling for already-complete tasks with appropriate message in src/cli/main.py
- [x] T020 [US3] Add handling for task not found with error message in src/cli/main.py

**Checkpoint**: User Stories 1, 2, AND 3 complete - users can add, view, and complete tasks

---

## Phase 6: User Story 4 - Update Task (Priority: P4)

**Goal**: Enable users to update task titles

**Independent Test**: Add a task, select "Update Task", enter new title, verify title changed

### Implementation for User Story 4

- [x] T021 [US4] Implement TodoManager.update_task(task_id, title) method returning bool in src/services/todo_manager.py
- [x] T022 [US4] Add title validation in update_task (non-empty after strip) in src/services/todo_manager.py
- [x] T023 [US4] Implement CLI update_task flow: show tasks, prompt for ID, prompt for new title in src/cli/main.py
- [x] T024 [US4] Add handling for empty title with error message in src/cli/main.py
- [x] T025 [US4] Add handling for task not found with error message in src/cli/main.py

**Checkpoint**: User Stories 1-4 complete - users can add, view, complete, and update tasks

---

## Phase 7: User Story 5 - Delete Task (Priority: P5)

**Goal**: Enable users to delete tasks

**Independent Test**: Add a task, select "Delete Task", choose the task, verify task removed from list

### Implementation for User Story 5

- [x] T026 [US5] Implement TodoManager.delete_task(task_id) method returning bool in src/services/todo_manager.py
- [x] T027 [US5] Implement CLI delete_task flow: show tasks, prompt for ID, call manager in src/cli/main.py
- [x] T028 [US5] Add success message after deletion in src/cli/main.py
- [x] T029 [US5] Add handling for task not found with error message in src/cli/main.py

**Checkpoint**: All user stories complete - full CRUD functionality available

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Error handling, input validation, and final polish

- [x] T030 Add numeric input validation for menu selection in src/cli/main.py
- [x] T031 Add numeric input validation for task ID selection in src/cli/main.py
- [x] T032 Implement graceful exit option (option 6) in src/cli/main.py
- [x] T033 Add consistent header formatting for menu display in src/cli/main.py
- [x] T034 Add module-level docstrings to all Python files per constitution
- [x] T035 Verify all functions have type hints per constitution
- [x] T036 Run manual quickstart.md validation to verify all scenarios work

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phases 3-7)**: All depend on Foundational phase completion
  - User stories should be implemented in priority order (P1 → P2 → P3 → P4 → P5)
  - Each story builds on previous stories (e.g., view needs add, complete needs view)
- **Polish (Phase 8)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Depends on US1 (needs tasks to view) - Adds display functionality
- **User Story 3 (P3)**: Depends on US2 (needs task selection UI) - Adds complete functionality
- **User Story 4 (P4)**: Depends on US2 (needs task selection UI) - Adds update functionality
- **User Story 5 (P5)**: Depends on US2 (needs task selection UI) - Adds delete functionality

### Within Each User Story

- Service methods before CLI integration
- Core implementation before error handling
- Story complete before moving to next priority

### Parallel Opportunities

- T002 and T003 can run in parallel (different directories)
- Within Phase 2, T004, T005, T006 modify different files but have logical dependencies
- Within each user story phase, service tasks should complete before CLI tasks

---

## Parallel Example: Setup Phase

```bash
# Launch package marker creation in parallel:
Task: "Create package markers: src/__init__.py, src/models/__init__.py..."
Task: "Create tests package markers: tests/__init__.py, tests/unit/__init__.py..."
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Task)
4. **STOP and VALIDATE**: Test adding tasks works
5. Demo if ready - basic task capture is functional

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test adding tasks → Demo (MVP!)
3. Add User Story 2 → Test viewing tasks → Demo
4. Add User Story 3 → Test completing tasks → Demo
5. Add User Story 4 → Test updating tasks → Demo
6. Add User Story 5 → Test deleting tasks → Demo
7. Polish phase → Final validation → Release

### Sequential Implementation (Recommended for Phase 1)

Since this is a single-developer project with interdependent stories:

1. Setup → Foundational → US1 → US2 → US3 → US4 → US5 → Polish
2. Each story builds on previous functionality
3. Validate at each checkpoint before proceeding

---

## Task Summary

| Phase | Tasks | Story |
|-------|-------|-------|
| Setup | T001-T003 | N/A |
| Foundational | T004-T006 | N/A |
| User Story 1 | T007-T011 | US1 (Add) |
| User Story 2 | T012-T015 | US2 (View) |
| User Story 3 | T016-T020 | US3 (Complete) |
| User Story 4 | T021-T025 | US4 (Update) |
| User Story 5 | T026-T029 | US5 (Delete) |
| Polish | T030-T036 | N/A |

**Total Tasks**: 36
**MVP Scope**: T001-T011 (11 tasks for Setup + Foundational + Add Task)

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Tests omitted as not explicitly requested in spec
