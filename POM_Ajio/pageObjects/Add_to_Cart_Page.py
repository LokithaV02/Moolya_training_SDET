import time
from selenium.webdriver.common.by import By
import re
from datetime import datetime


class AddCart:
    def __init__(self, driver):
        self.driver = driver

    add_to_cart = (By.CSS_SELECTOR, "div.pdp-addtocart-button")
    prod_price = (By.XPATH, "//div[@class='prod-sp']")
    cart_icon = (By.CSS_SELECTOR, "div[class='ic-cart ']")
    checkout_price = (By.XPATH, "//div[@class='net-price best-price-strip']")
    proceed_checkout = (By.XPATH, "//button[contains(text(),'Proceed to shipping')]")
    signform = (By.CLASS_NAME, "modal-login-container")
    close = (By.CLASS_NAME, "ic-close-quickview")

    def product_add_to_cart(self):
        self.driver.find_element(*AddCart.add_to_cart).click()
        price = self.driver.find_element(*AddCart.prod_price).text
        price_of_prod = re.search(r'\d+', price).group()
        time.sleep(10)
        self.driver.find_element(*AddCart.cart_icon).click()
        checkout_prod_price = self.driver.find_element(*AddCart.checkout_price).text
        product_price_in_checkout = re.search(r'\d+', checkout_prod_price).group()
        assert int(price_of_prod) == int(product_price_in_checkout)

    def proceed_to_checkout(self):
        self.driver.find_element(*AddCart.proceed_checkout).click()
        sign_in_form = self.driver.find_element(*AddCart.signform)
        assert sign_in_form
        self.driver.find_element(*AddCart.close).click()

    def screen_shot_capture(self):
        time.sleep(3)
        path = r"C:\Users\Hp\PycharmProjects\POM_Ajio\Results"
        t_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        file_name = r'\reg_succ' + t_stamp + '.png'
        self.driver.get_screenshot_as_file(path + file_name)
