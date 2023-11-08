from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.ID, "openwindow").click()
handles = driver.window_handles
parent_handle = driver.current_window_handle
print(parent_handle.title())
size = len(handles)
driver.switch_to.window(parent_handle)
for x in range(size):
    if handles[x] != parent_handle:
        driver.switch_to.window(handles[x])
        print(driver.title)
        driver.close()
        break

