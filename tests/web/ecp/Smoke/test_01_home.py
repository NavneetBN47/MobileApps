import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "ECP"

class Test_01_ECP_Home(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.login = self.fc.fd["login"]
        self.hpid = self.fc.fd["hpid"]
        self.home = self.fc.fd["home"]
        self.devices = self.fc.fd["devices"]
        self.users = self.fc.fd["users"]
        self.account = self.fc.fd["account"]
        self.es = self.fc.fd["endpoint_security"]

        self.t_account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.t_account["email"]
        self.hpid_password = self.t_account["password"]
        self.customer = self.t_account["customer"]
    
    def test_01_verify_side_menu(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29092660
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.verify_home_menu_btn()
        # self.home.verify_my_organization_menu_btn()
        # self.home.verify_dashboard_menu_btn()
        self.home.verify_devices_menu_btn()
        self.home.verify_users_menu_btn()
        self.home.verify_reports_menu_btn()
        # self.home.verify_account_menu_btn()
        # self.home.verify_customers_menu_btn()
        self.home.verify_policies_menu_btn()
        self.home.verify_solutions_menu_btn()
        # self.home.verify_customer_selector_displayed()
        self.home.verify_command_center_header()
        self.home.verify_home_breadcrumb()
        # self.home.click_dashboard_menu_btn()
        self.home.verify_page_title(self.customer)
        
    def test_02_verify_total_devices_link(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29309055
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.verify_home_menu_btn()
        # self.home.click_dashboard_menu_btn()
        self.home.verify_devices_widget()
        sleep(5) #wait for the widget to load data
        self.home.click_status_total_online_device_btn()
        self.devices.verify_page_title("Devices")

    def test_03_verify_total_users_link(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29309056
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.verify_home_menu_btn()
        # self.home.click_dashboard_menu_btn()
        self.home.verify_devices_widget()
        self.home.click_status_total_users_btn()
        self.home.verify_page_title("Users")

    def test_04_verify_account_profile_from_user_icon(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29236604
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.verify_home_menu_btn()
        # self.home.click_dashboard_menu_btn()
        self.home.click_user_icon_top_right()   
        self.home.click_user_icon_menu_account_profile_item()
        self.account.verify_account_profile_page()

    def test_05_verify_es_mfe_view_details_button(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29297871
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.verify_home_menu_btn()      
        # self.home.click_dashboard_menu_btn()
        self.home.verify_es_mfe()
        self.home.click_es_view_details_btn()
        self.es.verify_page_title("HP Secure Fleet Manager")

    def test_06_logout(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29236606
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.logout()
        self.login.verify_ecp_login()
        self.login.enter_email_address(self.hpid_username)
        self.login.click_next_btn()
        # self.hpid.verify_hp_id_sign_in()
    
    def test_07_verify_user_icon_design(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29309039
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.verify_home_menu_btn() 
        self.home.click_user_icon_top_right()   
        self.home.click_user_icon_menu_account_profile_item()
        self.account.verify_account_profile_page()
        user_first_name=self.account.get_first_name()
        user_last_name=self.account.get_last_name()
        expected_user_icon_text = user_first_name[0]+user_last_name[0]
        actual_user_icon_text = self.home.get_user_icon_initial()
        assert actual_user_icon_text == expected_user_icon_text.upper()

    def test_08_notification_center(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.verify_home_menu_btn()
        self.home.click_notification_bell_button()
        self.home.verify_notifications_popup()
        self.home.verify_notifications_title()

    def test_09_support_and_resources(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.verify_home_menu_btn()
        # self.home.click_dashboard_menu_btn()
        self.home.click_support_center_button()
        self.home.verify_support_and_resources_title()
        self.home.verify_support_center_option_count(7)
        # self.home.verify_support_center_options("Managed Print Service Supporting Portal")
        # self.home.verify_support_center_options("Contact HP Support to get help")
        # self.home.verify_support_center_options("HP Device Connect Fleet Operations")
        self.home.verify_support_center_options("Device Control Center")
        self.home.verify_support_center_options("HP Fleet Proxy")
        # self.home.verify_support_center_options("Managed Print Central")
        self.home.verify_support_center_options("MPS Printer Onboarding Tool")

    @pytest.mark.skip(reason="Skipping this test case as there is no organization assigned to the user")
    def test_10_verify_organization_selection_details(self):
        #
        # For now we are only checking there should be a organization (at least one) for logged in user
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.verify_home_menu_btn()
        self.home.click_user_icon_top_right()
        self.home.verify_organization_count()

    def test_11_verify_device_offline_widget(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.verify_home_menu_btn()
        # self.home.click_dashboard_menu_btn()
        self.home.verify_device_offline_widget()
        self.home.verify_devices_widget()
        self.home.verify_device_offline_widget_title()
        self.home.verify_device_offline_widget_view_details_button()
        if self.home.get_devices_widget_offline_device_count() == 0:
            self.home.verify_device_offline_widget_no_offline_devices_warnign_icon()
            self.home.verify_device_offline_widget_no_offline_devices_warnign_message()
            self.home.verify_device_offline_widget_view_details_button_disabled()
        else:
            assert self.home.get_devices_widget_offline_device_count() == self.home.get_device_offline_widget_offline_devices_count()
            self.home.click_device_offline_widget_view_details_button()
            self.devices.verify_device_page()