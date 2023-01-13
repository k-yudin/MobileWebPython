import time

from appium import webdriver

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
app_id = 'io.cloudgrey.the_app'
app_activity_1 = '.graphics.TouchPaint'
app_activity_2 = '.text.Marquee'

try:
    driver.install_app(APP)
    driver.start_activity(app_id, app_activity_1)
    time.sleep(2)
    driver.start_activity(app_id, app_activity_2)
    time.sleep(2)
finally:
    driver.quit()
