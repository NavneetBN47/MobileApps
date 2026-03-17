from MobileApps.libs.flows.common.gotham.gotham_flow import GothamFlow
import MobileApps.resources.const.windows.const as w_const
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import logging
import re
import os


class About(GothamFlow):
    flow_name = "about"

    PRIVACY_LINK = "privacy_link"
    EULA_LINK = "eula_link"
    TOU_LINK = "term_of_use_link"

    PRIVACY_URL = ["privacy", "privacy-central"]
    EULA_URL = ["support.hp.com"]
    TOU_URL = ["tou"]

    toggle = ['enable_oobe_logging_toggle', 'enable_logging_toggle', 'turn_on_officemode_toggle']
    logs_path = w_const.TEST_DATA.GOTHAM_APP_LOG_PATH + '\Logs'
    logging_data = logs_path + '\LoggingData.xml'
    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_link(self, link):
        """
        Click on a link
        :param link: use class constants:
                PRIVACY_LINK 
                EULA_LINK
                TOU_LINK
        """
        self.driver.click(link)

    def get_copyright_year(self):
        copyright = self.driver.wait_for_object("copyright_text")
        copyright = copyright.text.split()
        return int(copyright[2])

    def click_app_logo(self):
        """
        Click 10 or more times on the app logo.
        """
        for _ in range(10):
            self.driver.click("about_logo")

    def click_logging_value_dropdown(self):
        self.driver.click("log_value_box")

    def select_logging_level_value(self, num):
        self.driver.click("dynamic_log_value", format_specifier=[num])

    def get_logging_level_value(self):
        return self.driver.get_attribute("log_value_num", attribute="Name")

    def click_toggle(self, index):
        """
        For index
        - 0: Enable OOBE logging
        - 1: Enable logging
        - 2: Turn on OfficeMode 
        """
        self.driver.click(self.toggle[index])
    
    def get_toggle_status(self, index):
        """
        For index
        - 0: Enable OOBE logging
        - 1: Enable logging
        - 2: Turn on OfficeMode
        """    
        return int(self.driver.get_attribute(self.toggle[index], attribute="Toggle.ToggleState"))

    def click_save_setting_button(self):
        self.driver.click('save_settings_btn')

    def click_dialog_close_button(self):
        self.driver.click('close_btn')

    def click_clear_logs_button(self):
        self.driver.click('clear_logs_btn')

    def get_app_instance_id(self):
        """
        Get App Instance ID
        """    
        return self.driver.get_attribute("app_id_link", attribute="Name")[8:]

    def click_app_id_copy_btn(self):
        self.driver.click("app_id_copy_btn")

    def hover_app_id_link(self):
        self.driver.hover("app_id_link")

    def hover_app_id_copy_btn(self):
        self.driver.hover("app_id_copy_btn")

    def click_cancel_button(self):
        self.driver.click('cancel_btn')

    def click_copy_oobe_logs_button(self):
        self.driver.click('copy_oobe_logs_btn')

    def click_copy_logs_button(self):
        self.driver.click('copy_logs_btn')

    def click_hide_dev_tools_button(self):
        self.driver.click('hide_developer_tools_btn')

    def click_advanced_tools_button(self):
        self.driver.click('advanced_tools_btn')

    def click_at_close_button(self):
        self.driver.click('at_close_btn')

    def enter_file_name_and_save(self, file_name):
        self.driver.send_keys("file_name_edit", file_name)
        sleep(2)
        self.driver.click("dialog_save_btn")

    def enter_password_edit(self, password):
        self.driver.send_keys("enter_password_edit", password, press_enter=True)
        sleep(2)

    def check_test_mode_toggle(self):
        assert int(self.driver.get_attribute("test_mode_toggle", attribute="Toggle.ToggleState")) == 0
        self.driver.click("test_mode_toggle")
        assert int(self.driver.get_attribute("test_mode_toggle", attribute="Toggle.ToggleState")) == 1
        sleep(2)

    def check_server_settings_checkbox(self): 
        assert int(self.driver.get_attribute("mns_check_box", attribute="Toggle.ToggleState")) == 0
        assert int(self.driver.get_attribute("ars_check_box", attribute="Toggle.ToggleState")) == 0
        self.driver.click("mns_check_box")
        self.driver.click("ars_check_box")
        assert int(self.driver.get_attribute("mns_check_box", attribute="Toggle.ToggleState")) == 1
        assert int(self.driver.get_attribute("ars_check_box", attribute="Toggle.ToggleState")) == 1
        sleep(2)

    def check_ows_server_video(self, stack): 
        if stack == 'pie':
            assert self.driver.get_attribute("pie_radio_btn", attribute="SelectionItem.IsSelected") == 'true'
            assert self.driver.get_attribute("stage_radio_btn", attribute="SelectionItem.IsSelected") == 'false'
            assert self.driver.get_attribute("prod_radio_btn", attribute="SelectionItem.IsSelected") == 'false'
        if stack == 'stage':
            assert self.driver.get_attribute("pie_radio_btn", attribute="SelectionItem.IsSelected") == 'false'
            assert self.driver.get_attribute("stage_radio_btn", attribute="SelectionItem.IsSelected") == 'true'
            assert self.driver.get_attribute("prod_radio_btn", attribute="SelectionItem.IsSelected") == 'false'
        if stack == 'production':
            assert self.driver.get_attribute("pie_radio_btn", attribute="SelectionItem.IsSelected") == 'false'
            assert self.driver.get_attribute("stage_radio_btn", attribute="SelectionItem.IsSelected") == 'false'
            assert self.driver.get_attribute("prod_radio_btn", attribute="SelectionItem.IsSelected") == 'true'
   
    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_about_screen(self):
        """
        Verify the current screen is about screen
        """
        self.driver.wait_for_object("about_logo")
        self.driver.wait_for_object("hp_smart_name")
        self.driver.wait_for_object("hp_smart_version")
        self.driver.wait_for_object("app_id_link")
        self.driver.wait_for_object("app_id_copy_btn")
        self.driver.wait_for_object("privacy_link")
        self.driver.wait_for_object("eula_link")
        self.driver.wait_for_object("term_of_use_link")
        self.driver.wait_for_object("copyright_text")

    def verify_copied_tips_load(self, timeout=3, raise_e=True):
        """
        Check the Copied tips shows after clicking App instance id icon.
        """
        return self.driver.wait_for_object("copied_tips", timeout=timeout, raise_e=raise_e)

    def verify_developer_tools_screen(self, stack):
        self.driver.wait_for_object("developer_tools_title")
        self.driver.wait_for_object("enable_oobe_logging_toggle")
        self.driver.wait_for_object("enable_logging_toggle")
        self.driver.wait_for_object("log_value_box")
        self.driver.wait_for_object("use_webview2_toggle")

        self.driver.wait_for_object("clear_logs_btn")
        self.driver.wait_for_object("copy_oobe_logs_btn")
        self.driver.wait_for_object("copy_logs_btn")
        self.driver.wait_for_object("advanced_tools_btn")
        self.driver.wait_for_object("hide_developer_tools_btn")
        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("save_settings_btn")

        if stack == 'stage':
            self.driver.wait_for_object("auto_open_webview2_toggle")
            self.driver.wait_for_object("turn_on_officemode_toggle")
            self.driver.wait_for_object("turn_on_private_pickup_toggle")
            self.driver.wait_for_object("use_dev_stack_toggle")
            self.driver.wait_for_object("enable_cloudscan_toggle")
            self.driver.wait_for_object("allow_unfiltered_toggle")
            self.driver.wait_for_object("enable_screen_names_toggle")

    def check_logging_data_file_level(self, level):
        if (fh := self.driver.ssh.remote_open(self.logging_data, mode="r+", raise_e=False)):
            data = fh.read().decode("utf-8")
            fh.close()
            match = re.search("<MaxLogLevel>{}</MaxLogLevel>".format(level), data)
            if not match:
                raise NoSuchElementException("level '{}' is not found in LoggingData.xml".format(level))    
    
    def get_file_size(self, file_path):
        file_size = self.driver.ssh.send_command("[math]::Round((Get-Item {} -Force).Length / 1KB, 1)".format(file_path))["stdout"].strip()
        logging.info('Size: {}'.format(file_size))
        return float(file_size)

    def get_logs_file(self):
        logs_list = self.driver.ssh.send_command('(Get-ChildItem -Path {}).Name'.format(self.logs_path))["stdout"].strip()
        return logs_list

    def check_new_file_created(self, new_file):
        logs_list = list(self.get_logs_file().split('\r\n'))
        num = 0
        for log in logs_list:
            if re.match(new_file, log):
                logging.info('Created log file: {}'.format(log))
                num = num + 1
        if num != 0:
            return num
        else:
            return False

    def enable_or_disable_toggle(self, index, enable=True):
        if enable:
            num = 1
        else:
            num = 0
        self.click_toggle(index)
        assert self.get_toggle_status(index) == num
        self.click_save_setting_button()
        self.verify_settings_saved_dialog()
        self.click_dialog_close_button()
        assert self.verify_settings_saved_dialog(raise_e=False) is False
        sleep(2)

    def verify_save_as_dialog(self):
        self.driver.wait_for_object("file_name_edit")

    def verify_save_as_dialog(self):
        self.driver.wait_for_object("file_name_edit")

    def verify_settings_saved_dialog(self, raise_e=True):
        return self.driver.wait_for_object("settings_saved_title", raise_e=raise_e) and\
        self.driver.wait_for_object("close_btn", raise_e=raise_e)

    def verify_oobe_log_copied_dialog(self, raise_e=True):
        return self.driver.wait_for_object("oobe_log_content", raise_e=raise_e) and\
        self.driver.wait_for_object("close_btn", raise_e=raise_e)

    def verify_log_copied_dialog(self, raise_e=True):
        return self.driver.wait_for_object("logs_copied_content", raise_e=raise_e) and\
        self.driver.wait_for_object("close_btn", raise_e=raise_e)

    def verify_enter_password_edit(self, raise_e=True):
        return self.driver.wait_for_object("enter_password_edit", raise_e=raise_e)

    def verify_advanced_tools_screen(self, raise_e=True):
        return self.driver.wait_for_object("pie_radio_btn", raise_e=raise_e) and\
        self.driver.wait_for_object("stage_radio_btn", raise_e=raise_e) and\
        self.driver.wait_for_object("prod_radio_btn", raise_e=raise_e)
