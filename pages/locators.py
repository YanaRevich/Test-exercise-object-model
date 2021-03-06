from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.PARTIAL_LINK_TEXT, "basket") # ссылка на корзину в шапке сайта
 
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD =(By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "button[name='registration_submit']")
    SUCCESSFUL_REGISTRATION_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button[value='Add to basket']")
    PRODUCT_NAME_IN_MESSAGE_AFTER_ADD_TO_BASKET = (By.CSS_SELECTOR,"div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRICE_PRODUCT_IN_THE_MESSAGE = (By.CSS_SELECTOR, ".alertinner p strong")

class BasketPageLocators():
    MESSAGE_ABOUT_IS_ANY_PRODUCT_IN_THE_BASKET = (By.CSS_SELECTOR, ".row h2")
    MESSAGE_ABOUT_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")