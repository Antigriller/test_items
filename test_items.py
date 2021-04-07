import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_exist(browser):
    browser.get(link)
    try:
        element = browser.find_element_by_css_selector(".btn-add-to-basket")
    except:
        element = None
    finally:
    	assert element != None, "Кнопка куда-то подевалась"
    time.sleep(30)