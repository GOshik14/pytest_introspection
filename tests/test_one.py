import pytest

@pytest.mark.run_smoke
def test_passing():
    print("@pytest.mark.run_smoke")
    assert (1, 2, 3) == (1, 2, 3)
