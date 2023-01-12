import time

from appium import webdriver

APP = "https://github.com/cloudgrey-io/the-app/releases/download/v1.9.0/TheApp-v1.9.0.app.zip";
APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'iOS',
    'platformVersion': '16.2',
    'deviceName': 'iPhone 14 Pro',
    'automationName': 'XCUITest',
    'app': APP
}

driver = webdriver.Remote(command_executor=APPIUM, desired_capabilities=CAPS)

try:
    time.sleep(4)
    print(driver.page_source)
finally:
    driver.quit()
