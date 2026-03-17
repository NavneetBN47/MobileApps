import pytest
from time import sleep
from MobileApps.libs.flows.windows import utility

pytest.app_info = "GOTHAM"
class Test_Suite_04_Check_Developer_Tools_Button(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.about = cls.fc.fd["about"]

        cls.stack = request.config.getoption("--stack")

    def test_01_click_cancel_button(self):
        """
        Click "Cancel" Button on Developer Tool.

        Verify Developer Tool page dismiss and About page is seen.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14815154
        """
        self.fc.go_home()
        self.home.select_app_settings_btn()
        self.home.verify_app_settings_pane()
        self.home.select_about_listview()
        self.about.verify_about_screen()
        self.about.click_app_logo()
        self.about.verify_developer_tools_screen(self.stack)
        assert self.about.verify_enter_password_edit(raise_e=False) is False
        self.about.click_cancel_button()
        self.about.verify_about_screen()

    def test_02_click_copy_oobe_logs_button(self):
        """
        Click "Copy OOBE Logs" button on Developer Tool.
        Select a path and click Save on the file explore dialog.
        Click "Close" button on "OOBE Log File Copied" dialog.

        Verify File Explore open with the current OOBE log file ready to be saved.
        Verify "OOBE Log File Copied" dialog box shows after saving it to a location.
        Verify the OOBE log file can be open at the saved location.
        Verify the dialog is dismissed.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14815155
        https://hp-testrail.external.hp.com/index.php?/cases/view/14815156
        https://hp-testrail.external.hp.com/index.php?/cases/view/14815157
        """
        file_path = r'C:\Users\exec\Documents\HPSmart_oobe_log.log'
        try:
            self.about.click_app_logo()
            self.about.verify_developer_tools_screen(self.stack)
            self.about.click_copy_oobe_logs_button()
            self.about.verify_save_as_dialog()
            self.about.enter_file_name_and_save(file_path)
            self.about.verify_oobe_log_copied_dialog()
            self.about.click_dialog_close_button()
            assert self.about.verify_oobe_log_copied_dialog(raise_e=False) is False
            utility.check_path_exist(self.driver.ssh, file_path) is True
        finally:
            self.driver.ssh.send_command('Remove-Item -Path {}'.format(file_path))

    def test_03_click_copy_logs_button(self):
        """
        Click "Copy Logs" button on Developer Tool.
        Select a path and click Save on the file explore dialog.
        Click "Close" button on "Log File Copied" dialog.

        Verify File Explore open with the current Gotham log file ready to be saved.
        Verify "Log File Copied" dialog box shows after saving it to a location.
        Verify the gotham log file can be open at the saved location.
        Verify the dialog is dismissed.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14815158
        https://hp-testrail.external.hp.com/index.php?/cases/view/14815159
        https://hp-testrail.external.hp.com/index.php?/cases/view/14815160
        """
        file_path = r'C:\Users\exec\Documents\HPSmart_log.zip'
        try:
            self.about.click_copy_logs_button()
            self.about.verify_save_as_dialog()
            self.about.enter_file_name_and_save(file_path)
            self.about.verify_log_copied_dialog()
            self.about.click_dialog_close_button()
            assert self.about.verify_log_copied_dialog(raise_e=False) is False
            utility.check_path_exist(self.driver.ssh, file_path) is True
        finally:
            self.driver.ssh.send_command('Remove-Item -Path {}'.format(file_path))

    def test_04_click_hide_developer_tools_button(self):
        """
        Click "Hide developer Tools" on Developer Tool.

        Verify User navigates to main UI.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14815163
        """
        self.about.click_hide_dev_tools_button()
        self.home.verify_home_screen()
        sleep(2)
        self.home.select_app_settings_btn()
        self.home.verify_app_settings_pane()
        self.home.select_about_listview()
        self.about.verify_about_screen()
        self.about.click_app_logo()
        self.about.verify_developer_tools_screen(self.stack)

    def test_05_edit_incorrect_password_for_advanced_tools(self):
        """
        Click "Advance Tools" on Developer Tool.
        Enter incorrect password into the text box shown.

        Verify No any dialog pops up.

        https://hp-testrail.external.hp.com/index.php?/cases/view/15077557
        """
        self.about.click_advanced_tools_button()
        self.about.verify_enter_password_edit()
        self.about.enter_password_edit('123')
        assert self.about.verify_advanced_tools_screen(raise_e=False) is False

    def test_06_edit_correct_password_for_advanced_tools(self):
        """
        Click "Advance Tools" on Developer Tool.
        Enter correct password into the text box shown.

        Verify Advanced Tools (Only for Developer) dialog popup after input correct password.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14815164
        https://hp-testrail.external.hp.com/index.php?/cases/view/14815168
        """
        self.about.verify_enter_password_edit()
        self.about.enter_password_edit('Gotham')
        if self.stack != 'production':
            self.about.verify_advanced_tools_screen()
        else:
            assert self.about.verify_advanced_tools_screen(raise_e=False) is False
            
    def test_07_check_advanced_tools_screen(self):
        """
        Click buttons/checkboxes/radio buttons/toggles on Advanced Tools (Only for Developer) dialog.

        Verify TestMode toggle can be turned On/Off.
        Verify Server Settings checkbox can be checked/unchecked.
        Verify the OWS server videos can be checked.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14815167
        """
        if self.stack != 'production':
            self.about.verify_advanced_tools_screen()
            self.about.check_test_mode_toggle()
            self.about.check_server_settings_checkbox()
            self.about.check_ows_server_video(self.stack)

    def test_08_close_advanced_tools_screen(self):
        """
        Click "x" on Advanced Tools (Only for Developer) dialog.

        Verify the Advanced Tools dialog dismissed and Developer tools screen shows.

        https://hp-testrail.external.hp.com/index.php?/cases/view/15077558
        """
        if self.stack != 'production':
            self.about.click_at_close_button()
            assert self.about.verify_advanced_tools_screen(raise_e=False) is False
            self.about.verify_developer_tools_screen(self.stack)
