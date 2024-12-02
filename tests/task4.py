import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://grocerymate.masterschool.com/auth"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()


def test_registration(driver):
    time.sleep(5)
    create_account_link = driver.find_element(By.XPATH, "//a[@class='switch-link']")
    create_account_link.click()
    time.sleep(5)

    full_name_input = driver.find_element(By.XPATH, "//input[@type='text']")
    email_address_input = driver.find_element(By.XPATH, "//input[@type='email']")
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    full_name_input.send_keys("AgKnth")
    email_address_input.send_keys("1ac@example.com")
    password_input.send_keys("password1234")

    submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_btn.click()
    time.sleep(2)

    alert_div = driver.find_element(By.XPATH, "//div[@role='status']")
    assert alert_div.is_displayed() and alert_div.text

def test_login(driver):
    time.sleep(3)

    email_address_input = driver.find_element(By.XPATH, "//input[@type='email']")
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    email_address_input.send_keys("1ac@example.com")
    password_input.send_keys("password123")

    login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_btn.click()
    time.sleep(5)

    #dashboard_welcome = driver.find_element(By.XPATH, "//[contains(@class, 'submit-btn')]")
    assert driver.title == "Market Mate"





if __name__ == "__main__":
    pytest.main()