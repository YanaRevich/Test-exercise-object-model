from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    #проверка того, что в корзине нет товаров
    def shoul_not_be_message_about_any_products(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE_ABOUT_IS_ANY_PRODUCT_IN_THE_BASKET), "Message about is any product in the basket is not presented"

    #проверка наличия сообщения о том, что корзина пуста
    def shoul_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_BASKET_EMPTY), "Message about basket empty is not presented"
