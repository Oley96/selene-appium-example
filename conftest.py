import os

import pytest
from selene.api import config
from appium import webdriver
import dotenv

dotenv.load_dotenv()


@pytest.fixture
def mobile_driver():
    config.timeout = 10

    desired_caps = {
        'platformName': "IOS",
        'platformVersion': os.getenv('platform.version'),
        'deviceName': os.getenv('device.name'),
        'orientation': os.getenv('device.orientation'),
        'app': os.getenv('app.location'),
    }

    driver = webdriver.Remote(command_executor=os.getenv('remote.url'),
                              desired_capabilities=desired_caps)
    config.driver = driver

    yield driver
    driver.quit()
