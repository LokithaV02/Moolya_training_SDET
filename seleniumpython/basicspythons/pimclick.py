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

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.title)  # get the title of the page
print(driver.current_url)  # get the currentURL
time.sleep(3)

# login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)

# Select PIM
driver.find_element(By.LINK_TEXT,"PIM").click()
time.sleep(5)

# Employee List
driver.find_element(By.XPATH,"(//div//input[@placeholder='Type for hints...'])[1]").send_keys("ch")
time.sleep(3)
name = driver.find_elements(By.XPATH,"(//div[@class='oxd-autocomplete-dropdown --positon-bottom']//div[@role='option'])")
print(len(name))
# driver.find_element(By.XPATH,"(//span[text()='Charlie Carter)").click()

driver.find_element(By.XPATH,"(//div[@class='oxd-autocomplete-dropdown --positon-bottom']//div[@role='option'])[1]").click()
time.sleep(3)

# employment status drop down
# static drop down
driver.find_element(By.XPATH,"(//div[@class='oxd-select-text oxd-select-text--active'])[1]").click()
time.sleep(4)
listname = driver.find_elements(By.XPATH,"(//div[@role='listbox']//div[@role='option'])")
print(len(listname))
driver.find_element(By.XPATH,"(//div[@role='listbox']//div[@role='option'])[3]").click()
time.sleep(5)
