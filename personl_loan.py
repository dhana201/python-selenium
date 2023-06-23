from selenium import webdriver
import time
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

driver.find_element(By.LINK_TEXT,"LOANS").click()
driver.find_element(By.XPATH,"//h5[text()='Personal Loan']/following-sibling::span").click()
driver.find_element(By.ID,"name").send_keys("Dhana")
driver.find_element(By.ID,"email").send_keys("dhana@gmail.com")
driver.find_element(By.ID,"mobile").send_keys("68365898984")
element = driver.find_element(By.ID,"basic")
proof_selection = Select(element)
proof_selection.select_by_visible_text("Aadhar card")

driver.find_element(By.ID,"myFile").send_keys(R"D:\dhana pic.png")

checkbox = driver.find_element(By.XPATH,"//*[@id='loan_details_tab']/div[2]/div[3]/div[8]/div/div/label/input")
if not checkbox.is_selected():
    checkbox.click()
driver.find_element(By.LINK_TEXT,"Submit").click()

