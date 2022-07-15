from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure


class YandexSeacrhLocators:

    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SUGGEST = (By.CLASS_NAME, 'mini-suggest__popup-content')
    LOCATOR_YANDEX_LINK = (By.LINK_TEXT, 'tensor.ru')


class SearchHelper(BasePage):


    @allure.feature('Проверка наличия поля поиска и таблицы с подсказками')
    def enter_text(self):
        with allure.step('2) Проверить наличия поля поиска'):
            search_field = self.wait_of_element(
                YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
            assert search_field, f"На странице отсутствует поле поиска"
            print('На странице имеется поле поиска')
        
        with allure.step('3) Ввести в поиск Тензор'):
            search_field.send_keys("Тензор")

        with allure.step('4) Проверить, что появилась таблица с подсказками (suggest)'):
            suggest = self.wait_of_element(
                YandexSeacrhLocators.LOCATOR_YANDEX_SUGGEST)
            assert suggest, f"Не появилась таблица с подсказками"
            print('Появилась таблица с подсказками')

        with allure.step('5) При нажатии Enter появляется таблица результатов поиска'):
            search_field.send_keys(Keys.ENTER)



    @allure.feature('6) Проверить 1 ссылка ведет на сайт tensor.ru')
    def find_link(self):
        link = self.wait_of_element(
            YandexSeacrhLocators.LOCATOR_YANDEX_LINK)
        assert link, f"Нет ссылки на сайт tensor.ru"
        print('1 ссылка ведет на сайт tensor.ru')

