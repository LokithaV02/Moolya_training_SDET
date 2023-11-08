import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# drivers
# webdrivermanager
# Chrome Driver
service_obj = Service("C:\\Users\\Hp\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
# service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

# Firefox driver
# service_obj= Service()
# driver = webdriver.Firefox(service=service_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()  # Maximize window
# driver.minimize_window()  # minimize window
print(driver.title)  # get the title of the page
print(driver.current_url)  # get the currentURL
time.sleep(3)


# Locators
#id,Classname, Xpath, CSS, tagname, linktext, Partiallinktext, name

#login
driver.find_element(By.NAME, "username").send_keys("Admin")
# driver.find_element(By.XPATH, value="//input[@name='username']")
# driver.find_element(By.CSS_SELECTOR, value="input[name='username']")
# driver.find_element(By.CLASS_NAME, value="oxd-input")
# # when class is given convert to CSS using .classname
# driver.find_element(By.CSS_SELECTOR, value=".oxd-input")

driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
# driver.find_element(By.XPATH,"//button[contains(@class,'login-button')]").click()
time.sleep(5)

#logout
driver.find_element(By.CLASS_NAME,"oxd-dropdown-menu").click()
driver.find_element(By.CLASS_NAME,"oxd-userdropdown-link").click()

driver.close() # 1 Active = use close
driver.quit() # multiple Active = Use quit

#navigation commands
driver.back()
driver.forward()
driver.refresh()