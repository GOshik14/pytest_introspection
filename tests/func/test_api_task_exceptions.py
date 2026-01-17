import pytest

import sys
sys.path.append("/home/egor/Python/pytest_introspection/task/task.py")
from task.task import Task, is_task


@pytest.mark.smoke
def test_is_task_raises():
    with pytest.raises(TypeError) as exinfo:
        is_task("Task like string")
    exception_notice = exinfo.value.args[0]
    assert exception_notice == "Object type should be Task"