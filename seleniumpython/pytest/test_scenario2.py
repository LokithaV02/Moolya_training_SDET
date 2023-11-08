import pytest
from conftest import setup

@pytest.mark.skip
@pytest.mark.sanity
def test_case3():
    a = 2
    b = 3
    c = a+b
    print(c)


def test_case4regression(setup):
    print("pytest is done")