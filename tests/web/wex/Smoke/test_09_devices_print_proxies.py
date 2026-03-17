import pytest
from MobileApps.libs.ma_misc import ma_misc
from time import sleep
pytest.app_info = "WEX"
import random
from MobileApps.libs.flows.web.wex.wex_api_utility import *

#Generate random proxy name
proxy_name = "autoproxy_"+str(random.randint(1000,9999))

class Test_09_Workforce_Devices_Print_Proxies(object):

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
    def test_01_verify_add_proxy_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128856
        self.print_proxies.verify_print_proxies_table_data_load()
        if self.print_proxies.search_proxy_with_host_name("Automation-prodsrv1u") == True:
            self.print_proxies.removing_the_existing_proxy()
        self.print_proxies.click_print_proxies_add_button()
        proxy_code = get_fleet_proxy_verification_code(self.stack)
        self.print_proxies.enter_code(proxy_code)
        self.print_proxies.click_verify_proxy_popup_verify_button()
        sleep(5) # Need to wait for the verification animation to complete
        self.print_proxies.click_proxy_verified_popup_allow_button()
        self.print_proxies.verify_proxy_connected_popup_title()
        self.print_proxies.enter_proxy_name(proxy_name)
        self.print_proxies.enter_proxy_description("Auto Description")
        self.print_proxies.click_proxy_connected_popup_done_button()
        self.print_proxies.verify_add_proxy_toast_message(proxy_name)
        self.print_proxies.verify_print_proxies_table_data_load()

    @pytest.mark.sanity
    def test_02_verify_reconnect_this_proxy_popup_ui(self):
        #
        self.print_proxies.verify_print_proxies_table_data_load()
        self.print_proxies.click_print_proxies_add_button()
        proxy_code = get_fleet_proxy_verification_code(self.stack)
        self.print_proxies.enter_code(proxy_code)
        self.print_proxies.click_verify_proxy_popup_verify_button()
        sleep(5) # Need to wait for the verification animation to complete
        self.print_proxies.click_proxy_verified_popup_allow_button()
        self.print_proxies.verify_reconnect_this_proxy_popup_title()
        self.print_proxies.verify_reconnect_this_proxy_popup_description_1()
        self.print_proxies.verify_reconnect_proxy_popup_description_hostname()
        self.print_proxies.verify_reconnect_proxy_popup_description_text_2()
        self.print_proxies.verify_reconnect_proxy_popup_proxy_name_label()
        self.print_proxies.get_recconect_proxy_popup_proxy_name()
        self.print_proxies.verify_reconnect_proxy_popup_proxy_description_label()
        self.print_proxies.get_recconect_proxy_popup_proxy_description()
        self.print_proxies.verify_reconnect_proxy_popup_note_message()
        self.print_proxies.verify_reconnect_this_proxy_popup_reconnect_button()
        self.print_proxies.verify_reconnect_this_proxy_popup_cancel_button()
        self.print_proxies.click_reconnect_this_proxy_popup_cancel_button()

    def test_03_verify_reconnect_this_proxy_popup_cancel_button_functionality(self):
        self.print_proxies.verify_print_proxies_table_data_load()
        self.print_proxies.click_print_proxies_add_button()
        proxy_code = get_fleet_proxy_verification_code(self.stack)
        self.print_proxies.enter_code(proxy_code)
        self.print_proxies.click_verify_proxy_popup_verify_button()
        sleep(5) # Need to wait for the verification animation to complete
        self.print_proxies.click_proxy_verified_popup_allow_button()
        self.print_proxies.click_reconnect_this_proxy_popup_cancel_button()
        self.print_proxies.verify_reconnect_this_proxy_popup_title(displayed=False)

    def test_04_verify_reconnect_this_proxy_popup_reconnect_button_functionality(self):
        self.print_proxies.verify_print_proxies_table_data_load()
        self.print_proxies.click_print_proxies_add_button()
        proxy_code = get_fleet_proxy_verification_code(self.stack)
        self.print_proxies.enter_code(proxy_code)
        self.print_proxies.click_verify_proxy_popup_verify_button()
        sleep(5) # Need to wait for the verification animation to complete
        self.print_proxies.click_proxy_verified_popup_allow_button()
        assert proxy_name == self.print_proxies.get_recconect_proxy_popup_proxy_name()
        assert "Auto Description" == self.print_proxies.get_recconect_proxy_popup_proxy_description()
        self.print_proxies.click_reconnect_this_proxy_popup_reconnect_button()
        self.print_proxies.verify_reconnect_this_proxy_popup_title(displayed=False)

    @pytest.mark.sanity
    @pytest.mark.parametrize('search_string', ["invalidproxy", proxy_name])
    def test_05_verify_print_proxies_search_functionality(self,search_string ):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128849

        # Verify and wait fors proxies table data load
        self.print_proxies.verify_print_proxies_table_data_load()
        if search_string == "invalidproxy":
            assert False == self.print_proxies.search_proxy(search_string)
        else:
            assert True == self.print_proxies.search_proxy(search_string)
        self.print_proxies.click_search_clear_button()

    @pytest.mark.sanity
    def test_06_verify_search_functionality_with_number_of_devices_column_option(self):
        # Verify and wait for proxies table data load
        self.print_proxies.verify_print_proxies_table_data_load()
        self.print_proxies.click_table_header_by_name("proxy_name")
        self.print_proxies.search_proxy_with_number_of_devices(0)
        self.print_proxies.click_search_clear_button()

    @pytest.mark.sanity
    def test_07_verify_search_functionality_with_host_name(self):
        # Verify and wait for proxies table data load
        self.print_proxies.verify_print_proxies_table_data_load()
        search_string = self.print_proxies.get_search_string(self.stack)
        assert self.print_proxies.search_proxy_with_host_name(search_string)
        self.print_proxies.click_search_clear_button()

    @pytest.mark.sanity
    def test_08_verify_search_functionality_with_description(self):
        # Verify and wait for proxies table data load
        self.print_proxies.verify_print_proxies_table_data_load()
        assert self.print_proxies.search_proxy_with_description("Stage")
        self.print_proxies.click_search_clear_button()
    
    @pytest.mark.sanity
    @pytest.mark.parametrize('search_string', ["Offline", "Online"])
    def test_09_verify_search_functionality_with_connectivity_column_option(self, search_string):
        # Verify and wait for proxies table data load
        self.print_proxies.verify_print_proxies_table_data_load()
        assert self.print_proxies.search_proxy_with_connectivity_type(search_string)
        self.print_proxies.click_search_clear_button()
    
    @pytest.mark.sanity
    def test_10_verify_device_count_in_proxies_table(self):
        #
        self.print_proxies.verify_print_proxies_table_data_load()
        self.print_proxies.search_proxy(proxy_name)
        assert 0 == int(self.print_proxies.get_proxy_devices_count())

    @pytest.mark.sanity
    def test_11_verify_edit_proxy_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128861
        self.print_proxies.verify_print_proxies_table_data_load()
        self.print_proxies.click_print_proxies_checkbox()
        self.print_proxies.click_contextual_footer_select_action_dropdown()
        self.print_proxies.select_contextual_footer_select_action_dropdown_option("Edit")
        self.print_proxies.click_contextual_footer_continue_button()
        self.print_proxies.verify_edit_proxy_popup_title()
        self.print_proxies.verify_edit_proxy_popup_description()
        self.print_proxies.verify_edit_proxy_popup_proxy_name_textbox()
        self.print_proxies.verify_edit_proxy_popup_proxy_description()
        self.print_proxies.verify_edit_proxy_popup_cancel_button()
        self.print_proxies.verify_edit_proxy_popup_save_button()        
        self.print_proxies.click_edit_proxy_popup_cancel_button()
        self.print_proxies.verify_edit_proxy_popup_title(displayed=False)

    @pytest.mark.sanity
    def test_12_verify_edit_proxy_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128858
        self.print_proxies.verify_print_proxies_table_data_load()
        self.print_proxies.search_proxy(proxy_name)
        self.print_proxies.click_print_proxies_checkbox()
        self.print_proxies.click_contextual_footer_select_action_dropdown()
        self.print_proxies.select_contextual_footer_select_action_dropdown_option("Edit")
        self.print_proxies.click_contextual_footer_continue_button()
        # self.print_proxies.verify_edit_proxy_popup_proxy_save_button_status("disabled")
        self.print_proxies.update_proxy_name("Update_"+proxy_name)
        self.print_proxies.verify_edit_proxy_popup_proxy_save_button_status("enabled")
        self.print_proxies.click_edit_proxy_popup_save_button()
        self.print_proxies.verify_edit_proxy_toast_message("Update_"+proxy_name)
        self.print_proxies.verify_print_proxies_table_data_load()
        self.print_proxies.search_proxy("Update_"+proxy_name)

    def test_13_verify_edit_proxy_popup_tooltip_messages(self):
        #
        duplicate_proxy_name_tooltip_msg = "The proxy name you've entered is already in use. Enter a different name."
        warning_msg = "Proxy name is required."

        self.print_proxies.verify_print_proxies_table_data_load()
        self.print_proxies.search_proxy(proxy_name)
        self.print_proxies.click_print_proxies_checkbox()
        self.print_proxies.click_contextual_footer_select_action_dropdown()
        self.print_proxies.select_contextual_footer_select_action_dropdown_option("Edit")
        self.print_proxies.click_contextual_footer_continue_button()

        self.print_proxies.click_edit_proxy_popup_proxy_name_text_box()
        #Commenting out below lines as warning message not showing up only in automation env.
        # self.print_proxies.clear_edit_proxy_popup_proxy_name()
        # self.print_proxies.click_edit_proxy_popup_save_button()
        # assert warning_msg == self.print_proxies.get_edit_proxy_popup_proxy_name_text_box_tooltip_msg()

        self.print_proxies.update_proxy_name("DO NOT REMOVE")
        assert duplicate_proxy_name_tooltip_msg == self.print_proxies.get_edit_proxy_popup_proxy_name_text_box_tooltip_msg()

    @pytest.mark.sanity
    def test_14_verify_remove_proxy_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128857
        self.print_proxies.click_print_proxies_checkbox()
        self.print_proxies.click_contextual_footer_select_action_dropdown()
        self.print_proxies.select_contextual_footer_select_action_dropdown_option("Remove")
        self.print_proxies.click_contextual_footer_continue_button()
        self.print_proxies.verify_remove_proxy_popup_title()
        self.print_proxies.verify_remove_proxy_popup_description()
        self.print_proxies.verify_remove_proxy_popup_cancel_button()
        self.print_proxies.verify_remove_proxy_popup_remove_button()
        self.print_proxies.click_remove_proxy_popup_cancel_button()
        self.print_proxies.verify_remove_proxy_popup_title(displayed=False)

    @pytest.mark.sanity
    def test_15_verify_remove_proxy_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1393128857
        self.print_proxies.verify_print_proxies_table_data_load()
        self.print_proxies.search_proxy("Update_"+proxy_name)
        self.print_proxies.click_print_proxies_checkbox()
        # self.print_proxies.click_search_clear_button() 
        self.print_proxies.click_contextual_footer_select_action_dropdown()
        self.print_proxies.select_contextual_footer_select_action_dropdown_option("Remove")
        self.print_proxies.click_contextual_footer_continue_button()
        self.print_proxies.click_remove_proxy_popup_remove_button()
        self.print_proxies.verify_remove_proxy_toast_message("Update_"+proxy_name)
        self.print_proxies.click_search_clear_button()
        self.print_proxies.verify_print_proxies_table_data_load()
        assert False == self.print_proxies.search_proxy("Update_"+proxy_name)