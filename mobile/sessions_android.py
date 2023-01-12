from appium import webdriver

APP = 'https://github.com/cloudgrey-io/the-app/releases/download/v1.9.0/TheApp-v1.9.0.apk'
APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'Android',
    'platformVersion': '8.1',
    'deviceName': 'Android Emulator',
    'automationName': 'UiAutomator2',
    'app': APP
}

driver = webdriver.Remote(command_executor=APPIUM, desired_capabilities=CAPS)
driver.quit()
