import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "ECP"

class Test_03_ECP_Account_Profile(object):

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
  
    def test_01_verify_account_profile_cancel_button(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29093158
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_user_icon_top_right()   
        self.home.click_user_icon_menu_account_profile_item()
        self.account.verify_account_profile_page()

        # Get acount details 
        user_first_name=self.account.get_first_name()
        user_last_name=self.account.get_last_name()
        
        # update account details 
        self.account.enter_first_name("update_"+user_first_name)
        self.account.enter_last_name("update_"+user_last_name)
        self.account.click_cancel_button()
       
        # Verify Accounts detaild should not update after select Cancel 
        self.account.verify_first_name(user_first_name)
        self.account.verify_last_name(user_last_name)   
        
    def test_02_verify_account_profile_apply_changes_button(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29094186
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_user_icon_top_right()   
        self.home.click_user_icon_menu_account_profile_item()
        self.account.verify_account_profile_page()

        self.account.enter_first_name("test user")

        #When updating any of the field, contextual footer should be displayed with Cancel and Apply Changes button
        self.account.verify_account_profile_contextual_footer_is_displayed()
        self.account.verify_apply_changes_button()

    # def test_03_verify_account_profile_email_field_error_message(self):
    #     #https://hp-testrail.external.hp.com/index.php?/cases/view/29093245
    #     self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
    #     self.home.click_account_menu_btn()
    #     self.account.verify_account_profile_page()

    #     #Verify empty_email_error_message
    #     self.account.clear_email_text()
    #     self.account.verify_empty_email_error_message()

    #     #Verify empty_email_error_message
    #     self.account.enter_email("invalidemail.com")
    #     self.account.verify_invalid_email_error_message()

    # def test_04_verify_popup_Updating_email_will_not_change_Username(self):
    #     #https://hp-testrail.external.hp.com/index.php?/cases/view/29432757
    #     self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
    #     self.home.click_account_menu_btn()
    #     self.account.verify_account_profile_page()

    #     user_email=self.account.get_email()
    #     self.account.enter_email("update_"+user_email)
    #     self.account.click_apply_changes_button()
    #     self.account.verify_popup_Updating_email_will_not_change_Username()
    #     self.account.verify_popup_Updating_email_will_not_change_Username_description()
    #     self.account.verify_popup_continue_button()