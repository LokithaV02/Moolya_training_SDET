from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    searchbar = (By.NAME, "searchVal")
    search_icon = (By.XPATH, "//*[@class='ic-search']")

    def search_item_on_searchbar(self):
        self.driver.find_element(*HomePage.searchbar)

    def click_on_search_icon(self):
        self.driver.find_element(*HomePage.search_icon)
