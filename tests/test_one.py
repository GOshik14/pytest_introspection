import pytest

@pytest.mark.smoke
def test_passing():
    print("@pytest.mark.smoke")
    assert (1, 2, 3) == (1, 2, 3)
