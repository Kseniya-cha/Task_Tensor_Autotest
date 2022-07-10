# ожидание элементов
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://yandex.ru"


    def wait_of_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")
        return element


    def go_to_site(self):
        return self.driver.get(self.base_url)

