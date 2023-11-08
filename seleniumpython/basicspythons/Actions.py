import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()

# Actions
Action = ActionChains(driver)
# Action.double_click()
Action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
driver.implicitly_wait(10)
Action.key_down(Keys.ARROW_DOWN).perform()
#Context click - Right click
Action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
Action.key_down(Keys.ENTER).perform()
Action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

Action.key_down(Keys.CONTROL, "a").key_up(Keys.CONTROL).perform()

src = driver.find_element(By.ID,"draggable")
target = driver.find_element(By.ID,"droppable")
Action.drag_and_drop(src,target)