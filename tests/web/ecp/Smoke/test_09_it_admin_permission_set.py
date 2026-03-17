import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "ECP"

class Test_09_ECP_It_Admin_Permisson_Set(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.login = self.fc.fd["login"]
        self.hpid = self.fc.fd["hpid"]
        self.account = self.fc.fd["account"]
        self.users = self.fc.fd["users"]
        self.my_organization = self.fc.fd["my_organization"]
        self.login_account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.login_account["it_admin_email"]
        self.hpid_password = self.login_account["it_admin_password"]

    def test_01_verify_it_admin_permission_set_for_customer_selector(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/683277439
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.verify_customer_selector_displayed(displayed=False)
        self.home.verify_customer_menu_displayed(displayed=False)

    def test_02_verify_it_admin_permission_set_for_support_and_resources(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/683277744
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_support_center_button()
        self.home.verify_support_center_option_count(4)
        self.home.verify_support_center_options("Contact HP Support to get help")
        self.home.verify_support_center_options("Device Control Center")
        self.home.verify_support_center_options("HP Fleet Proxy")
        self.home.verify_support_center_options("MPS Printer Onboarding Tool")
        
    def test_03_verify_it_admin_permission_set_for_my_organization_and_account_profile(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/683277748
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_user_icon_top_right()
        self.home.verify_my_organization_link_displayed(displayed=False)
        self.home.click_user_icon_menu_account_profile_item()
        self.account.verify_account_profile_page()

    def test_04_Verify_admin_user_cannot_remove_themselves(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/29435286
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_users_menu_btn()

        # Verify and wait fors user table data load
        self.users.wait_for(self.users.users_table_data_checkbox_load())

        self.users.search_users(self.hpid_username, timeout=10)

        # Verify admin user checkbox is disabled
        self.users.verify_check_box_is_disabled()
        
        # Verify remove user button should not display after hover right click on the admin user
        self.users.verify_remove_user_button_is_not_displayed(timeout=10)

    def test_05_verify_side_menu(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29092660
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.verify_home_menu_btn()
        self.home.verify_devices_menu_btn()
        self.home.verify_users_menu_btn()
        self.home.verify_reports_menu_btn()
        self.home.verify_account_menu_btn()
        self.home.verify_customer_menu_displayed(displayed=False)
        self.home.verify_policies_menu_btn()
        self.home.verify_solutions_menu_btn()
        self.home.verify_proxies_menu_btn()

    def test_06_verify_account_profile_screen(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29093042
        #this test case verify account profile screen's objects and its label name
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_account_menu_btn()
        self.account.verify_page_title(page_title="Account")
        self.account.verify_account_profile_card()
        self.account.verify_account_profile_card_title()
        self.account.verify_account_profile_card_description()
        self.account.click_account_profile_card()
        self.account.verify_page_title(page_title="Account Profile")
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
    def test_07_verify_update_user_profile(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29093169
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_account_menu_btn()
        self.account.verify_account_profile_card()
        self.account.click_account_profile_card()

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

    def test_08_verify_contextual_footer(self):

        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_account_menu_btn()
        self.account.verify_account_profile_card()
        self.account.click_account_profile_card()
        self.account.verify_account_profile_page()
        
        #  Verify the contextual footer is not displayed by default
        self.account.verify_account_profile_contextual_footer_is_not_displayed()
       
        # update account details 
        self.account.enter_first_name("update_")
       
        # Verify contextual_footer is displayed after enter either first name or last name
        self.account.verify_account_profile_contextual_footer_is_displayed()
        self.account.verify_cancel_button_is_displayed()
        self.account.verify_apply_changes_button()

    def test_09_verify_account_profile_cancel_button(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29093158
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_account_menu_btn()
        self.account.verify_account_profile_card()
        self.account.click_account_profile_card()
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

    def test_10_verify_account_profile_organization_tab_screen(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/692849516
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_account_menu_btn()
        self.account.verify_account_profile_card()
        self.account.click_account_profile_card()
        self.account.click_organization_tab()
        self.account.verify_uid()
        self.account.verify_uid_is_disabled()  
        self.account.verify_organizations_name()
        self.account.verify_organization_name_label()
        self.account.verify_organization_description()
        self.account.verify_organization_desc_label()

    def test_11_verify_account_profile_organization_tab_contextual_footer(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_account_menu_btn()
        self.account.verify_account_profile_card()
        self.account.click_account_profile_card()
        self.account.click_organization_tab()
        self.account.verify_cancel_button_is_not_displayed()
        self.account.enter_organization_name("update_")
        self.account.verify_cancel_button_is_displayed()
        self.account.verify_apply_changes_button_is_displayed()

    def test_12_verify_organization_tab_contextual_footer_cancel_button_functionality(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_account_menu_btn()
        self.account.verify_account_profile_card()
        self.account.click_account_profile_card()
        self.account.click_organization_tab()

        # Get organization details 
        org_name=self.account.get_organization_name()
        org_desc=self.account.get_organization_desc()

        # update organization details 
        self.account.enter_organization_name("update_"+org_name)
        self.account.enter_organization_desc("update_"+org_desc)
        self.account.click_cancel_button()

        # Verify organization details are reverted back to previous
        self.account.verify_organization_name(org_name)
        self.account.verify_organization_desc(org_desc)

    @pytest.mark.skip
    def test_13_verify_update_organization_details(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/704084558
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_account_menu_btn()
        self.account.verify_account_profile_card()
        self.account.click_account_profile_card()
        self.account.click_organization_tab()

        # Get organization details 
        org_name=self.account.get_organization_name()
        org_desc=self.account.get_organization_desc()

        # update organization details 
        self.account.enter_organization_name("update_"+org_name)
        self.account.enter_organization_desc("update_"+org_desc)
        self.account.click_apply_changes_button()
        self.account.verify_toast_notification()

        # Verify organization details
        self.account.dismiss_toast()
        self.account.verify_organization_name("update_"+org_name)
        self.account.verify_organization_desc("update_"+org_desc)

        # reverback updated organization details
        self.account.enter_organization_name(org_name)
        self.account.enter_organization_desc(org_desc)
        self.account.click_apply_changes_button()
        self.account.verify_toast_notification()

    def test_14_verify_unsaved_changes_popup(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_account_menu_btn()
        self.account.verify_account_profile_card()
        self.account.click_account_profile_card()
        self.account.click_organization_tab()

        # Update organization details
        org_name=self.account.get_organization_name()
        org_desc=self.account.get_organization_desc() 
        self.account.enter_organization_name("update_"+org_name)
        self.account.enter_organization_desc("update_"+org_desc)

        # Navigate to users without saving organization details
        self.home.click_users_menu_btn()

        # Verfify Unsaved chnages pop-up
        self.account.verify_unsaved_changes_popup_title()
        self.account.verify_unsaved_changes_popup_desc()
        self.account.verify_unsaved_changes_popup_cancel_button()
        self.account.verify_unsaved_changes_popup_leave_button()

    def test_15_verify_unsaved_popup_cancel_button_functinality(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_account_menu_btn()
        self.account.verify_account_profile_card()
        self.account.click_account_profile_card()
        self.account.click_organization_tab()
       
         # Update organization details
        org_name=self.account.get_organization_name()
        org_desc=self.account.get_organization_desc() 
        self.account.enter_organization_name("update_"+org_name)
        self.account.enter_organization_desc("update_"+org_desc)

        #Navigate to home screen without saving organization details
        self.home.click_home_menu_btn()

        # Verify unsaved chnages pop-up
        self.account.click_unsaved_changes_popup_cancel_button()

        # Verify acount profile screen
        self.account.verify_page_title(page_title="Account Profile")

    def test_16_verify_unsaved_popup_leave_button_functinality(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_account_menu_btn()
        self.account.verify_account_profile_card()
        self.account.click_account_profile_card()
        self.account.click_organization_tab()
       
         # Update organization details
        org_name=self.account.get_organization_name()
        org_desc=self.account.get_organization_desc() 
        self.account.enter_organization_name("update_"+org_name)
        self.account.enter_organization_desc("update_"+org_desc)

        #Navigate to home screen without saving organization details
        self.home.click_home_menu_btn()
        self.account.click_unsaved_changes_popup_leave_button()

        #Verify Home screen
        self.home.verify_home_breadcrumb()

    def test_17_verify_switching_to_personal_tab_without_saving_organization_details(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_account_menu_btn()
        self.account.verify_account_profile_card()
        self.account.click_account_profile_card()
        self.account.click_organization_tab()

        # Update Organization details
        self.account.enter_organization_desc("Organization Name")

        # Naviate to persional tab without saving organization details
        self.account.click_personal_tab()

        # Verify that user should not navigate to Personal tab
        self.account.verify_personal_tab_is_not_selected()
       
    def test_18_verify_switching_to_organization_tab_without_saving_personal_details(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_account_menu_btn()
        self.account.verify_account_profile_card()
        self.account.click_account_profile_card()
        self.account.click_personal_tab()

        # Update personnal details
        self.account.enter_first_name("update_")

        # Naviate to organization tab without saving personal details
        self.account.click_organization_tab()

        # Verify that user should not navigate to Organization tab
        self.account.verify_organization_tab_is_not_selected()   

    # Notification Settings Screen was removed from the ECP UI, So commenting out the below test cases
    @pytest.mark.skip 
    def test_19_verify_notification_settings_screen_ui(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.verify_home_menu_btn()
        self.home.click_notification_bell_button()
        self.home.click_notification_popup_three_dot_menu_button()
        self.home.verify_notification_settings_option()
        self.home.click_notification_settings_option()
        self.home.verify_page_title(page_title="Notification Settings")
        self.home.verify_notification_settings_all_notification_title()
        self.home.verify_notification_settings_description()
        self.home.verify_notification_settings_email_notification_checkbox_label()
        self.home.verify_notification_settings_email_notification_checkbox()
       
    @pytest.mark.skip 
    def test_20_verify_notification_settings_screen_contextual_footer(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.verify_home_menu_btn()
        self.home.click_notification_bell_button()
        self.home.click_notification_popup_three_dot_menu_button()
        self.home.click_notification_settings_option()
        self.home.click_notification_settings_email_notification_checkbox()

        # verify the contextual footer is displayed after selecting the checkbox
        self.home.verify_notification_settings_contextual_footer_is_displayed()

        self.home.verify_notification_settings_reset_to_default_button
        self.home.verify_notification_settings_cancel_button()
        self.home.verify_notification_settings_save_button()

        # Click the cancel button and verify the contextual footer is no longer displayed
        self.home.click_notification_settings_cancel_button()
        self.home.verify_notification_settings_contextual_footer_is_not_displayed()

    @pytest.mark.skip 
    def test_21_verify_notification_settings_screen_save_button_functionality(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.verify_home_menu_btn()
        self.home.click_notification_bell_button()
        self.home.click_notification_popup_three_dot_menu_button()
        self.home.click_notification_settings_option()

        checkbox_status = self.home.get_notification_settings_email_checkbox_status()

        self.home.click_notification_settings_email_notification_checkbox()
        self.home.click_notification_settings_save_button()

        checkbox_status != self.home.get_notification_settings_email_checkbox_status()

    @pytest.mark.skip
    def test_23_verify_notification_settings_reset_to_default_popup_cancel_btn(self):
         #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.verify_home_menu_btn()
        self.home.click_notification_bell_button()
        self.home.click_notification_popup_three_dot_menu_button()
        self.home.click_notification_settings_option()
        self.home.click_notification_settings_email_notification_checkbox()    
        self.home.click_notification_settings_reset_to_default_button()
        self.home.click_notification_settings_reset_to_default_popup_cancel_button()

    @pytest.mark.skip   
    def test_24_verify_notification_settings_reset_to_default_functionlaity(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.verify_home_menu_btn()
        self.home.click_notification_bell_button()
        self.home.click_notification_popup_three_dot_menu_button()
        self.home.click_notification_settings_option()

        # Changing the Email Notification checkbox status
        checkbox_status = self.home.get_notification_settings_email_checkbox_status()
   
        self.home.click_notification_settings_email_notification_checkbox()

        # Click the reset to default button and verify the popup    
        self.home.click_notification_settings_reset_to_default_button()
        self.home.verify_notification_settings_reset_to_default_popup_desc()
        self.home.verify_notification_settings_reset_to_default_popup_cancel_button()
        self.home.verify_notification_settings_reset_to_default_popup_reset_button()
        # Revert back the changes
        self.home.click_notification_settings_reset_to_default_popup_reset_button()
        checkbox_status == self.home.get_notification_settings_email_checkbox_status()