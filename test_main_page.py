from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import time
import pytest

#@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser): 
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() # открываем страницу
        page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
        time.sleep(5)
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

#@pytest.mark.skip
def test_guest_should_be_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

#@pytest.mark.skip
def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

#@pytest.mark.skip
def test_guest_should_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()

#@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open() # Гость открывает главную страницу
    page.go_to_basket_page() # Переходит в корзину по кнопке в шапке сайта
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.shoul_not_be_message_about_any_products() # Ожидаем, что в корзине нет товаров
    basket_page.shoul_be_message_about_empty_basket() # Ожидаем, что есть текст о том, что корзина пуста 
    
#@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/excession_51/"  
    page = ProductPage(browser, link)
    page.open() #Гость открывает страницу товара
    page.go_to_basket_page() #Переходит в корзину по кнопке в шапке 
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.shoul_not_be_message_about_any_products() # Ожидаем, что в корзине нет товаров
    basket_page.shoul_be_message_about_empty_basket()#Ожидаем, что есть текст о том что корзина пуста

