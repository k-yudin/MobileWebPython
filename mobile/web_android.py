from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

APPIUM = 'http://localhost:4723'

CAPS = {
    'appium:platformName': 'Android',
    'appium:platformVersion': '11',
    'appium:automationName': 'UiAutomator2',
    'appium:udid': 'ZE222X8GH8',
    'appium:browserName': 'Chrome'
}

driver = webdriver.Remote(command_executor=APPIUM, desired_capabilities=CAPS)

try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com')
    form_auth_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Form Authentication')
    ))
    form_auth_link.click()

    user_name = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#username')
    ))
    user_name.send_keys('tomsmith')

    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys('SuperSecretPassword!')

    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Logout')
    )).click()

    wait.until(EC.url_to_be('https://the-internet.herokuapp.com/login'))
    flash = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#flash')
    ))
    assert 'logged out' in flash.text
finally:
    driver.quit()
