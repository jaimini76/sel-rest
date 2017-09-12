from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("http://www.gmail.com")
username = driver.find_element_by_id('identifierId')
username.send_keys('abc@gmail.com')
username.send_keys(Keys.RETURN)
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/form/div[2]/div/div/div[1]/div[1]/div/div[1]/div/div[1]/input")))
password.click()
password.send_keys("")
password.send_keys(Keys.RETURN)
driver.close()
