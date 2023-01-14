from appium import webdriver
import pytest
from views.home_view import HomeView

IOS_APP = "https://github.com/cloudgrey-io/the-app/releases/download/v1.9.0/TheApp-v1.9.0.app.zip";
ANDROID_APP = 'https://github.com/cloudgrey-io/the-app/releases/download/v1.9.0/TheApp-v1.9.0.apk'
APPIUMS = ['http://localhost:4700', 'http://localhost:4701']

IOS_CAPS = [{
    'platformName': 'iOS',
    'platformVersion': '16.2',
    'deviceName': 'iPhone 14 Pro',
    'automationName': 'XCUITest',
    'app': IOS_APP
}, {
    'platformName': 'iOS',
    'platformVersion': '16.2',
    'deviceName': 'iPhone 14 Pro Max',
    'automationName': 'XCUITest',
    'app': IOS_APP
}]

ANDROID_CAPS = [{
    'platformName': 'Android',
    'platformVersion': '11',
    'automationName': 'UiAutomator2',
    'udid': 'ZE222X8GH8',
    'app': ANDROID_APP
}, {
    'platformName': 'Android',
    'platformVersion': '8.1',
    'automationName': 'UiAutomator2',
    'app': ANDROID_APP
}]


def pytest_addoption(parser):
    parser.addoption('--platform', action='store', default='ios')


@pytest.fixture
def worker_num(worker_id):
    if worker_id == 'master':
        worker_id = 'gw0'
    return int(worker_id[2:])


@pytest.fixture
def server(worker_num):
    if worker_num >= len(APPIUMS):
        raise Exception('Too many workers for the num of Appium servers!')
    return APPIUMS[worker_num]


@pytest.fixture
def caps(platform, worker_num):
    cap_set = IOS_CAPS if platform == 'ios' else ANDROID_CAPS
    if worker_num >= len(cap_set):
        raise Exception('Too many workers for the num of Appium servers!')
    return cap_set[worker_num]


@pytest.fixture
def platform(request):
    plat = request.config.getoption('platform').lower()
    if plat not in ['ios', 'android']:
        raise ValueError('--platform value must be ios or android')
    return plat


@pytest.fixture
def driver(server, caps, platform):
    driver = webdriver.Remote(command_executor=server, desired_capabilities=caps)
    driver._platform = platform
    yield driver
    driver.quit()


@pytest.fixture
def home(driver):
    return HomeView.instance(driver)
