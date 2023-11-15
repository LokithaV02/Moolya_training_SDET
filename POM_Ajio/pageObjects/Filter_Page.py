import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FilterPage:

    def __init__(self, driver):
        self.driver = driver

    gen_more_link = (By.XPATH, "(//li//div[@id='verticalsizegroupformat'])[1]")
    men_sel = (By.XPATH, "//form//label[@for='modal-Men']")
    apply_btn = (By.XPATH, "//button[@aria-label='Apply']")
    sel_price = (By.XPATH, "(//div//span[@class='facet-left-pane-label'])[3]")
    min_price = (By.ID, "minPrice")
    max_price = (By.ID, "maxPrice")
    price_submit = (By.XPATH, "//div[@class='input-price-filter']//button[@type= 'submit']")
    no_of_filter = (By.XPATH, "//div[@class='fnl-plp-afliter']")

    def filter_by_gender(self):
        self.driver.find_element(*FilterPage.gen_more_link).click()
        men_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(FilterPage.men_sel))
        men_element.click()
        self.driver.find_element(*FilterPage.apply_btn).click()

    def filter_by_price(self):
        self.driver.find_element(*FilterPage.sel_price).click()
        self.driver.find_element(*FilterPage.min_price).send_keys("100")
        self.driver.find_element(*FilterPage.max_price).send_keys("700")
        self.driver.find_element(*FilterPage.price_submit).click()
        self.driver.implicitly_wait(10)

    def verifying_filters_applied(self):
        filters_applied = self.driver.find_elements(*FilterPage.no_of_filter)
        assert len(filters_applied) == 2
