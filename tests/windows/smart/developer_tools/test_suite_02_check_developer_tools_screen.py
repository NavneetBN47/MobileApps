import pytest
from time import sleep
from MobileApps.libs.flows.windows import utility
import MobileApps.resources.const.windows.const as w_const
import logging

pytest.app_info = "GOTHAM"
class Test_Suite_02_Check_Developer_Tools_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.about = cls.fc.fd["about"]

        cls.stack = request.config.getoption("--stack")
        
        cls.logs_path = w_const.TEST_DATA.GOTHAM_APP_LOG_PATH + '\Logs'
        cls.gotham_log = w_const.TEST_DATA.HP_SMART_LOG_PATH
        cls.logging_data = cls.logs_path + '\LoggingData.xml'
        cls.gotham_oobe_log = cls.logs_path + '\HPSmart_OOBE.log'

    def test_01_go_home_and_enable_developer_tools_screen(self):
        """
        Click 10 or more times on the app logo.
        Verify developer tool screen shows.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/14815125 
        https://hp-testrail.external.hp.com/index.php?/cases/view/14815126
        """
        self.fc.go_home()
        self.home.select_app_settings_btn()
        self.home.verify_app_settings_pane()
        self.home.select_about_listview()
        self.about.verify_about_screen()
        self.about.click_app_logo()
        self.about.verify_developer_tools_screen(self.stack)

    def test_02_check_logging_toggle_and_box(self):
        """
        Verify OOBE logging option is checked by default.
        check the toggle can be turn off/on.        
        Verify there's no "LoggingData.xml" file for Win.
        Verify enable Logging is default on with non-production builds, on production build, the logging is turned off by default.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14815136 
        https://hp-testrail.external.hp.com/index.php?/cases/view/14815128
        https://hp-testrail.external.hp.com/index.php?/cases/view/14815140
        """
        assert self.about.get_toggle_status(0) == 1
        self.about.click_toggle(0)
        assert self.about.get_toggle_status(0) == 0
        self.about.click_toggle(0)
        assert utility.check_path_exist(self.driver.ssh, self.gotham_oobe_log) is True
        if self.stack in ['stage', 'pie']:
            assert self.about.get_toggle_status(1) == 1
            self.about.click_toggle(1)
            assert self.about.get_toggle_status(1) == 0
            self.about.click_toggle(1)
        else:
            logging.info("The Logging toggle has been turned on during setup flow for production stack, skip the check")
        assert utility.check_path_exist(self.driver.ssh, self.gotham_log) is True
        assert utility.check_path_exist(self.driver.ssh, self.logging_data) is True

    def test_03_change_logging_level_and_save_setting(self):
        """
        Change the logging level in the drop-down box.
        Save the setting.

        Verify "Settings saved." dialog shows.
        Verify 1-10 values are displayed and selectable in logging level dropdown .
        Verify the settings can be changed and saved successfully.
        Verify the logging value in the LoggingData.xml file is consistent with that set from developer tool UI.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14815141
        https://hp-testrail.external.hp.com/index.php?/cases/view/14815143
        https://hp-testrail.external.hp.com/index.php?/cases/view/14815138
        """      
        assert int(self.about.get_logging_level_value()) == 10
        for i in range(1, 11):
            self.about.click_logging_value_dropdown()
            sleep(1)
            self.about.select_logging_level_value(i)
            assert int(self.about.get_logging_level_value()) == i
            self.about.click_save_setting_button()
            self.about.verify_settings_saved_dialog()
            self.about.click_dialog_close_button()
            sleep(1)
            self.about.check_logging_data_file_level(i)

    def test_04_click_clear_logs_button(self):
        """
        Click "Clear Logs" button on Developer Tool

        Verify it does not pop up anything.
        Verify the current logs files (hp smart & hp smart oobe) are cleared, their file size is 0~2KB.
        Verify old log files are still present.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14815162
        """   
        before_size = self.about.get_file_size(self.gotham_log)
        before_files = self.about.get_logs_file()        
        self.about.click_clear_logs_button()
        self.about.verify_developer_tools_screen(self.stack)
        after_size = self.about.get_file_size(self.gotham_log)
        after_files = self.about.get_logs_file()
        assert before_size > 2.0
        assert 0.0 <= after_size < 2.0
        assert before_files == after_files
