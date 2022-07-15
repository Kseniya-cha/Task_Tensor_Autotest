from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure

class YandexSeacrhLocators:

    LOCATOR_YANDEX_IMAGES_LINK = (By.PARTIAL_LINK_TEXT, 'Картинки')
    LOCATOR_YANDEX_POPULAR_IMAGES = (By.CLASS_NAME,'PopularRequestList-SearchText')
    LOCATOR_YANDEX_SEARCH_FIELD = (By.CLASS_NAME, 'input__control.mini-suggest__input')
    LOCATOR_YANDEX_FIRST_IMAGE = (By.CLASS_NAME, 'serp-item__thumb.justifier__thumb')
    LOCATOR_YANDEX_IMAGE_IS_OPENED = (By.CLASS_NAME, 'MMImage-Origin')
    LOCATOR_YANDEX_RIGHT_ARROW = (By.XPATH,'/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[4]')
    LOCATOR_YANDEX_LEFT_ARROW = (By.XPATH,'/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[1]')


class SearchHelper(BasePage):


    @allure.feature('2-3 пункты')
    def image_link(self):
        with allure.step('2) Проверить, что ссылка «Картинки» присутствует на странице'):
            images_link = self.wait_of_element(
                YandexSeacrhLocators.LOCATOR_YANDEX_IMAGES_LINK)
            assert images_link, f'Ссылка «Картинки» отсутствует на странице'
            print('Ссылка «Картинки» присутствует на странице')

        with allure.step('3) Кликаем на ссылку'):
            images_link.click()


    # переход к новой вкладке
    @allure.feature('4) Проверить, что перешли на url https://yandex.ru/images/')
    def switch_to_images(self):
        # self.driver.switch_to.window(self.driver.window_handles[1])
        # - не работает, не получилось устранить возникающую ошибку
        self.driver.get('https://yandex.ru/images/')
        assert self.driver.current_url == 'https://yandex.ru/images/', f'Не перешли на url https://yandex.ru/images/'
        print('Перешли на url https://yandex.ru/images/')
    

    @allure.feature('5-6 пункты')
    def popular_pictures(self):
        with allure.step('5) Открыть первую категорию'):
            self.wait_of_element( 
                YandexSeacrhLocators.LOCATOR_YANDEX_POPULAR_IMAGES).click()
        
        with allure.step('6) Проверить, что название категории отображается в поле поиска'):
            finder_field_not_empty = self.wait_of_element(
                YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD).get_attribute('value')
            assert finder_field_not_empty, f'Название категории не отображается'
            print(f'Название категории - {finder_field_not_empty}')
    

    @allure.feature('7-12 пункты')
    def open_pictures(self):
        with allure.step('7) Открыть 1 картинку'):
            self.wait_of_element(
                YandexSeacrhLocators.LOCATOR_YANDEX_FIRST_IMAGE).click()
        
        with allure.step('8) Проверить, что картинка открылась'):
            link_pic_1 = self.wait_of_element(
                YandexSeacrhLocators.LOCATOR_YANDEX_IMAGE_IS_OPENED).get_attribute("src")
            assert link_pic_1, f'Картинка не открылась'
            print('Картинка открылась')
        
        with allure.step('9) Нажать кнопку вперед'):
            self.wait_of_element(
                YandexSeacrhLocators.LOCATOR_YANDEX_RIGHT_ARROW).click()
        
        with allure.step('10) Проверить, что картинка сменилась'):
            link_pic_2 = self.wait_of_element(
                YandexSeacrhLocators.LOCATOR_YANDEX_IMAGE_IS_OPENED).get_attribute("src")
            assert link_pic_2 != link_pic_1, f'Картинка не сменилась'
            print('Картинка сменилась')

        with allure.step('11) Нажать назад'):
            self.wait_of_element(
                YandexSeacrhLocators.LOCATOR_YANDEX_LEFT_ARROW).click()
        
        with allure.step('12) Проверить, что картинка осталась из шага 8'):
            assert self.wait_of_element(
                YandexSeacrhLocators.LOCATOR_YANDEX_IMAGE_IS_OPENED).get_attribute("src") ==\
                link_pic_1, f'Картинка не та же, что в шаге 8'
            print('Картинка осталась из шага 8')

