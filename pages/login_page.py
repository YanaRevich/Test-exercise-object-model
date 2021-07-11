from .base_page import BasePage
from .locators import LoginPageLocators
from pages.main_page import MainPage
from selenium.webdriver.common.by import By
import time
import faker
f = faker.Faker()

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        # проверка, что на странице имеется форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что на странице имеется форма регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        print("Register form is presented")
  
    def register_new_user(self, browser, email, password):
        # метод, который регистрирует пользователя
        email = browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email.send_keys(f.email())
        password = browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys("WFDPTEGAj")
        password2 = browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2).send_keys("WFDPTEGAj")
        button = browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()
        print ("Registration completed") 
        
    def should_be_message_after_registration(self):
        # проверка, что  после регистрации пользователю отображается уведомление "Thanks for registering"   
        assert self.is_element_present(*LoginPageLocators.SUCCESSFUL_REGISTRATION_MESSAGE), \
        "Something went wrong, message after registration is not presented"
        print ("Message 'Thanks for registering' is presented") 

