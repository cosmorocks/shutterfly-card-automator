import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


email = input("Please input your Shutterfly email address: ")
password = input("Please input your Shutterfly password: ")

driver = webdriver.Chrome()
driver.get("https://accounts.shutterfly.com/?redirectUri=https%3A%2F%2Fwww.shutterfly.com%2F&cid=&brand=SFLY&theme=SFLY")

# Wait for the page to load
timeout = 10  # seconds
try:
    element_present = EC.presence_of_element_located((By.NAME, "email"))
    WebDriverWait(driver, timeout).until(element_present)
    print("Page is ready!")
except TimeoutException:
    print("Timed out waiting for page to load")

email_input_field = driver.find_element(By.NAME, "email")
email_input_field.send_keys(email)

# taking user's inputted email and password and placing them into shutterfly sign-in fields
password_input_field = driver.find_element(By.NAME, "password")
password_input_field.send_keys(password)

sign_in_button = driver.find_element(By.ID, "signInButton")
sign_in_button.click()

timeout = 10  # seconds
try:
    element_present = EC.presence_of_element_located((By.ID, "boxclose"))
    WebDriverWait(driver, timeout).until(element_present)
    print("pop up close button is ready!")
except TimeoutException:
    print("Timed out waiting for pop up close button to load.")

pop_up_close_button = driver.find_element(By.ID, "boxclose")
pop_up_close_button.click()

# Opening the template URL to get to creation screen
driver.get("https://www.shutterfly.com/creationpath/bundle/views/projects/6577da00-71fe-11ef-8fce-ed6ba242058c?brand=SFLY&productCode=1161534&bundleId=3&sizeIds=27&occasionIds=105&styleIds=10829&qty=1&sizeId=undefined&bundleTypeName=ENVELOPE&groupId=3")

time.sleep(15)