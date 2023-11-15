from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SortPage:

    def __init__(self, driver):
        self.driver = driver

    sorting_prod = (By.XPATH, "//div[@class='filter-dropdown']//select")

    def sort_the_product(self):
        self.driver.implicitly_wait(10)
        a = self.driver.find_element(*SortPage.sorting_prod)
        sort_dd = Select(a)
        sort_dd.select_by_visible_text("What's New")
