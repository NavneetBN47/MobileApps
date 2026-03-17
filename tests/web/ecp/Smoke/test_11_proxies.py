import pytest
from SAF.misc import saf_misc
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.web.ecp.ecp_api_utility import *
import random

pytest.app_info = "ECP"

#Generate random proxy name
proxy_name = "autoproxy_"+str(random.randint(1000,9999))

class Test_11_ECP_Proxies(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.login = self.fc.fd["login"]
        self.hpid = self.fc.fd["hpid"]
        self.proxies = self.fc.fd["proxies"]
        self.devices = self.fc.fd["devices"]
        self.login_account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.login_account["fp_email"]
        self.hpid_password = self.login_account["fp_password"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_proxies(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_proxies_menu_btn()
        return self.proxies.verify_page_title(page_title="Proxies")

    def test_00_verify_proxies_landing_page(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/34334868
        self.proxies.verify_page_title(page_title="Proxies")
        self.proxies.verify_proxies_refresh_button()
        self.proxies.verify_proxies_tab()
        self.proxies.verify_proxies_settings_tab()

    def test_01_verify_proxies_page_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33733061
        # https://hp-testrail.external.hp.com/index.php?/cases/view/34036288
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33727809

        self.proxies.verify_proxies_table_data_load()
        self.proxies.verify_proxies_search_box()
        self.proxies.verify_proxies_filter_button()
        self.proxies.verify_proxies_add_button()
        self.proxies.verify_proxies_column_option_gear_button()
        self.proxies.verify_proxies_table()        
    
    def test_02_verify_proxies_refresh_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33654063

        cur_time = self.proxies.get_sync_time_info()
        sleep(1)
        self.proxies.click_refresh_button()
        new_time = self.proxies.get_sync_time_info()
        assert saf_misc.compare_time_in_utc(new_time.split("Last Updated ")[1], self.driver.get_timezone(), "%b %d, %Y %I:%M:%S %p") == True
        assert new_time != cur_time

    def test_03_verify_proxies_pagination(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33654227
        
        self.proxies.verify_all_page_size_options_new([5, 25, 50, 100, 500])
        self.proxies.verify_table_displaying_correctly_new(5, page=1)
        self.proxies.verify_table_displaying_correctly_new(25, page=1)
        self.proxies.verify_table_displaying_correctly_new(50, page=1)
        self.proxies.verify_table_displaying_correctly_new(100, page=1)
        self.proxies.verify_table_displaying_correctly_new(500, page=1)

    @pytest.mark.parametrize('filter_name', ["Online","Offline"])
    def test_04_verify_proxies_filter_functionality(self,filter_name):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33654068
        
        self.proxies.verify_proxies_table_data_load()
        self.proxies.click_proxies_filter_button()
        self.proxies.select_filter(filter_name)
        self.proxies.verify_filter_in_proxies_table(filter_name)

    def test_05_verify_proxies_filter_side_bar_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33733166
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33733175
        
        self.proxies.verify_proxies_table_data_load()
        self.proxies.click_proxies_filter_button()
        self.proxies.verify_filter_side_bar_title()
        self.proxies.verify_filter_side_bar_description()
        self.proxies.verify_filter_side_bar_search_box()
        self.proxies.verify_filter_side_bar_connectivity_label()
        self.proxies.click_filter_side_bar_close_button()
        self.proxies.verify_filter_side_bar_title(displayed=False)

    def test_06_verify_proxies_contextual_footer_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33654201
        # https://hp-testrail.external.hp.com/index.php?/cases/view/34046102
        
        self.proxies.verify_proxies_table_data_load()
        self.proxies.click_proxies_checkbox()
        self.proxies.verify_contextual_footer()
        self.proxies.verify_contextual_footer_cancel_button()
        self.proxies.verify_contextual_footer_selected_item_label()
        self.proxies.verify_contextual_footer_select_action_dropdown()
        self.proxies.verify_contextual_footer_continue_button()
        self.proxies.click_contextual_footer_cancel_button()
        self.proxies.verify_contextual_footer_is_not_displayed()

    def test_07_verify_proxies_contextual_footer_select_action_dropdown_options(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/34043965

        expected_options= ["Edit", "Remove"]
        self.proxies.verify_proxies_table_data_load()
        self.proxies.click_proxies_checkbox()
        self.proxies.verify_contextual_footer()
        self.proxies.click_contextual_footer_select_action_dropdown()
        assert expected_options == self.proxies.get_contextual_footer_select_action_dropdown_options()

    def test_08_verify_column_option_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/edit/33654224        

        expected_options= ["Proxy Name","Connectivity","Connectivity Status Changed","Date Added","Devices","Host Name","Description","Fleet Proxy Version"]
        self.proxies.click_proxies_column_option_gear_button()
        self.proxies.verify_column_options_popup_title()
        self.proxies.verify_column_options_popup_reset_to_default_button()
        self.proxies.verify_column_options_popup_cancel_button()
        self.proxies.verify_column_options_popup_save_button()
        assert expected_options == self.proxies.get_column_options_popup_options()

    def test_09_verify_column_option_popup_save_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33654225

        self.proxies.click_proxies_column_option_gear_button()
        self.proxies.click_column_option("Connectivity")
        self.proxies.click_column_options_popup_save_button()

        # Verify Customers table Domain Column
        self.proxies.verify_proxies_tabel_column("Connectivity",displayed=False)

        # Reverting the Column option changes
        self.proxies.click_proxies_column_option_gear_button()
        self.proxies.click_column_option("Connectivity")
        self.proxies.click_column_options_popup_save_button()
        self.proxies.verify_proxies_tabel_column("Connectivity")

    def test_10_verify_column_option_popup_cancel_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/34043981

        self.proxies.click_proxies_column_option_gear_button()
        self.proxies.click_column_option("Connectivity")
        self.proxies.click_column_options_popup_cancel_button()

        # Verify proxies table connectivity Column
        self.proxies.verify_proxies_tabel_column("Connectivity")

    def test_11_verify_verify_proxy_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/34155821
        # https://hp-testrail.external.hp.com/index.php?/cases/view/34155825
        # https://hp-testrail.external.hp.com/index.php?/cases/view/34155826

        self.proxies.verify_proxies_table_data_load()
        self.proxies.click_proxies_add_button()
        self.proxies.verify_verify_proxy_popup_title()
        self.proxies.verify_verify_proxy_popup_description()
        self.proxies.verify_verify_proxy_popup_code_label()
        self.proxies.verify_verify_proxy_popup_code_text_box()
        self.proxies.verify_verify_proxy_popup_note()
        self.proxies.verify_verify_proxy_popup_cancel_button()
        self.proxies.verify_verify_proxy_popup_verify_button()
        self.proxies.click_verify_proxy_popup_verify_button()
        assert "Code is required." == self.proxies.get_verify_proxy_popup_code_text_box_tooltip_msg()
        self.proxies.click_verify_proxy_popup_cancel_button()
        self.proxies.verify_verify_proxy_popup_title(displayed=False)

    def test_12_verify_proxy_verified_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/34155827
        # https://hp-testrail.external.hp.com/index.php?/cases/view/34261676

        self.proxies.verify_proxies_table_data_load()
        self.proxies.click_proxies_add_button()
        proxy_code = get_fleet_proxy_verification_code(self.stack)
        self.proxies.enter_code(proxy_code)
        self.proxies.click_verify_proxy_popup_verify_button()
        sleep(2) # Need to wait for the verification animation to complete
        self.proxies.verify_proxy_verified_popup_title()
        # self.proxies.verify_proxy_verified_popup_description()
        self.proxies.verify_proxy_verified_popup_cancel_button()
        self.proxies.verify_proxy_verified_popup_allow_button()
        self.proxies.click_proxy_verified_popup_cancel_button()
        self.proxies.verify_proxy_verified_popup_title(displayed=False)

    def test_13_verify_add_proxy_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/34261677
        # https://hp-testrail.external.hp.com/index.php?/cases/view/34155830
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33654070

        self.proxies.verify_proxies_table_data_load()
        if self.proxies.search_proxy("Automation-prodsrv1u") == True:
            self.proxies.removing_the_existing_proxy()
        self.proxies.click_proxies_add_button()
        proxy_code = get_fleet_proxy_verification_code(self.stack)
        self.proxies.enter_code(proxy_code)
        self.proxies.click_verify_proxy_popup_verify_button()
        self.proxies.click_proxy_verified_popup_allow_button()
        self.proxies.verify_proxy_connected_popup_title()
        self.proxies.enter_proxy_name(proxy_name)
        self.proxies.enter_proxy_description("Auto Description")
        self.proxies.click_proxy_connected_popup_done_button()
        sleep(2) # Need to wait for the toast message to appear
        self.proxies.verify_add_proxy_toast_message(proxy_name)

    # def test_14_verify_add_proxy_popup_tooltip_messages(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/33654193

    #     expected_tooltip_msg = "The proxy name is used as the group name for Devices menu."
    #     expected_warning_msg = "Proxy Name is required."

    #     self.proxies.click_proxies_add_button()
    #     self.proxies.click_add_proxy_popup_proxy_name_text_box()
    #     assert expected_tooltip_msg == self.proxies.get_proxy_connected_popup_proxy_name_text_box_tooltip_msg()

    #     self.proxies.click_add_proxy_popup_continue_button()
    #     assert expected_warning_msg == self.proxies.get_proxy_connected_popup_proxy_name_text_box_tooltip_msg()

    @pytest.mark.parametrize('search_string', ["invalidproxy", proxy_name])
    def test_15_verify_proxies_search_functionality(self,search_string ):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33654067

        # Verify and wait fors proxies table data load
        self.proxies.verify_proxies_table_data_load()
        if search_string == "invalidproxy":
            assert False == self.proxies.search_proxy(search_string)
        else:
            assert True == self.proxies.search_proxy(search_string)
        self.proxies.click_search_clear_button()

    def test_16_verify_edit_proxy_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33654209
        # https://hp-testrail.external.hp.com/index.php?/cases/view/34130667

        self.proxies.verify_proxies_table_data_load()
        self.proxies.click_proxies_checkbox()
        self.proxies.click_contextual_footer_select_action_dropdown()
        self.proxies.select_contextual_footer_select_action_dropdown_option("Edit")
        self.proxies.click_contextual_footer_continue_button()
        self.proxies.verify_edit_proxy_popup_title()
        self.proxies.verify_edit_proxy_popup_description()
        self.proxies.verify_edit_proxy_popup_proxy_name_textbox()
        self.proxies.verify_edit_proxy_popup_proxy_description()
        self.proxies.verify_edit_proxy_popup_cancel_button()
        self.proxies.verify_edit_proxy_popup_save_button()        
        self.proxies.click_edit_proxy_popup_cancel_button()
        self.proxies.verify_edit_proxy_popup_title(displayed=False)  

    def test_17_verify_edit_proxy_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33654207
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33654215

        self.proxies.verify_proxies_table_data_load()
        self.proxies.search_proxy(proxy_name)
        self.proxies.click_proxies_checkbox()
        self.proxies.click_contextual_footer_select_action_dropdown()
        self.proxies.select_contextual_footer_select_action_dropdown_option("Edit")
        self.proxies.click_contextual_footer_continue_button()
        self.proxies.update_proxy_name("Update_"+proxy_name)
        self.proxies.click_edit_proxy_popup_save_button()
        self.proxies.verify_edit_proxy_toast_message("Update_"+proxy_name)
        self.proxies.verify_proxies_table_data_load()
        self.proxies.search_proxy("Update_"+proxy_name)

    def test_18_verify_edit_proxy_popup_tooltip_messages(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33746245
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33729160
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33729162

        duplicate_proxy_name_tooltip_msg = "The proxy name you've entered is already in use. Enter a different name."
        warning_msg = "Proxy name is required."

        self.proxies.verify_proxies_table_data_load()
        self.proxies.search_proxy(proxy_name)
        self.proxies.click_proxies_checkbox()
        self.proxies.click_contextual_footer_select_action_dropdown()
        self.proxies.select_contextual_footer_select_action_dropdown_option("Edit")
        self.proxies.click_contextual_footer_continue_button()

        self.proxies.click_edit_proxy_popup_proxy_name_text_box()
        self.proxies.clear_edit_proxy_popup_proxy_name()
        self.proxies.click_edit_proxy_popup_save_button()
        assert warning_msg == self.proxies.get_edit_proxy_popup_proxy_name_text_box_tooltip_msg()

        self.proxies.update_proxy_name("DO NOT REMOVE")
        assert duplicate_proxy_name_tooltip_msg == self.proxies.get_edit_proxy_popup_proxy_name_text_box_tooltip_msg()

    def test_19_verify_remove_proxy_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/edit/33654202
        # https://hp-testrail.external.hp.com/index.php?/cases/edit/33654204

        self.proxies.verify_proxies_table_data_load()
        self.proxies.click_proxies_checkbox()
        self.proxies.click_contextual_footer_select_action_dropdown()
        self.proxies.select_contextual_footer_select_action_dropdown_option("Remove")
        self.proxies.click_contextual_footer_continue_button()
        self.proxies.verify_remove_proxy_popup_title()
        self.proxies.verify_remove_proxy_popup_description()
        self.proxies.verify_remove_proxy_popup_cancel_button()
        self.proxies.verify_remove_proxy_popup_remove_button()
        self.proxies.click_remove_proxy_popup_cancel_button()
        self.proxies.verify_remove_proxy_popup_title(displayed=False)

    def test_20_verify_remove_proxy_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33654203

        self.proxies.verify_proxies_table_data_load()
        self.proxies.search_proxy("Update_"+proxy_name)
        self.proxies.click_proxies_checkbox()
        # self.proxies.click_search_clear_button()
        self.proxies.click_contextual_footer_select_action_dropdown()
        self.proxies.select_contextual_footer_select_action_dropdown_option("Remove")
        self.proxies.click_contextual_footer_continue_button()
        self.proxies.click_remove_proxy_popup_remove_button()
        self.proxies.verify_remove_proxy_toast_message("Update_"+proxy_name)
        self.proxies.click_search_clear_button()
        self.proxies.verify_proxies_table_data_load()
        assert False == self.proxies.search_proxy("Update_"+proxy_name)

    # Sorting is now based on Date Added (Recent top).
    # def test_21_verify_proxies_sort_functionality(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/33654226

    #     self.proxies.verify_proxies_table_data_load()
    #     self.proxies.verify_table_sort("connectivity_status",["Online","Offline"])
    #     self.proxies.click_table_header_by_name("connectivity_status")
    #     self.proxies.verify_table_sort("connectivity_status",["Offline","Online"])

    def test_22_verify_proxies_filter_clear_all_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33733447

        self.proxies.verify_proxies_table_data_load()
        self.proxies.click_proxies_filter_button()

        #verify no.of items selected text 
        self.proxies.select_filter("Online")
        self.proxies.verify_proxies_filter_items_selected_text_displayed()
        assert "1 items selected" == self.proxies.get_proxies_filter_items_selected_text()
        self.proxies.verify_proxies_filter_clear_all_button()

        #verify no.of items selected text 
        self.proxies.select_filter("Offline")
        self.proxies.verify_proxies_filter_items_selected_text_displayed()
        assert "2 items selected" == self.proxies.get_proxies_filter_items_selected_text()

        #verify clear all button functionality
        self.proxies.click_proxies_filter_clear_all_button()
        self.proxies.verify_proxies_filter_items_selected_text_displayed(displayed=False)

    def test_23_verify_settings_screen_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33597041

        self.proxies.click_proxies_settings_tab()
        self.proxies.verify_data_collection_preferences_tab()
        self.proxies.verify_proxies_settings_table_data_load()
        self.proxies.verify_proxies_settings_description()
        self.proxies.verify_proxies_settings_category_label()
        self.proxies.verify_proxies_settings_search_box()
        self.proxies.verify_proxies_settings_audit_log_button()
        self.proxies.verify_proxies_settings_audit_log_button_tooltip_message()
        self.proxies.verify_proxies_settings_toggle()
        self.proxies.click_proxies_settings_toggle_button()

    @pytest.mark.parametrize('search_string', ["invalidproxysetting", "Device UUID Key"])
    def test_24_verify_proxies_settings_search_functionality(self,search_string ):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33597042

        # Verify and wait fors proxies table data load
        self.proxies.verify_proxies_table_data_load()
        self.proxies.click_proxies_settings_tab()
        self.proxies.verify_proxies_settings_table_data_load()
        if search_string == "invalidproxysetting":
            assert False == self.proxies.proxies_settings_search(search_string)
        else:
            assert True == self.proxies.proxies_settings_search(search_string)
        self.proxies.click_search_clear_button()

    def test_25_verify_proxies_settings_table(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/34334898

        if self.proxies.verify_proxies_checkbox() == False:
            self.proxies.verify_proxy_setting_tab_status(displayed=False)
        else:
            self.proxies.click_proxies_settings_tab()
            assert True == self.proxies.verify_proxies_settings_toggle()

    def test_26_verify_settings_screen_warning_message(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/35026256

        self.proxies.click_proxies_settings_tab()
        self.proxies.verify_proxies_settings_table_data_load()
        if self.proxies.verify_proxies_settings_warning_message():
            self.proxies.verify_proxies_settings_screen_error_message()
        else:
            self.proxies.proxies_settings_search("Device UUID Key")
            self.proxies.click_proxies_settings_toggle_button()
            self.proxies.click_functionality_may_be_lost_popup_confirm_button()
            self.proxies.verify_proxies_settings_table_data_load()
            self.proxies.verify_proxies_settings_screen_error_message()
            
            # Reverting the settings
            self.proxies.click_proxies_settings_toggle_button()
            self.proxies.verify_proxies_settings_table_data_load()
            assert False == self.proxies.verify_proxies_settings_warning_message()

    def test_27_verify_proxies_settings_screen_help_popup(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/34032096

        self.proxies.click_proxies_settings_tab()
        self.proxies.verify_proxies_settings_table_data_load()
        self.proxies.click_proxies_settings_help_info_button()
        self.proxies.verify_proxies_settings_help_info_popup()
        self.proxies.click_proxies_settings_help_info_close_button()
        self.proxies.verify_proxies_settings_help_info_popup(displayed=False)

    def test_28_verify_verify_proxy_invalid_code_error_message(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/34155823

        self.proxies.verify_proxies_table_data_load()
        self.proxies.click_proxies_add_button()
        self.proxies.enter_code("123456")
        self.proxies.click_verify_proxy_popup_verify_button()
        self.proxies.verify_verify_proxy_invalid_code_error_msg()
        self.proxies.click_proxy_verified_popup_cancel_button()
        self.proxies.verify_proxy_verified_popup_title(displayed=False)

    def test_29_verify_proxies_settings_filter_side_bar_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/34776588
        
        self.proxies.click_proxies_settings_tab()
        self.proxies.verify_proxies_settings_table_data_load()
        self.proxies.click_proxies_settings_filter_button()
        self.proxies.verify_filter_side_bar_description()
        self.proxies.verify_filter_side_bar_search_box()
        self.proxies.verify_filter_side_bar_status_label()
        self.proxies.verify_filter_side_bar_data_collection_label()
        self.proxies.click_filter_side_bar_close_button()
        self.proxies.verify_filter_side_bar_title(displayed=False)

    def test_30_verify_proxies_settings_filter_clear_all_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/34776602

        self.proxies.click_proxies_settings_tab()
        self.proxies.verify_proxies_settings_table_data_load()
        self.proxies.click_proxies_settings_filter_button()

        #verify no.of items selected text 
        self.proxies.select_filter("Allow")
        self.proxies.verify_proxies_filter_items_selected_text_displayed()
        assert "1 items selected" == self.proxies.get_proxies_filter_items_selected_text()
        self.proxies.verify_proxies_filter_clear_all_button()

        #verify no.of items selected text 
        self.proxies.select_filter("Disallow")
        self.proxies.verify_proxies_filter_items_selected_text_displayed()
        assert "2 items selected" == self.proxies.get_proxies_filter_items_selected_text()

    def test_31_verify_proxies_settings_pagination(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/35655732
        
        self.proxies.click_proxies_settings_tab()
        self.proxies.verify_proxies_settings_table_data_load()

        self.proxies.verify_all_page_size_options_new([25, 50, 75, 100])
        self.proxies.verify_table_displaying_correctly_new(25, page=1)
        self.proxies.verify_table_displaying_correctly_new(50, page=1)
        self.proxies.verify_table_displaying_correctly_new(75, page=1)
        self.proxies.verify_table_displaying_correctly_new(100, page=1)

    @pytest.mark.parametrize('search_string', ["Serial Number"])
    def test_32_verify_functionality_may_be_lost_popup_ui(self,search_string):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33727447
        # https://hp-testrail.external.hp.com/index.php?/cases/view/33727628

        self.proxies.click_proxies_settings_tab()
        self.proxies.verify_proxies_settings_table_data_load()
        self.proxies.proxies_settings_search(search_string)
        self.proxies.click_proxies_settings_toggle_button()
        self.proxies.verify_functionality_may_be_lost_popup()
        self.proxies.verify_functionality_may_be_lost_popup_description()
        self.proxies.verify_functionality_may_be_lost_popup_settings_name(search_string)
        self.proxies.verify_functionality_may_be_lost_popup_cancel_button()
        self.proxies.verify_functionality_may_be_lost_popup_confirm_button()
        self.proxies.click_functionality_may_be_lost_popup_cancel_button()
        self.proxies.verify_functionality_may_be_lost_popup(displayed=False)

    def test_33_verify_proxies_settings_warning_icon(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/35655746

        self.proxies.click_proxies_settings_tab()
        self.proxies.verify_proxies_settings_table_data_load()
        self.proxies.proxies_settings_search("Serial Number")
        self.proxies.click_proxies_settings_toggle_button()
        self.proxies.click_functionality_may_be_lost_popup_confirm_button()
        self.proxies.verify_proxies_settings_table_data_load()
        self.proxies.verify_proxies_settings_warning_icon()

        # Reverting the settings
        self.proxies.click_proxies_settings_toggle_button()
        self.proxies.verify_proxies_settings_table_data_load()
        self.proxies.verify_proxies_settings_warning_icon(displayed=False)

    # Commenting the test for now, once the settings name are finalizd and stabel will get it back runnig.
    # def test_34_verify_proxy_settings_by_catagory(self):
    #     # 

    #     proxy_settings = {
    #         "Necessary Data": ["Device Uuid Key","Device Groups","Device Firmware Rom Date Code","Device Uuid",
    #                           "Serial Number","Device Control Panel Language","Device Manufacturer","Device Firmware Revision",
    #                           "Service Id","Device Firmware Identifier","Display Name","Model Number",
    #                           "Cloud Logging","Device Config","Config Component","Fleet Proxy"],
    #         "Device": ["Time Zone Daylight Saving","Ews Time Service Combo","Device Date Time Format","Date Time Services",
    #                           "Asset Number","Contact Person","Device Location","Company Name",
    #                           "Device Name","Use Requested Tray","Manual Feed","Size Type Prompt",
    #                           "Override A4 Letter","Job Retention"],
    #         "Ews": ["Ews Language Combo"],
    #         "File System": ["File System External Access","Enable Pjl Device Access","Secure File Erase Mode"],
    #         "Firmware": ["Remote Upgrade Enable","Printer Firmware Signing","Fwu"],
    #         "Network": ["Ipv4 Info","Dot1x Authentication","Dns Server","Device Np Config Source","Air Print Fax Scan",
    #                     "Certificate Upload Ca","Certificate Upload Identity","Network Enable Features Wins Registration",
    #                     "Network Enable Features Wins Port","Network Enable Features Llmnr","Network Enable Features Air Print",
    #                     "Network Enable Features Ipp","Network Enable Features Ipps","Web Services Print",
    #                     "Network Enable Features 9100","Network Enable Features Ftp","Network Enable Features Lpd",
    #                     "Network Enable Features Telnet","Network Enable Features Tftp Config File","Network Enable Features Xml Services",
    #                     "Network Enable Features Slp","Network Enable Features Ws Discovery","Network Enable Features Mdns"],
    #         "Security": ["Ldap Setup","Local Admin Password","Ews Password Is Set",
    #                      "Usb Printing","Send To Usb Settings Enabled","Usb Host Enable"],
    #     }

    #     self.proxies.click_proxies_settings_tab()
    #     self.proxies.verify_proxies_settings_table_data_load()
    #     for catagory in proxy_settings:
    #         self.proxies.click_settings_catagory(catagory)
    #         self.proxies.verify_proxies_settings_table_data_load()
    #         assert proxy_settings[catagory] == self.proxies.get_proxy_settings_names()

    # No Proxies devices available in the account so skipping the test for now.   
    @pytest.mark.skip    
    def test_35_verify_device_details_connectivity_widget(self):
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.click_first_entry_link()
        self.devices.verify_device_detail_connectivity_type_widget_title()
        device_type = self.devices.get_device_detail_connectivity_type_widget_device_type()
        if device_type != "Cloud":
            self.devices.verify_device_details_connectivity_type_widget_proxy_status()
            self.devices.cick_connectivity_type_widget_view_details_link()
            self.proxies.verify_page_title(page_title="Proxies")