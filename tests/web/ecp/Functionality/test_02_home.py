import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "ECP"

class Test_02_ECP_Home(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.devices = self.fc.fd["devices"]
        self.users = self.fc.fd["users"]
        self.es = self.fc.fd["endpoint_security"]
        self.endpoint_security = self.fc.fd["endpoint_security"]
        self.account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]
        # self.customer = self.account["customer"]
    
    def test_02_verify_notification_mfe_dropdown(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29236612
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.verify_home_menu_btn()
        self.home.click_dashboard_menu_btn()
        self.home.verify_notification_mfe_card()
        # self.home.verify_notification_mfe_filter_dropdown()
      
    def test_03_verify_status_widget_card_UI(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29236638
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.verify_home_menu_btn()
        self.home.click_dashboard_menu_btn()
        self.home.verify_devices_widget()
        sleep(5) #wait for the widget to load data
        self.home.verify_devices_widget_title()

        #verify device status label text like total devices, online, offline
        #self.home.verify_devices_widget_total_devices_header() #Not Available in the Design
        self.home.verify_devices_widget_online_device()
        self.home.verify_devices_widget_offline_device()
        self.home.verify_devices_widget_ready_status_devices()
        self.home.verify_devices_widget_warning_status_devices()
        self.home.verify_devices_widget_error_status_devices()

        #verify users status label text like total users, active and pending
        self.home.verify_users_widget()
        self.home.verify_users_widget_admin()
        self.home.verify_status_widget_users_status_header()
        self.home.verify_status_widget_active_users()
        self.home.verify_status_widget_pending_users()
        self.home.verify_status_widget_expired_users()
    
    def test_04_verify_status_widget_devices_information(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29309054
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.verify_home_menu_btn()
        self.home.click_dashboard_menu_btn()
        self.home.verify_devices_widget()
        
        #get device count from status widget 
        status_widget_total_device_count = self.home.get_devices_widget_total_device_count()
        status_widget_online_device_count = self.home.get_devices_widget_online_device_count()
        status_widget_offline_device_count = self.home.get_devices_widget_offline_device_count()

        #get device count from devices page
        self.home.click_status_total_online_device_btn()
        devices_page_device_count = self.devices.get_devices()

        #verify status widget device count 
        assert status_widget_total_device_count == devices_page_device_count["total_count"]
        assert status_widget_online_device_count == devices_page_device_count["online"]
        assert status_widget_offline_device_count == devices_page_device_count["offline"]


    def test_05_verify_status_widget_users_information(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29309054
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)    
        self.home.click_home_menu_btn()
        self.home.click_dashboard_menu_btn()
        self.home.verify_devices_widget()
        
        #get users count from status widget
        status_widget_total_users_count = self.home.get_status_widget_total_user_count()
        status_widget_active_users_count = self.home.get_status_widget_active_user_count()
        status_widget_pending_users_count = self.home.get_status_widget_pending_user_count()
        status_widget_expired_users_count = self.home.get_status_widget_expired_user_count()
        status_widget_enduser_users_count = self.home.get_status_widget_enduser_user_count()

        #get users count from users page
        self.home.click_status_total_users_btn()
        users_page_user_count = self.users.get_users("IT Admin")

        #verify status widget users count
        assert status_widget_total_users_count == users_page_user_count["total_count"]
        assert status_widget_active_users_count == users_page_user_count["active"]
        assert status_widget_pending_users_count == users_page_user_count["pending"]
        assert status_widget_expired_users_count == users_page_user_count["expired"]
        
        #verify status widget end user users count
        self.home.click_dashboard_menu_btn()
        self.home.verify_devices_widget()

        #get users count from users page
        self.home.click_users_widget_total_end_users_btn()
        users_page_user_count = self.users.get_users("End User")
        assert status_widget_enduser_users_count == users_page_user_count["total_count"]

    def test_06_verify_solution_entitled_widget_card_UI(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/682548926
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.verify_home_menu_btn()
        self.home.click_dashboard_menu_btn()
        self.home.verify_solution_entitled_widget()
        self.home.verify_solution_entitled_widget_title()
        self.home.verify_solution_entitled_view_details_button()
        self.home.verify_solution_entitled_hp_secure_fleet_manager()
        solution_entitled_widget_device_count = self.home.get_solution_entitled_device_count()

        #verify solution entitled widget device count 
        assert solution_entitled_widget_device_count == self.home.get_devices_widget_total_device_count()
        self.home.click_solution_entitled_view_details_button()
        self.es.verify_page_title("Solutions")

    def test_07_verify_hp_secure_fleet_manager_widget_card_UI(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/682548930
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.verify_home_menu_btn()
        self.home.click_dashboard_menu_btn()
        self.home.verify_hp_secure_fleet_manager_widget_title()
        self.home.verify_hp_secure_fleet_manager_view_details_button()
        hp_secure_fleet_manager_widget_device_count = self.home.get_hp_secure_fleet_manager_device_count()

        #verify solution entitled widget device count 
        assert hp_secure_fleet_manager_widget_device_count == self.home.get_devices_widget_total_device_count()

    def test_08_verify_ecp_footer(self):
        # 
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.verify_home_menu_btn()
        self.home.verify_ecp_footer_copyright()
        self.home.verify_ecp_footer_terms_of_service()
        self.home.verify_ecp_footer_privacy_statement()

    def test_09_verify_device_policy_status_widget_card_UI(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.verify_home_menu_btn()
        self.home.click_dashboard_menu_btn()
        self.home.verify_device_policy_status_widget()
        self.home.verify_device_policy_status_widget_title()
        self.home.verify_device_policy_status_view_details_button()
        self.home.click_device_policy_status_view_details_button()
        self.es.verify_page_title("Devices")
        self.endpoint_security.verify_policies_devices_page()