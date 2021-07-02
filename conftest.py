import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
        help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
        help="Choose any language")


@pytest.fixture(scope="function")
def browser(request):

    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {"intl.accept_languages": user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FifefoxProfile()
        fp.set_preference("intil.accept_languages", user_language)
        print('\nstart firefox browser for test..')
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome")
    yield browser
    print("\nquit browser..")
    browser.quit()


