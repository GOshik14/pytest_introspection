import pytest
from time import sleep

@pytest.mark.smoke
def test_failing():
    a = 1
    sleep(3)
    assert (a, 2, 3) == (3, 2, 1)

@pytest.mark.skip()
def test_skipping():
    assert (1, 2, 3) == (3, 2, 1)

@pytest.mark.xfail()
def test_xfailing():
    assert (1, 2, 3) == (1, 2)
