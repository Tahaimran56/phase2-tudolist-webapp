"""
Task data model for the Todo application.

This module defines the Task dataclass that represents a single work item
to be tracked by the user.
"""

from dataclasses import dataclass


@dataclass
class Task:
    """
    Represents a single task in the todo application.

    Attributes:
        id: Unique identifier assigned by the system.
        title: Required task title (must be non-empty).
        description: Optional task description (defaults to empty string).
        is_completed: Whether the task has been marked complete (defaults to False).
    """

    id: int
    title: str
    description: str = ""
    is_completed: bool = False
