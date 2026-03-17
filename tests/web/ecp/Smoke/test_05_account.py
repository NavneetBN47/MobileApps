import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "ECP"

class Test_05_ECP_Account(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.account = self.fc.fd["account"]
        self.login_account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.login_account["email"]
        self.hpid_password = self.login_account["password"]
        
    def test_01_verify_account_profile_screen(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29093042
        #this test case verify account profile screen's objects and its label name
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_user_icon_top_right()   
        self.home.click_user_icon_menu_account_profile_item()
        self.account.verify_account_profile_page()

        self.account.verify_firstname()
        self.account.verify_firstname_label()

        self.account.verify_lastname()
        self.account.verify_lastname_label()

        self.account.verify_email()
        self.account.verify_email_label()

        self.account.verify_phone_number()
        self.account.verify_phone_number_label()

        self.account.verify_country()
        self.account.verify_country_label()

    @pytest.mark.skip
    def test_02_verify_update_user_profile(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29093169
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_user_icon_top_right()   
        self.home.click_user_icon_menu_account_profile_item()
        # Get the logged account details 
        user_first_name=self.account.get_first_name()
        user_last_name=self.account.get_last_name()
        # user_email=self.account.get_email()
       
        # update account details 
        self.account.enter_first_name("update_"+user_first_name)
        self.account.enter_last_name("update_"+user_last_name)
        self.account.click_apply_changes_button()
        self.account.verify_toast_notification()

        # Verify updated user details
        self.account.verify_first_name("update_"+user_first_name)
        self.account.verify_last_name("update_"+user_last_name)
        
        # reverback updated account details
        self.account.dismiss_toast()
        self.account.enter_first_name(user_first_name)
        self.account.enter_last_name(user_last_name)
        self.account.click_apply_changes_button()
        self.account.verify_toast_notification()

    def test_03_verify_contextual_footer(self):

        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_user_icon_top_right()   
        self.home.click_user_icon_menu_account_profile_item()
        self.account.verify_account_profile_page()
        
        #  Verify the contextual footer is not displayed by default
        self.account.verify_account_profile_contextual_footer_is_not_displayed()
       
        # update account details 
        self.account.enter_first_name("update_")
       
        # Verify contextual_footer is displayed after enter either first name or last name
        self.account.verify_account_profile_contextual_footer_is_displayed()
        self.account.verify_cancel_button_is_displayed()
        self.account.verify_apply_changes_button()

    def test_04_verify_account_screen(self):
        # 
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.verify_home_menu_btn()
        self.home.click_account_menu_btn()
        self.account.verify_page_title(page_title="Account")
        self.account.verify_account_profile_card()
        self.account.verify_account_profile_card_title()
        self.account.verify_account_profile_card_description()
        self.account.click_account_profile_card()
        self.account.verify_page_title(page_title="Account Profile")