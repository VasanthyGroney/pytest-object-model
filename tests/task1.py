from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://academy.masterschool.com")
time.sleep(3)
print(driver.title)
driver.quit()
