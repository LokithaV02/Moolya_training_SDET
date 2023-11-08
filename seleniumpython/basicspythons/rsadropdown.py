import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# drivers
# webdrivermanager
# Chrome Driver
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)  # get the title of the page
print(driver.current_url)  # get the currentURL
time.sleep(3)

# Dropdown Example
dd = Select(driver.find_element(By.ID,"dropdown-class-example"))
dd.select_by_index(2)
# dd.select_by_visible_text("Option2")
# dd.select_by_value("option2")

# Suggestion class example
countrytobedisplayed = "India"
driver.find_element(By.ID,"autocomplete").send_keys("ind")
time.sleep(3)
countrylist= driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item']")
print(len(countrylist))
for i in countrylist:
    if i.text == countrytobedisplayed:
        i.click()
        break
valuetext = driver.find_element(By.ID,"autocomplete").is_displayed()
print(valuetext) # prints TRUE if displayed and FALSE if not displayed

# I want to capture  the text which is displayed
# get_attribute: to get the attributes(id, value, class) of dynamic attributes
expected = driver.find_element(By.ID,"autocomplete").get_attribute("value")
assert expected == countrytobedisplayed

# click on Checkbox
chkbox = driver.find_element(By.ID,"checkBoxOption2")
chkbox.click()
print(chkbox.is_selected())

#to count the no of checkboxes
noofchckbox= driver.find_elements(By.XPATH,"//label//*[@type='checkbox']")
print(len(noofchckbox))
# to check if the check box is selected or no

for i in noofchckbox:
    if i.get_attribute("value") == "option1":
        i.click()
        assert i.is_selected()
