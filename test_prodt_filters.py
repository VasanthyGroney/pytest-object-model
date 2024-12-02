from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "https://grocerymate.masterschool.com/store"

def test_price_filter(selenium_driver):
    driver = selenium_driver
    driver.get(URL)
    popup = driver.find_element(By.XPATH, "//div[@class='modal-content']")
    if popup:
        data_input = driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='DD-MM-YYYY']")
        confirm_button = driver.find_element(By.XPATH, "//button[text()='Confirm']")
        data_input.send_keys("10-10-1990")
        time.sleep(5)
        confirm_button.click()
    filter_button = driver.find_element(By.XPATH, "//div[@class='custom-select']")
    filter_button.click()
    time.sleep(3)
    price_option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='custom-option']"))
    )
    time.sleep(2)
    price_option.click()
    time.sleep(5)
