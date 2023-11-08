import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    service_obj = Service()
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://www.ajio.com")
    driver.maximize_window()
    driver.implicitly_wait(10)

    request.cls.driver = driver
    yield
    driver.close()
