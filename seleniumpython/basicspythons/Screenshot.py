from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demoqa.com/frames")
driver.maximize_window()
driver.get_screenshot_as_png()
driver.save_screenshot("image.png")
imageopen = Image.open("image.png")
imageopen.show()

