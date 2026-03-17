import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc
pytest.app_info = "smb"

class Test_10_SMB_HelpCenter(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, smb_setup, request):
        self = self.__class__
        self.driver, self.fc = smb_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        #locale will be received in language_region format
        self.locale = self.driver.session_data["locale"]+"/"+self.driver.session_data["language"]
        self.spec_file = self.driver.session_data["language"]+"-"+self.driver.session_data["locale"].upper()
        self.home = self.fc.fd["home"]
        self.helpcenter = self.fc.fd["helpcenter"]
        self.login_account = ma_misc.get_smb_account_info(self.stack)
        self.hpid_username = self.login_account["email"]
        self.hpid_password = self.login_account["password"]
        self.hpid_tenantID = self.login_account["tenantID"]
        self.attachment_path = conftest_misc.get_attachment_folder()

    def test_01_verify_helpcenter_screen_ui(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_help_center_menu()
        self.home.click_help_center_menu_btn()

        #To load localization files based on the specified language
        self.fc.load_localization_files(self.spec_file)

        # creating a folder to store Screenshot 
        ma_misc.create_localization_screenshot_folder("helpcenter_localization_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "helpcenter_screenshot/{}_helpcenter_localization.png".format(self.locale))

        # verifying the helpcenter landing page strings
        self.helpcenter.verify_help_center_title()
        self.helpcenter.verify_about_help_center_title()
        # self.helpcenter.verify_about_help_center_description()

        self.helpcenter.verify_help_center_printing_title()
        self.helpcenter.verify_help_center_help_and_support_title()
        self.helpcenter.verify_help_center_account_title()
        self.helpcenter.verify_help_center_scan_and_fax_settings_title()
        self.helpcenter.verify_help_center_sustainability_title()
        self.helpcenter.verify_help_center_solutions_title()
        self.helpcenter.verify_help_center_hp_instant_ink_title()
        self.helpcenter.verify_help_center_managing_users_title()
        self.helpcenter.verify_help_center_managing_printers_title()
        self.helpcenter.verify_help_center_hp_smart_admin_dashboard_title()
        self.helpcenter.verify_helpcenter_breadcrumb_helpcenter_text()
        self.helpcenter.verify_helpcenter_breadcrumb_home_text()

        logging.info("Current URL: {}".format(self.driver.get_current_url()))