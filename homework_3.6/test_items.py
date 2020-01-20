import time
import selenium

#Тест поиска кнопки "Добавить в корзину"
def test_find_button_add_basket(browser, browser_language):
    link = f"http://selenium1py.pythonanywhere.com/{browser_language}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button_add_basket = browser.find_element_by_css_selector(".btn-add-to-basket")
    button_text = button_add_basket.text
    assert "" != button_text, "Button not found"


