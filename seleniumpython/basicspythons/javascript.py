import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#
# driver.execute_script('document.getElementById("checkBoxOption1").click()')
# time.sleep(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

time.sleep(5)
name = driver.find_element(By.NAME,"username")
driver.execute_script("arguments[0].value='Admin';", name)
time.sleep(5)
passwrd = driver.find_element(By.NAME,"password")
driver.execute_script("arguments[0].value='admin123';", passwrd)
time.sleep(5)
submit = driver.find_element(By.XPATH,"*//button[@type='submit']")
driver.execute_script("arguments[0].click();", submit)
time.sleep(5)

