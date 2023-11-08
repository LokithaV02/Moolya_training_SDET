import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Actions import Action

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()

src = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")
Action.drag_and_drop(src, target)
