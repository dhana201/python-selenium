from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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

driver.find_element(By.LINK_TEXT, "TRANSFER").click()
driver.find_element(By.XPATH, '//*[@id="9999000453354533"]').click()
frm_acc_ele = driver.find_element(By.CSS_SELECTOR, "#fromaccount")
("9999000453354527")

to_acc_ele = driver.find_element(By.XPATH, '//*[@id="toaccount"]')
assert to_acc_ele.is_enabled() == False, "Element must be disabled"
driver.find_element(By.XPATH,'//*[@id="amount"]').send_keys("1000")
driver.find_element(By.CSS_SELECTOR,"#message").send_keys("Transfer")
driver.find_element(By.XPATH,'//*[@id="confirm_payment"]').click()

assert "Transaction Successful" == driver.find_element(By.ID,"confirmationMessage").text, \
    "Confirmation Message is Wrong"