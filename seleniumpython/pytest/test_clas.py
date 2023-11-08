# execute at class level
import pytest

from conftest import setup


@pytest.mark.usefixtures("setup")
class Test_Python:
    def test_c1(self):
        print("this is first method")

    def test_c2(self):
        print("this is second method")

    def test_c3(self):
        print("this is third method")


@pytest.mark.usefixtures("data")
class Test_dtone:
    def test_tc1(self, data):
        print(data)


