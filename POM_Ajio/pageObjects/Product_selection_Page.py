import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    item_text = "Men Slim Fit Track Pants with Insert Pockets"
    items = (By.XPATH, f"//div[@class='nameCls' and contains(text(), '{item_text}')]")
    name = (By.CLASS_NAME, "prod-name")
    diff_colours_options = (By.CLASS_NAME, "color-swatch")
    single_colour = (By.CLASS_NAME, 'color-swatch')
    diff_size_options = (By.CLASS_NAME, "size-swatch")

    def select_product_and_verify(self):
        prod = self.driver.find_elements(*ProductPage.items)
        if len(prod) == 1:
            prod[0].click()  # Click on the first product found if only one matching product found
        elif len(prod) > 1:
            prod[3].click()
        time.sleep(10)
        wind = self.driver.window_handles
        self.driver.switch_to.window(wind[1])
        print(self.driver.title)
        product_name = self.driver.find_element(*ProductPage.name).text
        assert product_name == ProductPage.item_text

    def select_product_color(self):
        sel_colours = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located(ProductPage.diff_colours_options))
        if len(sel_colours) > 1:
            sel_colours[3].click()
        else:
            sel_single_color = self.driver.find_element(*ProductPage.single_colour)
            sel_single_color.click()

    def select_product_size(self):
        sel_size = self.driver.find_elements(*ProductPage.diff_size_options)
        print(len(sel_size))
        for size in sel_size:
            if size.text == "M":
                size.click()
                break
