import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store",
    default="chrome", help="Type in browser name e.g.chrome OR firefox")

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager

    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())

    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test completed")