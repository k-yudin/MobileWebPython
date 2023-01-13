from appium import webdriver

APP = '/Users/kyudin/Downloads/TheApp-v1.9.0.apk'
APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'Android',
    'platformVersion': '11',
    'automationName': 'UiAutomator2',
    'udid': 'ZE222X8GH8',
    'app': APP
}

driver = webdriver.Remote(command_executor=APPIUM, desired_capabilities=CAPS)
app_id = 'io.cloudgrey.the_app'

try:
    driver.remove_app(app_id)
    driver.install_app(APP)
    driver.activate_app(app_id)
    driver.terminate_app(app_id)
finally:
    driver.quit()
