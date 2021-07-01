from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add.click()

    def add_quiz(self):
    	self.solve_quiz_and_get_code()
    
    def shoul_be_message_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        assert self.is_element_present(*ProductPageLocators.SUCCSESS_ADD_TO_BASKET), "Message about adding is not presented" 
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text     
        message = self.browser.find_element(*ProductPageLocators.SUCCSESS_ADD_TO_BASKET).text
        assert product_name in message, "No product name in the message"
    def shoul_be_price_product_in_the_message_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Price is not presented оn the page of product"
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT_IN_THE_MESSAGE), "Message about price product when it added to basket is not presented"
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_product_in_message = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_THE_MESSAGE).text
        assert product_price in price_product_in_message, "No product price in the message"
