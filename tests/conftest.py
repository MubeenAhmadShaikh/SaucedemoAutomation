import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome", help="browser selection: chrome or firefox"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name in ("chrome", "ch", "Chrome"):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    elif browser_name in ("firefox", "ff", "Firefox"):
        firefox_service = Service(GeckoDriverManager().install())
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')
        firefox_options.add_argument('--no-sandbox')
        driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
    elif browser_name in ("Edge", "edge", "ed"):
        edge_options = EdgeOptions()
        edge_options.add_argument('--headless')
        edge_options.add_argument('--no-sandbox')
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)
    elif browser_name in ("Opera", "opera", "op"):
        opera_options = webdriver.ChromeOptions()
        opera_options.add_argument('--headless')
        opera_options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(service=Service(OperaDriverManager().install()), options=opera_options)

    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
