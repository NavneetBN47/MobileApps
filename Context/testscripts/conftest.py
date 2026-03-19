import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"  # Change this to your device name
    options.app_package = "com.example.mobileapp"  # Replace with your app package
    options.app_activity = ".MainActivity"  # Replace with your main activity
    options.automation_name = "UiAutomator2"
    
    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()