import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

# searching for "CA" in search box
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ca")
driver.implicitly_wait(15)
add_items = driver.find_elements(By.XPATH,"//div[@class='product']")
print(len(add_items))


# Adding the items to cart
for item in add_items:
    driver.implicitly_wait(10)
    item.find_element(By.CLASS_NAME,"increment").click()
    cart = item.find_element(By.XPATH,".//button[contains(text(),'ADD TO CART')]")
    cart.click()
    added_cart_text = cart.get_attribute("class")
    print(added_cart_text)
    assert added_cart_text == "added"


# click on Cart and proceed
driver.find_element(By.CSS_SELECTOR,"a.cart-icon").click()
driver.find_element(By.XPATH,"//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
time.sleep(5)

# Each item sum = total amount
total_column = driver.find_elements(By.XPATH,"*//table[@id='productCartTables']//tr/*[5]")
t_sum = 0
for value in total_column[1:]:
    t_sum = t_sum + int(value.text)
    print(sum)

total_amount = driver.find_element(By.XPATH,"*//span[@class='totAmt']").text
Amount = int(total_amount)
print(Amount)

assert Amount == t_sum
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/button").click()
print("Placing order")


# Select Country, click on checkbox and click on Proceed
country = driver.find_element(By.XPATH,"//div[@class='products']//div//div//select")
Select(country).select_by_value("India")

driver.find_element(By.XPATH,"*//input[@type='checkbox']").click()
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div/button").click()

# Placing Order successfully
driver.implicitly_wait(30)
text_msg = driver.find_element(By.XPATH,"*//div[@class='products']//div//span")
message = text_msg.text
assert message == '''Thank you, your order has been placed successfully
You'll be redirected to Home page shortly!!'''
print("Order placed successfully")
