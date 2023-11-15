import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None


@pytest.fixture(scope="class",params=["chrome"])
def setup(request):
    global driver
    if request.param == "chrome":
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj)
    if request.param == "firefox":
        service_obj = Service()
        driver = webdriver.Firefox(service=service_obj)
    driver.get("https://www.ajio.com")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
