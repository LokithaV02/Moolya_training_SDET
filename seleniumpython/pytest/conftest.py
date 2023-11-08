# anything before yeild is Before method
# anything after yeild is After method
import pytest


@pytest.fixture(scope="class")
def setup():
    print("this will run first")
    yield
    print("this will run in the last")


@pytest.fixture(params=["chrome","firefox"])
def data(browser):
    return browser.params
