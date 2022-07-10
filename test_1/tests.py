from YandexPages import SearchHelper

def test_first_task(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.enter_text('Тензор')
    main_page.find_link()
