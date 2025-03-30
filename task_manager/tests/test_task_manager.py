import pytest
from task_manager import TaskManager

def test_add_task():
    manager = TaskManager()
    task = manager.add_task("Estudar Python")
    assert task["description"] == "Estudar Python"
    assert len(manager.list_tasks()) == 1

def test_complete_task():
    manager = TaskManager()
    manager.add_task("Fazer exercícios")
    task = manager.complete_task(1)
    assert task["completed"] is True

def test_empty_description():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.add_task("")