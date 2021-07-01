from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.add_quiz()
    page.shoul_be_message_add_to_basket()
    page.shoul_be_price_product_in_the_message_add_to_basket()
    time.sleep(20)
