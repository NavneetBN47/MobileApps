import pytest
from MobileApps.libs.ma_misc import ma_misc
from time import sleep
pytest.app_info = "WEX"
import random
from MobileApps.libs.flows.web.wex.wex_api_utility import *

#Generate random proxy name
proxy_name = "autoproxy_"+str(random.randint(1000,9999))

class Test_08_Workforce_Devices_Print_Proxies(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, wex_setup, request):
        self = self.__class__
        self.driver, self.fc = wex_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.print_proxies = self.fc.fd["fleet_management_printproxies"]
        self.printers = self.fc.fd["fleet_management_devices"]
        self.dashboard = self.fc.fd["fleet_management_dashboard"]
        if "sanity" in request.config.getoption("-m"):
            self.account = ma_misc.get_wex_account_info(self.stack)
            self.hpid_username = self.account["ldk_sanity_email"]
            self.hpid_password = self.account["ldk_sanity_password"]
        else:
            self.account = ma_misc.get_wex_account_info(self.stack)
            self.hpid_username = self.account["customer_email"]
            self.hpid_password = self.account["customer_password"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_printers(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_dropdown_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.print_proxies.click_devices_proxies_button()
        self.print_proxies.verify_fleet_management_print_proxies_breadcrumb()
        self.print_proxies.verify_print_proxies_table_data_load()

    @pytest.mark.sanity
    def test_01_verify_print_proxies_landing_page(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128846
        expected_table_headers = ["Proxy Name","Connectivity","Connectivity Status Changed","Date Added","Devices","Host Name","Description"]
        self.print_proxies.verify_print_proxies_search_textbox()
        self.print_proxies.verify_print_proxies_filter_button()
        self.print_proxies.verify_print_proxies_download_button()
        self.print_proxies.verify_print_proxies_add_button()
        self.print_proxies.verify_print_proxies_column_option_gear_button()
        self.print_proxies.verify_print_proxies_proxies_table()
        self.print_proxies.verify_print_proxies_table_data_load()
        assert expected_table_headers == self.print_proxies.verify_proxies_table_headers()

    @pytest.mark.sanity
    # Testcase will be removed or modified in future: Design change in UI
    def test_02_verify_proxies_tab_breadcrumb_and_navigation(self):
        #
        self.print_proxies.verify_fleet_management_print_proxies_breadcrumb()
 
        # Verify Print Proxies page url
        self.print_proxies.verify_print_proxies_page_url(self.stack)

    def test_03_verify_proxies_pagination(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128853
        self.print_proxies.verify_all_page_size_options([5, 25, 50, 100, 500])
        self.print_proxies.verify_table_displaying_correctly(5, page=1)
        self.print_proxies.verify_table_displaying_correctly(25, page=1)
        self.print_proxies.verify_table_displaying_correctly(50, page=1)
        self.print_proxies.verify_table_displaying_correctly(100, page=1)
        self.print_proxies.verify_table_displaying_correctly(500, page=1)

    @pytest.mark.sanity
    def test_04_verify_proxies_filter_side_bar_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128854 
        self.print_proxies.verify_print_proxies_table_data_load()
        self.print_proxies.verify_print_proxies_filter_button()   
        self.print_proxies.click_print_proxies_filter_button()
        self.print_proxies.verify_filter_side_bar_title()
        self.print_proxies.verify_filter_side_bar_description()
        self.print_proxies.verify_filter_side_bar_search_box()
        self.print_proxies.verify_filter_side_bar_connectivity_label()
        self.print_proxies.click_filter_side_bar_close_button()
        self.print_proxies.verify_filter_side_bar_title(displayed=False)

    @pytest.mark.sanity
    @pytest.mark.parametrize('filter_name', ["Online", "Offline"])
    def test_05_verify_proxies_filter_functionality(self,filter_name):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128854
        
        self.print_proxies.verify_print_proxies_filter_button()  
        self.print_proxies.click_print_proxies_filter_button()
        self.print_proxies.select_filter(filter_name)
        self.print_proxies.verify_filter_in_proxies_table(filter_name)
        self.print_proxies.click_filter_side_bar_close_button()
        self.print_proxies.verify_filter_side_bar_connectivity_status_tags(filter_name)
        self.print_proxies.click_filter_side_bar_connectivity_status_tag_close_tag()
    
    @pytest.mark.sanity
    def test_06_verify_filter_connectivity_status_clear_all_tag(self):
        #
        self.print_proxies.verify_print_proxies_table_data_load()
        self.print_proxies.verify_print_proxies_filter_button()  
        self.print_proxies.click_print_proxies_filter_button()
        self.print_proxies.select_filter("Online")
        self.print_proxies.select_filter("Offline")
        self.print_proxies.click_filter_side_bar_close_button()
        self.print_proxies.verify_filter_side_bar_connectivity_status_clear_all_tag()
        self.print_proxies.click_filter_side_bar_connectivity_status_clear_all_tag()
        self.print_proxies.verify_filter_side_bar_connectivity_online_tag_is_not_displayed()
        self.print_proxies.verify_filter_side_bar_connectivity_offline_tag_is_not_displayed()

    @pytest.mark.sanity
    def test_07_verify_print_proxies_filter_clear_all_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128854
        self.print_proxies.verify_print_proxies_table_data_load()
        self.print_proxies.click_print_proxies_filter_button()

        #verify no.of items selected text 
        self.print_proxies.select_filter("Online")
        self.print_proxies.verify_print_proxies_filter_items_selected_text_displayed()
        assert "1 items selected" == self.print_proxies.get_print_proxies_filter_items_selected_text()
        self.print_proxies.verify_print_proxies_filter_clear_all_button()

        #verify no.of items selected text 
        self.print_proxies.select_filter("Offline")
        self.print_proxies.verify_print_proxies_filter_items_selected_text_displayed()
        assert "2 items selected" == self.print_proxies.get_print_proxies_filter_items_selected_text()

        #verify clear all button functionality
        self.print_proxies.click_print_proxies_filter_clear_all_button()
        self.print_proxies.verify_print_proxies_filter_items_selected_text_displayed(displayed=False)

    @pytest.mark.sanity
    def test_08_verify_column_option_popup_save_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128852

        self.print_proxies.click_print_proxies_column_option_gear_button()
        self.print_proxies.click_column_option("Connectivity")
        self.print_proxies.click_column_options_popup_save_button()

        # Verify Customers table Domain Column
        self.print_proxies.verify_print_proxies_table_data_load()
        self.print_proxies.verify_print_proxies_table_column("Connectivity",displayed=False)

        # Reverting the Column option changes
        self.print_proxies.click_print_proxies_column_option_gear_button()
        self.print_proxies.click_column_option("Connectivity")
        self.print_proxies.click_column_options_popup_save_button()
        self.print_proxies.verify_print_proxies_table_column("Connectivity")

    @pytest.mark.sanity
    def test_09_verify_column_option_popup_cancel_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128852

        self.print_proxies.click_print_proxies_column_option_gear_button()
        self.print_proxies.click_column_option("Connectivity")
        self.print_proxies.click_column_options_popup_cancel_button()

        # Verify proxies table connectivity Column
        self.print_proxies.verify_print_proxies_table_column("Connectivity")

    @pytest.mark.sanity
    def test_10_verify_column_option_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128847        

        expected_options= ["Proxy Name","Connectivity","Connectivity Status Changed","Date Added","Devices","Host Name","Description","Fleet Proxy Version"]
        self.print_proxies.click_print_proxies_column_option_gear_button()
        self.print_proxies.verify_column_options_popup_title()
        self.print_proxies.verify_column_options_popup_reset_to_default_button()
        self.print_proxies.verify_column_options_popup_cancel_button()
        self.print_proxies.verify_column_options_popup_save_button()
        assert expected_options == self.print_proxies.get_column_options_popup_options()

    @pytest.mark.sanity
    def test_11_verify_verify_proxy_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128860
        self.print_proxies.verify_print_proxies_table_data_load()
        self.print_proxies.verify_print_proxies_add_button()
        self.print_proxies.click_print_proxies_add_button()
        self.print_proxies.verify_verify_proxy_popup_title()
        self.print_proxies.verify_verify_proxy_popup_description()
        self.print_proxies.verify_verify_proxy_popup_code_label()
        self.print_proxies.verify_verify_proxy_popup_code_text_box()
        self.print_proxies.verify_verify_proxy_popup_note()
        self.print_proxies.verify_verify_proxy_popup_cancel_button()
        self.print_proxies.verify_verify_proxy_popup_verify_button()
        self.print_proxies.click_verify_proxy_popup_verify_button()
        assert "Code is required." == self.print_proxies.get_verify_proxy_popup_code_text_box_tooltip_msg()
        self.print_proxies.click_verify_proxy_popup_cancel_button()
        self.print_proxies.verify_verify_proxy_popup_title(displayed=False)

    @pytest.mark.sanity
    def test_12_verify_proxy_verified_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128859
        self.print_proxies.verify_print_proxies_table_data_load()
        self.print_proxies.click_print_proxies_add_button()
        proxy_code = get_fleet_proxy_verification_code(self.stack)
        self.print_proxies.enter_code(proxy_code)
        self.print_proxies.click_verify_proxy_popup_verify_button()
        sleep(5) # Need to wait for the verification animation to complete
        self.print_proxies.verify_proxy_verified_popup_title()
        self.print_proxies.verify_proxy_verified_popup_cancel_button()
        self.print_proxies.verify_proxy_verified_popup_allow_button()
        self.print_proxies.click_proxy_verified_popup_cancel_button()
        self.print_proxies.verify_proxy_verified_popup_title(displayed=False)
    
    @pytest.mark.sanity
    def test_13_verify_add_printers_popup_ui(self):
        #
        self.print_proxies.click_print_proxies_download_button()
        self.print_proxies.verify_add_printers_popup_title()
        self.print_proxies.verify_add_printers_popup_description()
        self.print_proxies.verify_add_printers_popup_view_instructions_link()
        self.print_proxies.verify_add_printers_popup_done_button()
        self.print_proxies.verify_add_printers_popup_hp_print_fleet_proxy_download_button()
        self.print_proxies.verify_add_printers_popup_hp_print_fleet_proxy_download_button_title()
        self.print_proxies.verify_add_printers_popup_hp_print_fleet_proxy_download_button_version()
        self.print_proxies.verify_add_printers_popup_hp_print_fleet_proxy_download_button_icon()
        self.print_proxies.click_add_printers_popup_done_button()
        self.print_proxies.verify_print_proxies_table_data_load()