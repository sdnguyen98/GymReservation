from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Use Service class for ChromeDriver
service = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

#YOUR OSU LOGIN
login_u = input("Enter username:")
login_p = input("Enter password:")

driver.get("https://shop.recsports.oregonstate.edu/booking/47c87f69-0234-4aba-9c22-99d036560eb8")

time.sleep(2)

# Updated element finding methods
login_button = driver.find_element(By.CLASS_NAME, "loginOption.btn.btn-lg.btn-block.btn-social.btn-soundcloud")
login_button.click()

userlog = driver.find_element(By.ID, "username")
userlog.send_keys(login_u)
passlog = driver.find_element(By.ID, "password")
passlog.send_keys(login_p)
passlog.send_keys(Keys.RETURN)

time.sleep(10)

current_link = driver.current_url
print(current_link)
flag = 0
while(flag == 0):
    if(current_link == "https://shop.recsports.oregonstate.edu/booking/47c87f69-0234-4aba-9c22-99d036560eb8" ):
        date_buttons = driver.find_elements(By.CLASS_NAME, "btn.btn-default.single-date-select-button.single-date-select-one-click")
        flag = 1
    else:
        time.sleep(5)
        flag = 0

print(date_buttons)
date_buttons[1].click()
