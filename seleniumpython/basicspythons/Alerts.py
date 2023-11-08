import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# drivers
# webdrivermanager
# Chrome Driver
# default time for selenium= 30s
# default time for implicitwait= 0s
# default time for explicit wait = until condition is satisfied
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
print(driver.title)  # get the title of the page
print(driver.current_url)  # get the currentURL
driver.implicitly_wait(10)



# Switch to Alert Example- Alert
driver.find_element(By.ID,"alertbtn").click()
alt = driver.switch_to.alert
message = alt.text
assert "Hello ," in message
time.sleep(5)
alt.accept()
# alt.send_keys("test")
time.sleep(5)


# Switch to Alert Example - Confirm
driver.find_element(By.ID,"confirmbtn").click()
conf = driver.switch_to.alert
conf.dismiss()

# Explicit Wait
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Free Access")))
element.click()