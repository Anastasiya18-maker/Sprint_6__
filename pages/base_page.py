from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

class BasePage:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/' # URL

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_url(self):
        self.driver.get(self.BASE_URL)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_into_view(self, locator):
        element = self.wait.until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def find_element_with_wait(self, locator1, locator2 = None):
        if locator2:
            self.wait.until(expected_conditions.invisibility_of_element(locator2))
        return self.wait.until(expected_conditions.visibility_of_element_located(locator1))

    def click_on_element(self, locator1):
        element = self.find_element_with_wait(locator1)
        element.click()

    def get_text_from_element(self, locator1):
        element = self.find_element_with_wait(locator1)
        return element.text

    def format_locator(self, locator, num):
        method, locator = locator
        locator = locator.format(num)
        return (method, locator)

    def get_current_url(self):
        return self.driver.current_url

    def is_visible(self, locator):
        return self.driver.find_element(locator).is_displayed()

    def windows_switch(self):
        return self.driver.window_handles

    def switch_to_window(self, handles):
        self.driver.switch_to.window(handles[1])