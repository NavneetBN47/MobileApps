import pytest
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from time import sleep
import random

new_dashboard_name= "auto_test"+str(random.randint(1,1000))
 
class Test_13_Workforce_Home_and_Analytics_Dashboard(object):
 
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, wex_setup, request):
        self = self.__class__
        self.driver, self.fc = wex_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.printers = self.fc.fd["fleet_management_devices"]
        self.policies = self.fc.fd["fleet_management_policies"]
        self.dashboard = self.fc.fd["fleet_management_dashboard"]
        self.account = ma_misc.get_wex_account_info(self.stack)
        if "sanity" in request.config.getoption("-m"):
            self.account = ma_misc.get_wex_account_info(self.stack)
            self.hpid_username = self.account["ldk_sanity_email"]
            self.hpid_password = self.account["ldk_sanity_password"]
        else:
            self.account = ma_misc.get_wex_account_info(self.stack)
            self.hpid_username = self.account["customer_email"]
            self.hpid_password = self.account["customer_password"]
    
    @pytest.fixture(scope="function", autouse="true")
    def go_to_dashboard(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)

        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        self.home.click_sidemenu_analytics_button()
        self.home.click_analytics_fleet_management_button()
        sleep(3)
        return self.home.verify_fleet_management_breadcrumb()

    def test_01_verify_sidemenu_options(self):
        #
        # Verify the side menu options
        self.home.verify_sidemenu_home_btn()
        self.home.verify_sidemenu_analytics_button()
        self.home.verify_sidemenu_devices_button()
        self.home.verify_sidemenu_remediations_button()
        self.home.verify_sidemenu_pulses_button()
        self.home.verify_sidemenu_labs_button()
    
    def test_02_verify_sidebar_options_when_collapsed_and_its_navigation(self):
        #
        # Collapse the sidebar as it is expanded
        self.home.click_side_menu_collapse_button()

        # Verify the Devices options are not visible
        assert not self.home.verify_sidemenu_devices_button_is_expanded()
        assert not self.home.verify_sidemenu_remediations_button_is_expanded()

        self.home.click_home_menu_btn()
        self.home.verify_home_fleet_inventory_widget()

        # Verify the Devices options are visible
        self.home.click_sidemenu_devices_button()
        self.home.verify_sidemenu_devices_dropdown_list()
        
        expected_options=["PCs","Printers", "Virtual Machines", "Physical Assets"]
        assert expected_options == self.home.get_sidemenu_devices_options_list_items()

        # Verify the Remediations options are visible
        self.home.click_sidemenu_remediations_button()
        self.home.verify_sidemenu_remediations_dropdown_list()

        expected_options=["Policies", "Scripts", "Secrets", "Activity"]
        assert expected_options == self.home.get_sidemenu_remediations_options_list_items()

        # Verify the navigation to the printers page
        self.home.click_sidemenu_devices_button()
        self.home.click_sidemenu_devices_dropdown_list_printers_button()
        self.printers.verify_devices_printers_table_loaded()

        # Verify the navigation to the policies page
        self.home.click_sidemenu_remediations_button()
        self.home.click_sidemenu_remediations_dropdown_list_policies_button()
        #self.policies.click_remediations_policies_printers_tab()
        self.policies.click_remediations_printer_policies_button()
        self.policies.verify_fleet_management_policies_breadcrumb()

    @pytest.mark.sanity
    # Home - Fleet Inventory Widget
    def test_03_verify_fleet_inventory_widget_in_home_page(self):
        # 
        self.home.click_home_menu_btn()
        self.home.verify_home_fleet_inventory_widget()
        self.home.verify_fleet_inventory_widget_title()

        # Verify PC button in the fleet inventory widget
        self.home.verify_fleet_inventory_pcs_button()
        self.home.verify_fleet_inventory_pcs_icon()
        self.home.verify_fleet_inventory_pcs_title()
        self.home.verify_fleet_inventory_pcs_count()

        # Verify Printers button in the fleet inventory widget
        self.home.verify_fleet_inventory_printers_button()
        self.home.verify_fleet_inventory_printers_icon()
        self.home.verify_fleet_inventory_printers_title()
        self.home.verify_fleet_inventory_printers_count()

        # Verify Virtual Machines button in the fleet inventory widget
        if self.home.verify_fleet_inventory_virtual_machines_button() is True:
            self.home.verify_fleet_inventory_virtual_machines_icon()
            self.home.verify_fleet_inventory_virtual_machines_title()
            self.home.verify_fleet_inventory_virtual_machines_count()

        # Verify Video Endpoints button in the fleet inventory widget
        if self.home.verify_fleet_inventory_video_endpoints_button() is True:
            self.home.verify_fleet_inventory_video_endpoints_icon()
            self.home.verify_fleet_inventory_video_endpoints_title()
            self.home.verify_fleet_inventory_video_endpoints_add_on_btn()

        # Verify Telephones button in the fleet inventory widget
        if self.home.verify_fleet_inventory_telephones_button() is True:
            self.home.verify_fleet_inventory_telephones_icon()
            self.home.verify_fleet_inventory_telephones_title()
            self.home.verify_fleet_inventory_telephones_add_on_btn()

    @pytest.mark.sanity
    def test_04_verify_fleet_inventory_widget_printers_chart(self):
        # 
        self.home.click_home_menu_btn()
        self.home.verify_home_fleet_inventory_widget()
        self.home.verify_fleet_inventory_printers_button()
        self.home.click_fleet_inventory_printers_button()
        self.home.verify_fleet_inventory_card_printers_chart_chart()
        self.home.verify_fleet_inventory_card_printers_chart_count()
        self.home.verify_fleet_inventory_card_printers_chart_online_button()
        self.home.verify_fleet_inventory_card_printers_chart_offline_button()
        self.home.verify_fleet_inventory_card_printers_chart_view_list_of_printers_button()
        self.home.verify_fleet_inventory_card_printers_chart_printers_by_connectivity_label()
        printers_count = self.home.get_fleet_inventory_printers_count()
        assert printers_count == self.home.get_fleet_inventory_card_printers_chart_count()

    @pytest.mark.sanity
    def test_05_verify_fleet_inventory_widget_printers_chart_view_list_of_printers_navigation(self):
        #
        self.home.click_home_menu_btn()
        self.home.verify_home_fleet_inventory_widget()
        self.home.verify_fleet_inventory_printers_button()
        self.home.click_fleet_inventory_printers_button()
        self.home.verify_fleet_inventory_card_printers_chart_chart()
        printers_count = self.home.get_fleet_inventory_card_printers_chart_count()
        self.home.click_fleet_inventory_card_printers_chart_view_list_of_printers_button()
        self.printers.verify_devices_printers_table_loaded()
        #verifying the total count of printers in the table with the count displayed in the chart
        assert printers_count == self.printers.get_printers_table_count()

    @pytest.mark.sanity
    def test_06_verify_online_and_offline_button_status_in_printers_chart(self):
        #
        # Verify whether the online button is enabled or disabled
        self.home.click_home_menu_btn()
        self.home.verify_home_fleet_inventory_widget()
        self.home.verify_fleet_inventory_printers_button()
        self.home.click_fleet_inventory_printers_button()
        self.home.verify_fleet_inventory_card_printers_chart_online_button()

        # Verify whether the offline button is enabled or disabled
        online_button_status = self.home.verify_fleet_inventory_card_printers_chart_online_button_is_enabled()
        sleep(5)
        if online_button_status:
            self.home.click_fleet_inventory_card_printers_chart_online_button()
            assert not self.home.verify_fleet_inventory_card_printers_chart_online_button_is_enabled()
        else:
            self.home.click_fleet_inventory_card_printers_chart_online_button()
            assert self.home.verify_fleet_inventory_card_printers_chart_online_button_is_enabled()

        # Verify whether the offline button is enabled or disabled
        offline_button_status = self.home.verify_fleet_inventory_card_printers_chart_offline_button_is_enabled()
        sleep(5)
        if offline_button_status:
            self.home.click_fleet_inventory_card_printers_chart_offline_button()
            assert not self.home.verify_fleet_inventory_card_printers_chart_offline_button_is_enabled()
        else:
            self.home.click_fleet_inventory_card_printers_chart_offline_button()
            assert self.home.verify_fleet_inventory_card_printers_chart_offline_button_is_enabled()
    
    @pytest.mark.sanity
    # Fleet Management Dashboard - Printer Inventory Widget
    def test_07_verify_printer_inventory_card_in_dashboard(self):
        # https://hp-testrail.external.hp.com/index.php?/tests/view/1446545533
        self.dashboard.verify_printer_inventory_card()
        self.dashboard.verify_printer_inventory_card_title()
        self.dashboard.verify_printer_inventory_card_graph_chart()
        self.dashboard.verify_printer_inventory_card_printers_count()
        self.dashboard.verify_printer_inventory_card_printers_count_label()
        self.dashboard.verify_printer_inventory_card_online_button()
        self.dashboard.verify_printer_inventory_card_offline_button()
        self.dashboard.verify_printer_inventory_card_online_button_label()
        self.dashboard.verify_printer_inventory_card_offline_button_label()
    
    @pytest.mark.sanity
    def test_08_verify_printer_inventory_card_printer_count_in_dashboard(self):
        #
        self.dashboard.verify_printer_inventory_card()
        self.dashboard.verify_printer_inventory_card_title()
        self.dashboard.verify_printer_inventory_card_graph_chart()
        self.dashboard.verify_printer_inventory_card_printers_count()
        printer_inventory_count = self.dashboard.get_printer_inventory_card_printers_count()

        online_printer_count = self.dashboard.get_printer_inventory_card_online_button_count()
        offline_printer_count = self.dashboard.get_printer_inventory_card_offline_button_count()

        assert int(online_printer_count) + int(offline_printer_count) == int(printer_inventory_count)

    @pytest.mark.sanity
    def test_09_verify_printer_inventory_card_online_printer_chart_navigation(self):
        #
        self.dashboard.verify_printer_inventory_card()
        self.dashboard.verify_printer_inventory_card_graph_chart()
        online_printer_count = self.dashboard.get_printer_inventory_card_online_button_count()
        self.dashboard.click_printer_inventory_card_online_button()

        if online_printer_count == 0:
            self.printers.verify_no_items_found()
        else:
            self.printers.verify_printers_table_filtered_by_printer_connectivity_status("Online", online_printer_count)
            self.printers.click_first_entry_link()
            self.printers.verify_devices_printers_details_page_details_breadcrumb()
    
    @pytest.mark.sanity
    def test_10_verify_printer_inventory_card_offline_printer_chart_navigation(self):
        #
        self.dashboard.verify_printer_inventory_card()
        self.dashboard.verify_printer_inventory_card_graph_chart()
        offline_printer_count = self.dashboard.get_printer_inventory_card_offline_button_count()
        self.dashboard.click_printer_inventory_card_offline_button()

        if offline_printer_count == 0:
            self.printers.verify_no_items_found()
        else:
            self.printers.verify_printers_table_filtered_by_printer_connectivity_status("Offline", offline_printer_count)
            self.printers.click_first_entry_link()
            self.printers.verify_devices_printers_details_page_details_breadcrumb()

    # Testcase will be modified in future: MFE change yet to implement 
    # def test_11_verify_printer_inventory_widget_online_and_offline_button_status(self):
    #     #
    #     self.dashboard.verify_printer_inventory_card()

    #     # Verify whether the online button is enabled or disabled
    #     online_button_status = self.dashboard.verify_printer_inventory_card_online_button_is_enabled()
    #     if online_button_status:
    #         self.dashboard.click_printer_inventory_card_online_button()
    #         assert not self.dashboard.verify_printer_inventory_card_online_button_is_enabled()
    #     else:
    #         self.dashboard.click_printer_inventory_card_online_button()
    #         assert self.dashboard.verify_printer_inventory_card_online_button_is_enabled()

    #     # Verify whether the offline button is enabled or disabled
    #     offline_button_status = self.dashboard.verify_printer_inventory_card_offline_button_is_enabled()
    #     if offline_button_status:
    #         self.dashboard.click_printer_inventory_card_offline_button()
    #         assert not self.dashboard.verify_printer_inventory_card_offline_button_is_enabled()
    #     else:
    #         self.dashboard.click_printer_inventory_card_offline_button()
    #         assert self.dashboard.verify_printer_inventory_card_offline_button_is_enabled()

    @pytest.mark.sanity
    # Fleet Management Dashboard - Printer Fleet Security Widget
    def test_12_verify_printer_fleet_security_widget_in_dashboard(self):
        #
        # Verify Printer Fleet Security widget
        self.dashboard.verify_printer_fleet_security_widget()
        self.dashboard.verify_printer_fleet_security_widget_title()
        self.dashboard.verify_printer_fleet_security_widget_view_details_button()
        self.dashboard.verify_printer_fleet_security_widget_badge_title()
        self.dashboard.verify_printer_fleet_security_widget_badge_subtitle()
        self.dashboard.verify_printer_fleet_security_widget_badge_icon()

        #verify high risk status button in printer fleet security widget
        if self.dashboard.verify_printer_fleet_security_widget_high_risk_status_button() is True:
            # Verify the status button count 
            self.dashboard.verify_printer_fleet_security_widget_high_risk_status_button_count()
            # Verify the navigation icons 
            # self.dashboard.verify_printer_fleet_security_widget_high_risk_status_navigation_icon()

        #verify medium risk status button in printer fleet security widget
        if self.dashboard.verify_printer_fleet_security_widget_medium_risk_status_button() is True:
            # Verify the status button count 
            self.dashboard.verify_printer_fleet_security_widget_medium_risk_status_button_count()
            # Verify the navigation icons 
            # self.dashboard.verify_printer_fleet_security_widget_medium_risk_status_navigation_icon()
        
        #verify not assessed status button in printer fleet security widget
        if self.dashboard.verify_printer_fleet_security_widget_not_assessed_status_button() is True:
            # Verify the status button count 
            self.dashboard.verify_printer_fleet_security_widget_not_assessed_status_button_count()
            # Verify the navigation icons 
            # self.dashboard.verify_printer_fleet_security_widget_not_assessed_status_navigation_icon()

        #verify low risk status button in printer fleet security widget
        if self.dashboard.verify_printer_fleet_security_widget_low_risk_status_button() is True:
            # Verify the status button count 
            self.dashboard.verify_printer_fleet_security_widget_low_risk_status_button_count()
            # Verify the navigation icons 
            # self.dashboard.verify_printer_fleet_security_widget_low_risk_status_navigation_icon()
        
        #verify passed status button in printer fleet security widget
        if self.dashboard.verify_printer_fleet_security_widget_passed_status_button() is True:
            # Verify the status button count
            self.dashboard.verify_printer_fleet_security_widget_passed_status_button_count()
            # Verify the navigation icons 
            # self.dashboard.verify_printer_fleet_security_widget_passed_status_navigation_icon()
    
    @pytest.mark.sanity
    def test_13_verify_printer_fleet_security_widget_view_details_button(self):
        #
        self.dashboard.verify_printer_fleet_security_widget()
        self.dashboard.verify_printer_fleet_security_widget_view_details_button()
        self.dashboard.click_printer_fleet_security_widget_view_details_button()
        self.printers.verify_devices_printers_table_loaded()
        self.printers.click_first_entry_link()
        sleep(5)
        self.printers.verify_devices_printers_details_page_details_breadcrumb()

    @pytest.mark.sanity
    def test_14_verify_printer_fleet_security_widget_status_buttons(self):
        #
        self.dashboard.verify_printer_fleet_security_widget()

        # Capture all status buttons and their counts dynamically
        status_buttons = self.dashboard.get_printer_fleet_security_widget_status_buttons() or []
        status_counts = {}

        for status in status_buttons:
            # Capture the count for each status
            status_counts[status] = self.dashboard.get_printer_fleet_security_widget_status_button_count(status) or 0

        for status, count in status_counts.items():
            # Click on each status button and verify the table is filtered accordingly
            self.dashboard.click_printer_fleet_security_widget_status_button(status)
            self.printers.verify_devices_printers_table_loaded()

            # Verify the count of the table entries
            self.printers.verify_printers_table_filtered_by_printer_assessment_status(status, count)
            # Navigate back to the dashboard
            self.home.click_sidemenu_analytics_button()
            self.home.click_analytics_fleet_management_button()
            self.dashboard.verify_printer_fleet_security_widget()

    @pytest.mark.sanity
    def test_15_verify_printer_fleet_security_widget_information_icon(self):
        # 
        self.dashboard.verify_printer_fleet_security_widget()
        self.dashboard.verify_printer_fleet_security_widget_more_options_button()
        self.dashboard.click_printer_fleet_security_widget_more_options_button()
        self.dashboard.click_printer_fleet_security_widget_about_this_widget_button()
        
        self.dashboard.verify_hp_secure_fleet_manager_status_information_modal()
        self.dashboard.verify_hp_secure_fleet_manager_status_information_modal_title()
        self.dashboard.verify_hp_secure_fleet_manager_status_information_modal_description()
        self.dashboard.verify_hp_secure_fleet_manager_status_information_modal_status_description()
        self.dashboard.verify_hp_secure_fleet_manager_status_information_modal_high_risk_status_description()
        self.dashboard.verify_hp_secure_fleet_manager_status_information_modal_medium_risk_status_description()
        self.dashboard.verify_hp_secure_fleet_manager_status_information_modal_low_risk_status_description()
        self.dashboard.verify_hp_secure_fleet_manager_status_information_modal_compliant_status_description()

        self.dashboard.verify_hp_secure_fleet_manager_status_information_modal_close_button()
        self.dashboard.click_hp_secure_fleet_manager_status_information_modal_close_button()
        self.dashboard.verify_hp_secure_fleet_manager_status_information_modal_not_displayed()
    
    @pytest.mark.sanity
    def test_16_verify_printer_fleet_security_widget_badge_subtitle_status(self):
        #
        self.dashboard.verify_printer_fleet_security_widget()
        
        # Verify High Risk status
        if self.dashboard.verify_printer_fleet_security_widget_high_risk_status_button():
            assert "High risk" == self.dashboard.get_printer_fleet_security_widget_badge_subtitle_status()
        
        # Verify Medium Risk status
        elif self.dashboard.verify_printer_fleet_security_widget_medium_risk_status_button() or self.dashboard.verify_printer_fleet_security_widget_not_assessed_status_button():
            assert "Medium Risk" == self.dashboard.get_printer_fleet_security_widget_badge_subtitle_status()
        
        # Verify Low Risk status
        elif self.dashboard.verify_printer_fleet_security_widget_low_risk_status_button():
            assert "Low risk" == self.dashboard.get_printer_fleet_security_widget_badge_subtitle_status()
        
        # Verify Compliant status
        elif self.dashboard.verify_printer_fleet_security_widget_passed_status_button():
            assert "Compliant" == self.dashboard.get_printer_fleet_security_widget_badge_subtitle_status()
    
    @pytest.mark.sanity
    # Fleet Management Dashboard - Printer Fleet Compliance Widget
    def test_17_verify_printer_fleet_compliance_widget_in_dashboard(self):
        #
        self.dashboard.verify_printer_fleet_compliance_widget()
        self.dashboard.verify_printer_fleet_compliance_widget_title()
        self.dashboard.verify_printer_fleet_compliance_widget_view_details_button()
        self.dashboard.verify_printer_fleet_compliance_widget_graph_chart()
        self.dashboard.verify_printer_fleet_compliance_widget_graph_chart_printers_count()
        self.dashboard.verify_printer_fleet_compliance_widget_graph_chart_printers_count_label()

        self.dashboard.verify_printer_fleet_compliance_widget_compliance_status_button()
        self.dashboard.verify_printer_fleet_compliance_widget_non_compliant_status_button()
        self.dashboard.verify_printer_fleet_compliance_widget_not_assessed_status_button()
        self.dashboard.verify_printer_fleet_compliance_widget_compliance_status_button_label()
        self.dashboard.verify_printer_fleet_compliance_widget_non_compliant_status_button_label()
        self.dashboard.verify_printer_fleet_compliance_widget_not_assessed_status_button_label()

    @pytest.mark.sanity
    def test_18_verify_printer_fleet_compliance_widget_printer_count_in_dashboard(self):
        #
        self.dashboard.verify_printer_fleet_compliance_widget()
        self.dashboard.verify_printer_fleet_compliance_widget_title()
        self.dashboard.verify_printer_fleet_compliance_widget_graph_chart()
        self.dashboard.verify_printer_fleet_compliance_widget_graph_chart_printers_count()
        printer_fleet_compliance_count = self.dashboard.get_printer_fleet_compliance_widget_graph_chart_printers_count()

        compliance_printer_count = self.dashboard.get_printer_fleet_compliance_widget_compliance_status_button_count()
        non_compliance_printer_count = self.dashboard.get_printer_fleet_compliance_widget_non_compliant_status_button_count()
        not_assessed_printer_count = self.dashboard.get_printer_fleet_compliance_widget_not_assessed_status_button_count()

        assert int(compliance_printer_count) + int(non_compliance_printer_count) + int(not_assessed_printer_count) == int(printer_fleet_compliance_count)
    
    @pytest.mark.sanity
    def test_19_verify_printer_fleet_compliance_widget_compliance_printer_chart_navigation(self):
        #
        self.dashboard.verify_printer_fleet_compliance_widget()
        self.dashboard.verify_printer_fleet_compliance_widget_graph_chart()
        
        compliance_printer_count = self.dashboard.get_printer_fleet_compliance_widget_compliance_status_button_count()
        self.dashboard.click_printer_fleet_compliance_widget_compliance_status_button()
        sleep(5)

        if compliance_printer_count == 0:
            self.printers.verify_no_items_found()
        else:
            self.printers.verify_printers_table_filtered_by_printer_compliance_status("Compliant", compliance_printer_count)
            self.printers.click_first_entry_link()
            self.printers.verify_devices_printers_details_page_details_breadcrumb()
        
    @pytest.mark.sanity
    def test_20_verify_printer_fleet_compliance_widget_non_compliance_printer_chart_navigation(self):
        #
        self.dashboard.verify_printer_fleet_compliance_widget()
        self.dashboard.verify_printer_fleet_compliance_widget_graph_chart()

        non_compliance_printer_count = self.dashboard.get_printer_fleet_compliance_widget_non_compliant_status_button_count()
        self.dashboard.click_printer_fleet_compliance_widget_non_compliant_status_button()
        sleep(5)

        if non_compliance_printer_count == 0:
            self.printers.verify_no_items_found()
        else:
            self.printers.verify_printers_table_filtered_by_printer_compliance_status("Noncompliant", non_compliance_printer_count)
            self.printers.click_first_entry_link()
            self.printers.verify_devices_printers_details_page_details_breadcrumb()

    @pytest.mark.sanity
    def test_21_verify_printer_fleet_compliance_widget_not_assessed_printer_chart_navigation(self):
        #
        self.dashboard.verify_printer_fleet_compliance_widget()
        self.dashboard.verify_printer_fleet_compliance_widget_graph_chart()

        not_assessed_printer_count = self.dashboard.get_printer_fleet_compliance_widget_not_assessed_status_button_count()
        self.dashboard.click_printer_fleet_compliance_widget_not_assessed_status_button()
        sleep(5)

        if not_assessed_printer_count == 0:
            self.printers.verify_no_items_found()
        else:
            self.printers.verify_printers_table_filtered_by_printer_compliance_status("Not Assessed", not_assessed_printer_count)
            self.printers.click_first_entry_link()
            self.printers.verify_devices_printers_details_page_details_breadcrumb()

    @pytest.mark.sanity
    def test_22_verify_printer_fleet_compliance_widget_view_details_button(self):
        #
        self.dashboard.verify_printer_fleet_compliance_widget()
        sleep(5)
        self.dashboard.verify_printer_fleet_compliance_widget_view_details_button()
        self.dashboard.click_printer_fleet_compliance_widget_view_details_button()
        self.printers.verify_devices_printers_table_loaded()
        self.printers.click_first_entry_link()
        self.printers.verify_devices_printers_details_page_details_breadcrumb()
    
    # #Testcase will be removed or modified in future: Design change in UI
    # def test_23_verify_printer_fleet_compliance_widget_status_buttons(self):
    #     #
    #     self.dashboard.verify_printer_fleet_compliance_widget()

    #     self.dashboard.verify_printer_fleet_compliance_widget_compliance_status_button()

    #     # Verify whether the compliance button is enabled or disabled
    #     compliance_button_status = self.dashboard.verify_printer_fleet_compliance_widget_compliance_status_button_is_enabled()
    #     if compliance_button_status is False:
    #         self.dashboard.click_printer_fleet_compliance_widget_compliance_status_button()
    #         assert self.dashboard.verify_printer_fleet_compliance_widget_compliance_status_button_is_enabled()

    #     # Verify whether the non-compliant button is enabled or disabled
    #     non_compliant_button_status = self.dashboard.verify_printer_fleet_compliance_widget_non_compliant_status_button_is_enabled()
    #     if non_compliant_button_status:
    #         self.dashboard.verify_printer_fleet_compliance_widget_non_compliant_status_button()
    #         self.dashboard.click_printer_fleet_compliance_widget_non_compliant_status_button()
    #         assert not self.dashboard.verify_printer_fleet_compliance_widget_non_compliant_status_button_is_enabled()
    #     else:
    #         self.dashboard.click_printer_fleet_compliance_widget_non_compliant_status_button()
    #         assert self.dashboard.verify_printer_fleet_compliance_widget_non_compliant_status_button_is_enabled()

    #     # Verify whether the not assessed button is enabled or disabled
    #     not_assessed_button_status = self.dashboard.verify_printer_fleet_compliance_widget_not_assessed_status_button_is_enabled()
    #     if not_assessed_button_status:
    #         self.dashboard.click_printer_fleet_compliance_widget_not_assessed_status_button()
    #         assert not self.dashboard.verify_printer_fleet_compliance_widget_not_assessed_status_button_is_enabled()
    #     else:
    #         self.dashboard.click_printer_fleet_compliance_widget_not_assessed_status_button()
    #         assert self.dashboard.verify_printer_fleet_compliance_widget_not_assessed_status_button_is_enabled()

    def test_24_verify_more_options_in_printer_inventory_in_fleet_management_dashboard(self):
        #
        self.dashboard.verify_printer_inventory_card()
        self.dashboard.verify_printer_inventory_card_more_options_button()
        self.dashboard.click_printer_inventory_card_more_options_button()
        expected_options=["Export as PNG", "Copy as PNG", "Remove widget"]
        assert expected_options == self.dashboard.get_printer_inventory_card_more_options_list_items()
        
    def test_25_verify_more_options_in_printer_fleet_security_widget_in_fleet_management_dashboard(self):
        #
        self.dashboard.verify_printer_fleet_security_widget()
        self.dashboard.verify_printer_fleet_security_widget_more_options_button()
        self.dashboard.click_printer_fleet_security_widget_more_options_button()
        expected_options=["About this widget", "Export as PNG", "Copy as PNG", "Remove widget"]
        assert expected_options == self.dashboard.get_printer_fleet_security_widget_more_options_list_items()
    
    def test_26_verify_more_options_in_printer_fleet_compliance_widget_in_fleet_management_dashboard(self):
        #
        self.dashboard.verify_printer_fleet_compliance_widget()
        self.dashboard.verify_printer_fleet_compliance_widget_more_options_button()
        self.dashboard.click_printer_fleet_compliance_widget_more_options_button()
        expected_options=["Export as PNG", "Copy as PNG", "Remove widget"]
        assert expected_options == self.dashboard.get_printer_fleet_compliance_widget_more_options_list_items()