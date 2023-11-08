import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.parametrize("params",["ca", "cu", "ap"])
class TestGreenkart:
    def test_placeorder(self,params):
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj)
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        driver.maximize_window()

        # searching for "CA" in search box
        driver.find_element(By.XPATH, "//input[@type='search']").send_keys(params)
        driver.implicitly_wait(15)
        additems = driver.find_elements(By.XPATH, "//div[@class='product']")
        print(len(additems))

        # Adding the items to cart
        for item in additems:
            driver.implicitly_wait(10)
            item.find_element(By.CLASS_NAME, "increment").click()
            cart = item.find_element(By.XPATH, ".//button[contains(text(),'ADD TO CART')]")
            cart.click()
            addedcarttext = cart.get_attribute("class")
            print(addedcarttext)
            assert addedcarttext == "added"

        # click on Cart and proceed
        driver.find_element(By.CSS_SELECTOR, "a.cart-icon").click()
        driver.find_element(By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
        time.sleep(5)

        # Each item sum = total amount
        total_column = driver.find_elements(By.XPATH, "*//table[@id='productCartTables']//tr/*[5]")
        sum = 0
        for value in total_column[1:]:
            sum = sum + int(value.text)
            print(sum)

        totalamount = driver.find_element(By.XPATH, "*//span[@class='totAmt']").text
        Amount = int(totalamount)
        print(Amount)

        assert Amount == sum
        driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div/button").click()
        print("Placing order")

        # Select Country, click on checkbox and click on Proceed
        country = driver.find_element(By.XPATH, "//div[@class='products']//div//div//select")
        Select(country).select_by_value("India")

        driver.find_element(By.XPATH, "*//input[@type='checkbox']").click()
        driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div/button").click()

        # Placing Order successfully
        driver.implicitly_wait(30)
        textmsg = driver.find_element(By.XPATH, "*//div[@class='products']//div//span")
        message = textmsg.text
        assert message == '''Thank you, your order has been placed successfully
You'll be redirected to Home page shortly!!'''
        print("Order placed successfully")
