import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection: chrome or firefox"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name in ("chrome", "ch", "Chrome"):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_service = Service('../chromedriver.exe')
        driver = webdriver.Chrome(service=chrome_service)
    elif browser_name in ("firefox", "ff", "Firefox"):
        firefox_service = Service("../geckodriver.exe")
        driver = webdriver.Firefox(service=firefox_service)


    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()


