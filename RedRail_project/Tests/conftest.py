import pytest
from selenium import webdriver
from library.config import Config

@pytest.fixture(params=['chrome'])
def init_driver(request):
    browser = request.param

    if browser.lower() == 'chrome':
        driver = webdriver.Chrome(executable_path=Config.chrome_path)

    # elif browser.lower() == 'firefox':
    #     driver = webdriver.Firefox(executable_path=Config.firefox_path)
    #
    # else:
    #     driver = webdriver.Edge(executable_path=Config.edge_path)

        driver.get(Config.url)
        driver.maximize_window()
        yield driver
        driver.close()