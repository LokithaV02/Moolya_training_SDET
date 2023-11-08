from selenium.webdriver.common.by import By


class FilterPage:

    def __init__(self, driver):
        self.driver = driver

    gen_more_link = (By.XPATH, "(//li//div[@id='verticalsizegroupformat'])[1]")
    men_sel = (By.XPATH, "//form//label[@for='modal-Men']")
    apply_btn = (By.XPATH, "//button[@aria-label='Apply']")
    price = (By.XPATH, "//span[@aria-label='price']")
    minprice = (By.ID, "minPrice")
    maxprice = (By.ID, "maxPrice")
    price_submit = (By.XPATH, "//div[@class='input-price-filter']//button[@type= 'submit']")
    no_of_filter = (By.XPATH, "//div[@class='fnl-plp-afliter']")

    def click_on_more_link(self):
        self.driver.find_element(*FilterPage.gen_more_link)

    def select_men(self):
        self.driver.find_element(*FilterPage.men_sel)

    def click_on_apply_button(self):
        self.driver.find_element(*FilterPage.apply_btn)

    def click_on_price_filter(self):
        self.driver.find_element(*FilterPage.price)

    def enter_min_price(self):
        self.driver.find_element(*FilterPage.minprice)

    def enter_max_price(self):
        self.driver.find_element(*FilterPage.maxprice)

    def click_on_submit_price(self):
        self.driver.find_element(*FilterPage.price_submit)

    def verify_filter(self):
        self.driver.find_element(*FilterPage.no_of_filter)
