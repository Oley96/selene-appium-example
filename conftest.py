import pytest
from selene.api import config
from appium import webdriver


@pytest.fixture
def mobile_driver():
    config.timeout = 10

    desired_caps = {
        'platformName': 'iOS',
        'platformVersion': '12.2',
        'deviceName': 'iPhone X',
        'deviceOrientation': 'PORTRAIT',
        'app': "https://github.com/saucelabs-training/demo-java/blob/master/appium-example/resources/ios/SauceGuineaPig-sim-debug.app.zip?raw=true"
    }

    driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",
                              desired_capabilities=desired_caps)
    config.driver = driver

    yield driver
    driver.quit()
