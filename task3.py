from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class WikipediaSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_bar = (By.NAME, "search")

    def enter_search_text(self, text):
        search_input = self.driver.find_element(*self.search_bar)
        search_input.clear()
        search_input.send_keys(text)

    def submit_search(self):
        search_input = self.driver.find_element(*self.search_bar)
        search_input.send_keys(Keys.RETURN)
