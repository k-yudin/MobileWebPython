from appium import webdriver
import pytest
from views.home_view import HomeView

APP = "https://github.com/cloudgrey-io/the-app/releases/download/v1.9.0/TheApp-v1.9.0.app.zip";
APPIUM = 'http://localhost:4723'


@pytest.fixture
def driver():
    CAPS = {
        'platformName': 'iOS',
        'platformVersion': '16.2',
        'deviceName': 'iPhone 14 Pro',
        'automationName': 'XCUITest',
        'app': APP
    }
    driver = webdriver.Remote(command_executor=APPIUM, desired_capabilities=CAPS)
    yield driver
    driver.quit()


@pytest.fixture
def home(driver):
    return HomeView(driver)