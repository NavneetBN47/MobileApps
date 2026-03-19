import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestShortcutsFunctionality:
    def test_add_new_shortcut(self, driver):
        wait = WebDriverWait(driver, 10)
        
        # Navigate to shortcuts screen
        add_shortcuts_button = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "Add Shortcuts")
            )
        )
        add_shortcuts_button.click()
        
        # Click on "Add New Shortcut" button
        add_new_button = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.Button[@text='Add New']")
            )
        )
        add_new_button.click()
        
        # Fill in shortcut details
        name_field = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='shortcut_name']")
            )
        )
        name_field.send_keys("Test Shortcut")
        
        url_field = driver.find_element(
            AppiumBy.XPATH, "//android.widget.EditText[@resource-id='shortcut_url']"
        )
        url_field.send_keys("https://example.com")
        
        # Save the shortcut
        save_button = driver.find_element(
            AppiumBy.XPATH, "//android.widget.Button[@text='Save']"
        )
        save_button.click()
        
        # Verify shortcut was added
        shortcut_item = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.TextView[@text='Test Shortcut']")
            )
        )
        assert shortcut_item.is_displayed(), "Shortcut was not added successfully"
        
        print("Test passed: Successfully added new shortcut")
    
    def test_edit_shortcut(self, driver):
        wait = WebDriverWait(driver, 10)
        
        # Navigate to shortcuts screen
        add_shortcuts_button = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "Add Shortcuts")
            )
        )
        add_shortcuts_button.click()
        
        # Long press on existing shortcut to edit
        shortcut_item = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.TextView[@text='Test Shortcut']")
            )
        )
        driver.execute_script("mobile: longClickGesture", {"elementId": shortcut_item.id})
        
        # Click edit option
        edit_option = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.TextView[@text='Edit']")
            )
        )
        edit_option.click()
        
        # Modify shortcut name
        name_field = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='shortcut_name']")
            )
        )
        name_field.clear()
        name_field.send_keys("Updated Shortcut")
        
        # Save changes
        save_button = driver.find_element(
            AppiumBy.XPATH, "//android.widget.Button[@text='Save']"
        )
        save_button.click()
        
        # Verify shortcut was updated
        updated_shortcut = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.TextView[@text='Updated Shortcut']")
            )
        )
        assert updated_shortcut.is_displayed(), "Shortcut was not updated successfully"
        
        print("Test passed: Successfully edited shortcut")
    
    def test_delete_shortcut(self, driver):
        wait = WebDriverWait(driver, 10)
        
        # Navigate to shortcuts screen
        add_shortcuts_button = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "Add Shortcuts")
            )
        )
        add_shortcuts_button.click()
        
        # Long press on shortcut to delete
        shortcut_item = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.TextView[@text='Updated Shortcut']")
            )
        )
        driver.execute_script("mobile: longClickGesture", {"elementId": shortcut_item.id})
        
        # Click delete option
        delete_option = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.TextView[@text='Delete']")
            )
        )
        delete_option.click()
        
        # Confirm deletion
        confirm_button = wait.until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.Button[@text='Confirm']")
            )
        )
        confirm_button.click()
        
        # Verify shortcut was deleted
        from selenium.common.exceptions import TimeoutException
        try:
            wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, "//android.widget.TextView[@text='Updated Shortcut']")
                )
            )
            assert False, "Shortcut still exists after deletion"
        except TimeoutException:
            print("Test passed: Successfully deleted shortcut")
            pass