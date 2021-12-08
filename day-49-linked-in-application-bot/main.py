from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = "test@gmail.com"
ACCOUNT_PASSWORD = "test"

ser = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=ser)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=105773754&keywords=python%20developer&location=Bucharest%2C%20Romania")

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

#Wait for the next page to load.
time.sleep(5)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)




















































