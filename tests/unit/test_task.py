"""
tests.test_task
Check data type Task from task.task
"""


import pytest

import sys
sys.path.append("/home/egor/Python/pytest_introspection/task/")
from task.task import Task

@pytest.mark.smoke
def test_defaults():
    """
    Docstring for test_defaults
    Checking default values for namedtuple class Task
    """

    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access():
    """
    Check access to the fields of Task by namedtuple mark
    """

    t = Task("buy milk", "brian")
    assert t.summary == "buy milk"
    assert t.owner == "brian"
    assert (t.done, t.id) == (False, None)

def test_asdict():
    t = Task("do smth.", "okken", True, 1)
    t_dict = t._asdict()
    expected = {"summary": "do smth.",
                "owner": "okken",
                "done": True,
                "id": 1}
    assert t_dict == expected

def test_replace():
    t_before = Task("finish book", "brian", False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task("finish book", "brian", True, 10)
    assert t_after == t_expected