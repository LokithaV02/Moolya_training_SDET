import time
from selenium.webdriver.common.by import By


class HomePageSearch:
    def __init__(self, driver):
        self.driver = driver

    searchbar = (By.NAME, "searchVal")
    search_icon = (By.XPATH, "//*[@class='ic-search']")
    header = (By.XPATH, "//div[@class='header2']")

    def search_clothes_and_verifying_search(self):
        enter_text = self.driver.find_element(*HomePageSearch.searchbar)
        enter_text.send_keys("clothes")
        text_in_search = enter_text.get_attribute("value")
        time.sleep(5)
        self.driver.find_element(*HomePageSearch.search_icon).click()
        header_text = self.driver.find_element(*HomePageSearch.header).text
        print(header_text)
        assert text_in_search == header_text.lower()
