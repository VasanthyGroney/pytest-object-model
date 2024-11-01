import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # No path or Service specification
    driver.get("https://www.wikipedia.org")
    yield driver
    driver.quit()


def test_search_selenium_webdriver(driver):
    # Locate the search bar and enter text
    search_bar = driver.find_element(By.NAME, "search")
    search_bar.send_keys("Selenium WebDriver")

    # Submit the form by pressing Enter or locating the search button
    search_bar.send_keys(Keys.RETURN)

    # Verify the result page contains "Selenium WebDriver"
    assert "Selenium WebDriver" in driver.page_source
