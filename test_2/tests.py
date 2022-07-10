from YandexPages import SearchHelper

def test_first_task(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.image_link()
    main_page.switch_to_images()
    main_page.popular_pictures()
    main_page.open_pictures()
    