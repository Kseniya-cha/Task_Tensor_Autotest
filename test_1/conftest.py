# инициализация драйвера
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox

@pytest.fixture(scope="session")
def browser():
    profile_path = r'C:\Program Files\drives_selenium\geckodriver.exe'
    options = Options()
    options.set_preference('profile', profile_path)
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()