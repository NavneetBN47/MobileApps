import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddShortcuts:
    def test_add_shortcuts(self, driver):
        # Wait for the main screen to load
        wait = WebDriverWait(driver, 10)
        
        # Find and click the "Add Shortcuts" button
        add_shortcuts_button = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "Add Shortcuts")
            )
        )
        add_shortcuts_button.click()
        
        # Verify that we navigated to the shortcuts screen
        shortcuts_title = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.TextView[@text='Shortcuts']")
            )
        )
        assert shortcuts_title.is_displayed(), "Shortcuts screen not displayed"
        
        print("Test passed: Successfully navigated to Add Shortcuts screen")