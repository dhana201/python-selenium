from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.get("https://birdbank.pythonanywhere.com/")
signin_button = driver.find_element(By.ID, "signin_button")
signin_button.click()
assert "Login - Internet Banking" == driver.title, "Title is incorrect"
driver.find_element(By.ID, "id_username").send_keys("testuser1")
driver.find_element(By.NAME, "password").send_keys("testpassword")
driver.find_element(By.ID, "signin").click()
assert "My Accounts - Bird Bank" == driver.title, "Title is incorrect"

driver.find_element(By.LINK_TEXT, "HELP").click()
driver.find_element(By.ID,"question").send_keys("Hey How Are you!!!")
driver.find_element(By.ID,"submit").click()

import time
time.sleep(1)
#PIL statement

import PIL.ImageGrab
im = PIL.ImageGrab.grab()
im.save("screenshot2.png", "PNG")