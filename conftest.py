import os

import pytest
from selene.api import config
from appium import webdriver
import dotenv


# dotenv.load_dotenv()

def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="IOS")


@pytest.fixture
def mobile_driver(request):
    config.timeout = 10

    if request.config.getoption("--platform") == "ios":
        dotenv.load_dotenv(dotenv_path=".env.ios")
    elif request.config.getoption("--platform") == "android":
        dotenv.load_dotenv(dotenv_path=".env.android")
    else:
        raise ValueError("Unsupported cli param")

    desired_caps = {
        'platformName': os.getenv('platform.name'),
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
