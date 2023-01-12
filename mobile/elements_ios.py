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

driver = webdriver.Remote(command_executor=APPIUM, desired_capabilities=CAPS)

try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Echo Box')
    )).click()
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'messageInput')
    )).send_keys('Hello!')
    driver.find_element(MobileBy.ACCESSIBILITY_ID, 'messageSaveBtn').click()

    saved_text = driver.find_element(MobileBy.ACCESSIBILITY_ID, 'savedMessage').text
    assert saved_text == 'Hello!'

    driver.back()

    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Echo Box')
    )).click()
    saved_text = wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'savedMessage'
         ))).text
    assert saved_text == 'Hello!'
finally:
    driver.quit()
