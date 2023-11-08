import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)

# Select PIM
driver.find_element(By.LINK_TEXT,"PIM").click()
time.sleep(5)

idval= driver.find_element(By.XPATH,"//div[contains(text(),Neha Manoj)]")
time.sleep(10)
driver.execute_script("arguments[0].scrollIntoView();",idval)
print(idval.text)