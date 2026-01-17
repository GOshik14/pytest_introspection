"""
tests.test_task_fail
Check data type Task from task.task_fail
and expecte tests will fail
"""


import pytest

import sys
sys.path.append("/home/egor/Python/pytest_introspection/task/")
from task.task import Task

@pytest.mark.equality
def test_task_equality():
    """Different task should be equal
    """

    t1 = Task("sit there", "brian")
    t2 = Task("do smth.", "okken")

    assert t1 == t2
@pytest.mark.equality
def test_dict_equality():
    """Different task, made like dict, should be equal"""
    t1_dict = Task("make sandwich", "okken")._asdict()
    t2_dict = Task("make sandwich", "okkey")._asdict()
    assert t1_dict == t2_dict