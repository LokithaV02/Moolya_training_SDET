from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demoqa.com/frames")
driver.maximize_window()

# Switch to frame
driver.switch_to.frame("frame2")
text = driver.find_element(By.ID,"sampleHeading").text
print(text)
driver.switch_to.default_content()
print(driver.title)

