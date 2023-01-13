import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

APP = "https://github.com/cloudgrey-io/the-app/releases/download/v1.9.0/TheApp-v1.9.0.app.zip";
APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'iOS',
    'platformVersion': '16.2',
    'deviceName': 'iPhone 14 Pro',
    'automationName': 'XCUITest',
    'app': APP
}


class WebViewActive(object):

    def __call__(self, driver):
        for context in driver.contexts:
            if context != 'NATIVE_APP':
                driver.switch_to.context(context)
                return True
        return False


driver = webdriver.Remote(command_executor=APPIUM, desired_capabilities=CAPS)

try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Webview Demo')
    )).click()

    wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//XCUIElementTypeTextField[@name="urlInput"]')
    )).send_keys('https://appiumpro.com')
    driver.find_element(MobileBy.ACCESSIBILITY_ID, 'navigateBtn').click()
    time.sleep(1)
    wait.until(WebViewActive())
    print(driver.current_url)
    print(driver.title)
finally:
    driver.quit()
