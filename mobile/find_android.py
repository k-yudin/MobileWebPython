from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

APP = 'https://github.com/cloudgrey-io/the-app/releases/download/v1.9.0/TheApp-v1.9.0.apk'
APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'Android',
    'platformVersion': '11',
    'automationName': 'UiAutomator2',
    'udid': 'ZE222X8GH8',
    'app': APP
}

driver = webdriver.Remote(command_executor=APPIUM, desired_capabilities=CAPS)

try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Login Screen')
    ))
    driver.find_element(MobileBy.CLASS_NAME, 'android.widget.TextView')
    driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Webview Demo"]')
finally:
    driver.quit()
