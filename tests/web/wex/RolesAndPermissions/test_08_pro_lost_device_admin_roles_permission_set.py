import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.web.wex.wex_utility import SoftAssert
from time import sleep

pytest.app_info = "WEX"
soft_assertion = SoftAssert()

class Test_08_Workforce_Pro_Lost_Device_Admin_Permisson_Set(object):

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
        self.groups = self.fc.fd["pcs_groups"]
        self.policies_pcs = self.fc.fd["remediations_policies_pcs"]
        self.secrets = self.fc.fd["remediations_secrets"]
        self.activity = self.fc.fd["remediations_activity"]
        self.help_and_support = self.fc.fd["help_and_support"]
        self.user_profile = self.fc.fd["user_profile"]
        self.settings = self.fc.fd["workforce_settings"]
        self.pulses = self.fc.fd["employee_pulses"]
        self.accounts = self.fc.fd["accounts_overview"]
        self.alerts = self.fc.fd["upgrades_alerts"]
        self.scripts = self.fc.fd["upgrades_scripts"]
        self.labs = self.fc.fd["upgrades_labs"]
        self.integrations = self.fc.fd["upgrades_integrations"]
        self.account = ma_misc.get_wex_account_info(self.stack)
        self.hpid_username = self.account["pro_lost_device_admin_email"]
        self.hpid_password = self.account["pro_lost_device_admin_password"]

    def test_01_verify_pro_lost_device_admin_permission_set_for_home_page(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
            
        # Perform soft assertions on home side menu button
        soft_assertion.assert_false(self.home.verify_sidemenu_home_btn(), "Side menu Home button")
       
        # Perform soft assertions for Experience Score Widget
        soft_assertion.assert_false(self.home.verify_experience_score_widget(), "Home- Experience Score Widget")
        soft_assertion.assert_false(self.home.verify_experience_score_widget_overall_score(), "Experience Score Widget - Overall Score progress")
        soft_assertion.assert_false(self.home.verify_experience_score_widget_system_health(), "Experience Score Widget - System Health progress")
        soft_assertion.assert_false(self.home.verify_experience_score_widget_os_performance(), "Experience Score Widget - OS Performance progress")
        soft_assertion.assert_false(self.home.verify_experience_score_widget_security(), "Experience Score Widget - Security progress")
        soft_assertion.assert_false(self.home.verify_experience_score_widget_sentiment(), "Experience Score Widget - Sentiment progress")
        soft_assertion.assert_false(self.home.verify_experience_score_widget_network_health(), "Experience Score Widget - Network Health progress")
        soft_assertion.assert_false(self.home.verify_experience_score_widget_applications(), "Experience Score Widget - Applications progress")
        soft_assertion.assert_false(self.home.verify_experience_score_widget_collaboration(), "Experience Score Widget - Collaboration progress")

        # Perform soft assertions for Drill-Down permissions
        soft_assertion.assert_false(self.home.verify_experience_score_widget_drill_down_overall_score(), "Drill-Down Overall Score value")
        soft_assertion.assert_false(self.home.verify_experience_score_widget_drill_down_system_health(), "Drill-Down System Health value")
        soft_assertion.assert_false(self.home.verify_experience_score_widget_drill_down_os_performance(), "Drill-Down OS Performance value")
        soft_assertion.assert_false(self.home.verify_experience_score_widget_drill_down_security(), "Drill-Down Security value")
       
        soft_assertion.assert_false(self.home.verify_experience_score_widget_drill_down_sentiment(), "Drill-Down Sentiment value")        
        soft_assertion.assert_false(self.home.verify_experience_score_widget_drill_down_network_health(), "Drill-Down Network Health value")
        soft_assertion.assert_false(self.home.verify_experience_score_widget_drill_down_applications(), "Drill-Down Applications")
        soft_assertion.assert_false(self.home.verify_experience_score_widget_drill_down_collaboration(), "Drill-Down Collaboration")

        # Perform soft assertion for "View Experience OverTime" widget
        soft_assertion.assert_false(self.home.verify_experience_overtime_widget(), "Experience OverTime Widget")
        soft_assertion.assert_false(self.home.verify_experience_overtime_widget_days_filter(), "Experience OverTime Widget - Days filter")

        # Perform soft assertions for Fleet Inventory Widget permissions
        soft_assertion.assert_false(self.home.verify_home_fleet_inventory_widget_is_displayed(), "Fleet Inventory widget")
        soft_assertion.assert_false(self.home.verify_fleet_inventory_pcs_button(), "Fleet Inventory - PC's button")
        soft_assertion.assert_false(self.home.verify_fleet_inventory_virtual_machines_button(), "Fleet Inventory - Virtual Machines button")
        soft_assertion.assert_false(self.home.verify_fleet_inventory_printers_button(),"Fleet Inventory - Printers button")
        soft_assertion.assert_false(self.home.verify_fleet_inventory_video_endpoints_button(), "Fleet Inventory - Video Endpoints")
        soft_assertion.assert_false(self.home.verify_fleet_inventory_telephones_button(),"Fleet Inventory - Telephones value")

        # Perform soft assertions for "Apps with Most Crashes" widget
        soft_assertion.assert_false(self.home.verify_apps_with_most_crashes_widget(), "Apps with Most Crashes widget")

        #Perform soft assertions for Alerts
        soft_assertion.assert_false(self.home.verify_home_view_alerts_widget(), "Home - View Alerts widget")
        soft_assertion.assert_false(self.home.verify_home_view_full_list_of_alerts_widget(), "Home - View Full List of Alerts widget")
 
        # Generate report for soft assertions
        soft_assertion.generate_report("Test Results - Home Page", "Pro Lost Device Admin")
 
        # Export report to txt file
        # soft_assertion.export_report_to_txt(filename="report_home_page.txt", title="Soft Assert Report", message="Pro Lost Device Admin")
 
        # Raise exception if any soft assertions failed
        soft_assertion.raise_assertion_errors("Pro Lost Device Admin")

    def test_02_verify_pro_lost_device_admin_permission_set_for_devices_menu(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_button()
        soft_assertion.clear()
 
        # Perform soft assertions on devices side menu button
        soft_assertion.assert_true(self.home.verify_sidemenu_devices_view_pcs_button(),"Side menu Devices - View PCs button")
        soft_assertion.assert_true(self.home.verify_sidemenu_devices_view_virtual_machines_button(),"Side menu Devices - View Virtual Machines button")
        soft_assertion.assert_true(self.home.verify_sidemenu_devices_view_physical_assets_button(),"Side menu Devices - View Physical Assets button")
        soft_assertion.assert_false(self.home.verify_sidemenu_devices_view_printers_button(),"Side menu Devices - View Printers button")
 
        # Perform soft assertions on Devices- View PCs page
        # Navigate to Devices - View PCs page
        self.home.click_sidemenu_devices_view_pcs_button()
        soft_assertion.assert_equal(self.printers.get_devices_view_pcs_page(), "PCs", "Devices - View PCs page")
        self.printers.click_status_clear_button()
        sleep(5) # wait for table to load
 
        # Perform soft assertions for Add, Delete PCs permission
        self.printers.click_first_checkbox()
        soft_assertion.assert_false(self.printers.verify_add_pcs_button(),"Add PCs button")
        soft_assertion.assert_false(self.printers.verify_delete_pcs_button(),"Delete PCs button")
 
        # Perform soft assertions for Export PCs permission
        soft_assertion.assert_true(self.printers.verify_export_pcs_button(),"Export PCs button")
 
        # Perform soft assertions on Devices- View Virtual Machines page
        # Navigate to Devices - View Virtual Machines page
        self.home.click_sidemenu_devices_view_virtual_machines_button()
        soft_assertion.assert_equal(self.printers.get_devices_view_virtual_machines_page(),"Virtual Machines", "Devices - View Virtual Machines page")
 
        # Perform soft assertions for Add, Delete Virtual Machines permission
        # self.printers.click_first_checkbox()
        soft_assertion.assert_false(self.printers.verify_add_virtual_machines_button(),"Add Virtual Machines button")
        soft_assertion.assert_false(self.printers.verify_delete_virtual_machines_button(),"Delete Virtual Machines button")
 
        # Perform soft assertions for Export Virtual Machines permission
        # soft_assertion.assert_true(self.printers.verify_export_virtual_machines_button(),"Export Virtual Machines button")
 
        # Perform soft assertions on Devices- View Physical Assets page
        # Navigate to Devices - View Physical Assets page
        self.home.click_sidemenu_devices_view_physical_assets_button()
        soft_assertion.assert_equal(self.printers.get_devices_view_physical_assets_page(), "Physical Assets", "Devices - View Physical Assets page")
 
        # Perform soft assertions for Add, Delete Physical Assets permission
        # self.printers.click_first_checkbox()
        soft_assertion.assert_false(self.printers.verify_add_physical_assets_button(),"Add Physical Assets button")
        soft_assertion.assert_false(self.printers.verify_delete_physical_assets_button(),"Delete Physical Assets button")
 
        # Perform soft assertions for Export Physical Assets permission
        # soft_assertion.assert_true(self.printers.verify_export_physical_assets_button(),"Export Physical Assets button")
 
        #Generate report for soft assertions
        soft_assertion.generate_report("Test Results- Devices Page", "Pro Lost Device Admin")
 
        # Export report to txt file
        # soft_assertion.export_report_to_txt(filename="report_devices_page.txt", title="Soft Assert Report", message="Pro Lost Device Admin")
 
        # Raise exception if any soft assertions failed
        soft_assertion.raise_assertion_errors("Pro Lost Device Admin")

    def test_03_verify_pro_lost_device_admin_permission_set_for_groups(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        
        # Navigate to Groups page
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        soft_assertion.clear()

        # Perform soft assertions for Groups permissions
        soft_assertion.assert_false(self.home.verify_sidemenu_groups_button(), "Side menu Groups button")
        soft_assertion.assert_false(self.groups.verify_pcs_groups_add_button(), "Groups - Add button")
        soft_assertion.assert_false(self.groups.verify_pcs_groups_delete_button(), "Groups - Delete button")
        soft_assertion.assert_false(self.groups.verify_pcs_groups_export_button(), "Groups - Export button")
        soft_assertion.assert_false(self.groups.verify_pcs_groups_edit_button(), "Groups - Edit button")

        # Generate report for soft assertions
        soft_assertion.generate_report("Test Results - Groups Page", "Pro Lost Device Admin")

        # Export report to txt file
        # soft_assertion.export_report_to_txt(filename="report_groups_page.txt", title="Soft Assert Report", message="Pro Lost Device Admin")

        # Raise exception if any soft assertions failed
        soft_assertion.raise_assertion_errors("Pro Lost Device Admin")
    
    def test_04_verify_pro_lost_device_admin_permission_set_for_remediations(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()

        # Navigate to Remediations page
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        soft_assertion.clear()

        # Perform soft assertions on Remediations side menu button
        soft_assertion.assert_false(self.home.verify_sidemenu_remediations_button(), "Side menu Remediations button")
        soft_assertion.assert_false(self.home.verify_sidemenu_remediations_policies_button(), "Side menu Remediations - View Policies button")
        soft_assertion.assert_false(self.home.verify_sidemenu_remediations_secrets_button(), "Side menu Remediations - View Secrets button")
        soft_assertion.assert_false(self.home.verify_sidemenu_remediations_activity_button(), "Side menu Remediations - View activity button")
    
        # Perform soft assertions for Remediations - View Policies PC's page
        soft_assertion.assert_false(self.policies_pcs.verify_remediations_policies_pcs_page(), "Policies PC's page")
        soft_assertion.assert_false(self.policies_pcs.verify_remediations_policies_pcs_tab(), "Policies PC's tab")
        soft_assertion.assert_false(self.policies_pcs.verify_remediations_policies_pcs_add_button(), "Policies PC's page- Add button")
        soft_assertion.assert_false(self.policies_pcs.verify_pcs_policies_edit_button(), "Policies PC's page - Edit button")
        soft_assertion.assert_false(self.policies_pcs.verify_pcs_policies_delete_button(), "Policies PC's page - Delete button")

        # Perform soft assertions for Remediations - View Secrets page
        soft_assertion.assert_false(self.secrets.verify_remediations_secrets_page(), "Remediations - View Secrets page")
        soft_assertion.assert_false(self.secrets.verify_remediations_secrets_add_button(), "Remediations - Add Secrets button")
        soft_assertion.assert_false(self.secrets.verify_secrets_page_edit_button(), "Remediations - View Secrets page - Edit button")
        soft_assertion.assert_false(self.secrets.verify_secrets_page_delete_button(), "Remediations - View Secrets page - Delete button")

        # Perform soft assertions for Remediations - View activity page
        soft_assertion.assert_false(self.activity.verify_remediations_activity_page(), "Remediations - View activity page")
        soft_assertion.assert_false(self.activity.verify_remediations_activity_add_button(), "Remediations - Add activity button")
        soft_assertion.assert_false(self.activity.verify_activity_page_edit_button(), "Remediations - View activity page - Edit button")
        soft_assertion.assert_false(self.activity.verify_activity_page_delete_button(), "Remediations - View activity page - Delete button")

        # Perform soft assertions for Remediations - View Scripts page
        soft_assertion.assert_false(self.scripts.verify_remediations_scripts_page(), "Remediations - View Scripts page")
        soft_assertion.assert_false(self.scripts.verify_remediations_scripts_page_library_tab(), "Remediations - View Scripts page - Library tab")
        soft_assertion.assert_false(self.scripts.verify_remediations_scripts_page_assignments_tab(), "Remediations - View Scripts page - Assignments tab")
        soft_assertion.assert_false(self.scripts.verify_remediations_scripts_page_gallery_tab(), "Remediations - View Scripts page - Gallery tab")

        soft_assertion.assert_false(self.scripts.verify_remediations_scripts_add_button(), "Remediations - Add Scripts button")
        soft_assertion.assert_false(self.scripts.verify_scripts_page_delete_button(), "Remediations - View Scripts page - Delete button")

        # Generate report for soft assertions
        soft_assertion.generate_report("Test Results - Remediations Page", "Pro Lost Device Admin")

        # Export report to txt file
        # soft_assertion.export_report_to_txt(filename="report_remediations_page.txt", title="Soft Assert Report", message="Pro Lost Device Admin")

        # Raise exception if any soft assertions failed
        soft_assertion.raise_assertion_errors("Pro Lost Device Admin")

    def test_05_verify_pro_lost_device_admin_permission_user_profile_overview_and_communication_preferences_page(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        soft_assertion.clear()

        # Verify User Profile button
        soft_assertion.assert_true(self.user_profile.verify_user_profile_button(), "User Profile button")
        self.user_profile.click_user_profile_button()
        self.user_profile.click_user_profile_link()
        soft_assertion.assert_true(self.user_profile.verify_user_profile_page_breadcrumb(), "Navigation - User Profile page")
       
        # Perform soft assertions for User Profile Overview page
        soft_assertion.assert_true(self.user_profile.verify_user_profile_overview_tab(), "User Profile Overview tab")
        soft_assertion.assert_true(self.user_profile.verify_user_profile_overview_tab_name_label(), "User Profile Overview tab - Name label")
        soft_assertion.assert_true(self.user_profile.verify_user_profile_overview_tab_mobile_phone_number_label(), "User Profile Overview tab - Mobile Phone Number label")
        soft_assertion.assert_true(self.user_profile.verify_user_profile_overview_tab_office_phone_number_label(), "User Profile Overview tab - Office Phone Number label")
        soft_assertion.assert_true(self.user_profile.verify_user_profile_overview_tab_preferred_language_label(), "User Profile Overview tab - Preferred Language label")
        soft_assertion.assert_true(self.user_profile.verify_user_profile_overview_time_zone_label(), "User Profile Overview tab - Time Zone label")
        soft_assertion.assert_true(self.user_profile.verify_user_profile_overview_tab_title_label(), "User Profile Overview tab - Title label")

        soft_assertion.assert_true(self.user_profile.verify_user_profile_overview_tab_name_edit_button(), "User Profile Overview tab - Name Edit button")
        soft_assertion.assert_true(self.user_profile.verify_user_profile_overview_tab_mobile_phone_number_edit_button(), "User Profile Overview tab - Mobile Phone Number Edit button")
        soft_assertion.assert_true(self.user_profile.verify_user_profile_overview_tab_office_phone_number_edit_button(), "User Profile Overview tab - Office Phone Number Edit button")
        soft_assertion.assert_true(self.user_profile.verify_user_profile_overview_tab_preferred_language_edit_button(), "User Profile Overview tab - Preferred Language Edit button")
        soft_assertion.assert_true(self.user_profile.verify_user_profile_overview_tab_time_zone_edit_button(), "User Profile Overview tab - Time Zone Edit button")
        soft_assertion.assert_true(self.user_profile.verify_user_profile_overview_tab_title_edit_button(), "User Profile Overview tab - Title Edit button")

        # Perform soft assertions for User Profile Communication Preferences page
        # Verify Whats New popup alerts toggle button
        soft_assertion.assert_true(self.user_profile.verify_user_profile_communication_preference_tab(), "User Profile Communication Preferences tab")
        self.user_profile.click_user_profile_page_communication_preference_tab()
        soft_assertion.assert_equal(self.user_profile.get_user_profile_communication_tab_whats_new_popup_title(), "What's new popup alerts", "User Profile Communication Preferences tab - What's new popup alerts")
        soft_assertion.assert_true(self.user_profile.verify_user_profile_communication_tab_whats_new_popup_toggle_button(), "User Profile Communication Preferences tab - What's new popup toggle button")
        self.user_profile.user_profile_communication_tab_whats_new_popup_toggle_button_status()

        # Verify Alert notifications toggle button
        soft_assertion.assert_equal(self.user_profile.get_user_profile_communication_tab_alert_notifications_title(), "Alert notifications", "User Profile Communication Preferences tab - Alert notifications")
        soft_assertion.assert_true(self.user_profile.verify_user_profile_communication_tab_alert_notifications_toggle_button(), "User Profile Communication Preferences tab - Alert notifications toggle button")
        self.user_profile.user_profile_communication_tab_alert_notifications_toggle_button_status()

        # Verify General system notifications toggle button
        soft_assertion.assert_equal(self.user_profile.get_user_profile_communication_tab_general_system_notifications_title(), "General system notifications", "User Profile Communication Preferences tab - General system notifications")
        soft_assertion.assert_true(self.user_profile.verify_user_profile_communication_tab_general_system_notifications_toggle_button(), "User Profile Communication Preferences tab - General system notifications toggle button")
        self.user_profile.user_profile_communication_tab_general_system_notifications_toggle_button_status()
                                    
        # Generate report for soft assertions
        soft_assertion.generate_report("Test Results - User Profile", "Pro Lost Device Admin")

        # Export report to txt file
        # soft_assertion.export_report_to_txt(filename="report_user_profile.txt", title="Soft Assert Report", message="Pro Lost Device Admin")
 
        # Raise exception if any soft assertions failed
        soft_assertion.raise_assertion_errors("Pro Lost Device Admin")
    
    def test_06_verify_pro_lost_device_admin_permission_set_for_help_and_support_page(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        soft_assertion.clear()

        # Verify Help and Support button
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_button(), "Help and Support button")

        #Navigate to Help and Support Page and Perform soft assertions for Help and Support page
        self.help_and_support.click_help_and_support_button()
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page(), "Help and Support page")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_header(), "Help & Support page - Header")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_header_description(), "Help & Support page - Header Description")

        # Perform soft assertion for "Get Started" widget
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_get_started_widget(), "Get Started Widget")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_get_started_widget_title(), "Get Started Widget - Title")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_get_started_widget_description(), "Get Started Widget - Description")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_get_started_widget_navigation_button(), "Get Started Widget - Navigation Button")
   
        # Perform soft assertion for "System requirements" widget
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_system_requirements_widget(), "System Requirements Widget")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_system_requirements_widget_title(), "System Requirements Widget - Title")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_system_requirements_widget_description(), "System Requirements Widget - Description")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_system_requirements_widget_navigation_button(), "System Requirements Widget - Navigation Button")

        # Perform soft assertion for "Knowledge base" widget
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_knowledge_base_widget(), "Knowledge Base Widget")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_knowledge_base_widget_title(),"Knowledge Base Widget - Title")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_knowledge_base_widget_description(), "Knowledge Base Widget - Description")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_knowledge_base_widget_navigation_button(), "Knowledge Base Widget - Navigation Button")
       
        # Perform soft assertion for "Software download" widget
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_software_download_widget(), "Software Download Widget")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_software_download_widget_title(), "Software Download Widget - Title")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_software_download_widget_description(), "Software Download Widget - Description")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_software_download_widget_navigation_button(), "Software Download Widget - Navigation Button")

        # Perform soft assertion for "What's new" widget
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_whats_new_widget(), "What's New Widget")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_whats_new_widget_title(), "What's New Widget - Title")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_whats_new_widget_description(), "What's New Widget - Description")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_whats_new_widget_navigation_button(), "What's New Widget - Navigation Button")

        # # Perform soft assertion for "Send Feedback" widget
        # soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_send_feedback_widget(), "Send Feedback Widget")
        # soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_send_feedback_widget_title(), "Send Feedback Widget - Title")
        # soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_send_feedback_widget_description(), "Send Feedback Widget - Description")
        # soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_send_feedback_widget_navigation_button(), "Send Feedback Widget - Navigation Button")

        # Perform soft assertion for "My Support Cases" widget
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_my_support_cases_widget(), "My Support Cases Widget")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_my_support_cases_widget_title(), "My Support Cases Widget - Title")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_my_support_cases_widget_description(), "My Support Cases Widget - Description")
        soft_assertion.assert_true(self.help_and_support.verify_help_and_support_page_my_support_cases_widget_navigation_button(), "My Support Cases Widget - Navigation Button")

        # Generate report for soft assertions
        soft_assertion.generate_report("Test Results - Help and Support Page", "Pro Lost Device Admin")

        # Export report to txt file
        # soft_assertion.export_report_to_txt(filename="report_help_and_support_page.txt", title="Soft Assert Report", message="Pro Lost Device Admin")
 
        # Raise exception if any soft assertions failed
        soft_assertion.raise_assertion_errors("Pro Lost Device Admin")
    
    def test_07_verify_pro_lost_device_admin_permission_set_for_settings_page(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        soft_assertion.clear()

        # Navigate to Settings page
        soft_assertion.assert_false(self.home.verify_sidemenu_settings_button(), "Side menu Settings button")

        # Perform soft assertions for Settings - Locations tab
        soft_assertion.assert_false(self.settings.verify_settings_locations_tab(), "Settings - Locations tab")
        
        # Perform soft assertions for Settings - Preferences tab
        soft_assertion.assert_false(self.settings.verify_settings_preferences_tab(), "Settings - Preferences tab")
      
        # Perform soft assertions for Settings - Roles and Permissions tab
        soft_assertion.assert_false(self.settings.verify_settings_roles_and_permissions_tab(), "Settings - Roles and Permissions tab")

        # Perform soft assertions for Settings - End User Notifications tab
        soft_assertion.assert_false(self.settings.verify_settings_end_user_notifications_tab(), "Settings - End User Notifications tab")
     
        # Perform soft assertions for Settings - Logs tab
        soft_assertion.assert_false(self.settings.verify_settings_logs_tab(), "Settings - Logs tab")
        
        # Generate report for soft assertions
        soft_assertion.generate_report("Test Results - Settings Tabs", "Pro Lost Device Admin")
        
        # Export report to txt file
        # soft_assertion.export_report_to_txt(filename="report_settings_tabs.txt", title="Soft Assert Report", message="Pro Lost Device Admin")
        
        # Raise exception if any soft assertions failed
        soft_assertion.raise_assertion_errors("Pro Lost Device Admin")

    def test_08_verify_pro_lost_device_admin_permission_set_for_analytics_dashboards_page(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        soft_assertion.clear()
        
        soft_assertion.assert_false(self.home.verify_sidemenu_analytics_button(), "Side menu Analytics button")
        soft_assertion.assert_false(self.dashboard.verify_analytics_dashboards_new_dashboard_button(), "Dashboards page - New Dashboard button")
        soft_assertion.assert_false(self.dashboard.verify_analytics_dashboards_experience_score_dashboard_button(), "Dashboards page - Experience Score Dashboard button")
        soft_assertion.assert_false(self.dashboard.verify_analytics_dashboards_fleet_management_dashboard_button(), "Dashboards page - Fleet Management Dashboard button")
        soft_assertion.assert_false(self.dashboard.verify_analytics_dashboards_employee_engagement_dashboard_button(), "Dashboards page - Employee Engagement Dashboard button")

        # Generate report for soft assertions
        soft_assertion.generate_report("Test Results - Analytics Dashboards Page", "Pro Lost Device Admin")

        # Export report to txt file
        # soft_assertion.export_report_to_txt(filename="report_analytics_dashboards_page.txt", title="Soft Assert Report", message="Pro Lost Device Admin")

        # Raise exception if any soft assertions failed
        soft_assertion.raise_assertion_errors("Pro Lost Device Admin")

    def test_09_verify_pro_lost_device_admin_permission_set_for_modern_reports(self): 
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        soft_assertion.clear()

        soft_assertion.assert_false(self.home.verify_sidemenu_analytics_button(), "Side menu Analytics button")

        #Verify Modern Reports from Analytics - Dashboards page
        soft_assertion.assert_false(self.dashboard.verify_modern_reports_tab(), "Analytics - Modern Reports tab")
        
        soft_assertion.assert_false(self.dashboard.verify_windows_11_readiness_assessment_report(), "Windows 11 Readiness Assessment report")
        soft_assertion.assert_false(self.dashboard.verify_application_experience_installed_app_report(), "Application Experience - Installed App report")
        soft_assertion.assert_false(self.dashboard.verify_application_experience_web_app_report(), "Application Experience - Web App report")
        soft_assertion.assert_false(self.dashboard.verify_network_health_report(), "Network Health report")
        soft_assertion.assert_false(self.dashboard.verify_device_utilization_report(), "Device Utilization report")
        soft_assertion.assert_false(self.dashboard.verify_sustainability_report(), "Sustainability report")
        soft_assertion.assert_false(self.dashboard.verify_bios_inventory_report(), "BIOS Inventory report")
        soft_assertion.assert_false(self.dashboard.verify_driver_inventory_report(), "Driver Inventory report")
        soft_assertion.assert_false(self.dashboard.verify_hardware_inventory_report(), "Hardware Inventory report")
        soft_assertion.assert_false(self.dashboard.verify_application_inventory_report(), "Application Inventory report")
        soft_assertion.assert_false(self.dashboard.verify_security_report(), "Security report")
        soft_assertion.assert_false(self.dashboard.verify_system_health_report(), "System Health report")
        soft_assertion.assert_false(self.dashboard.verify_os_performance_report(), "OS Performance report")
        soft_assertion.assert_false(self.dashboard.verify_blue_screen_errors_report(), "Blue Screen Errors report")
        soft_assertion.assert_false(self.dashboard.verify_application_experience_report(), "Application Experience report")
    
        #Generate report for soft assertions
        soft_assertion.generate_report("Test Results - Modern Reports", "Pro Lost Device Admin")

        # Export report to txt file
        # soft_assertion.export_report_to_txt(filename="report_modern_reports.txt", title="Soft Assert Report", message="Pro Lost Device Admin")

        # Raise exception if any soft assertions failed
        soft_assertion.raise_assertion_errors("Pro Lost Device Admin")

    def test_10_verify_pro_lost_device_admin_permission_set_for_classic_reports(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        soft_assertion.clear()

        soft_assertion.assert_false(self.home.verify_sidemenu_analytics_button(), "Side menu Analytics button")

        #Verify Classic Reports from Analytics - Dashboards page
        soft_assertion.assert_false(self.dashboard.verify_classic_reports_tab(), "Analytics - Classic Reports tab")

        # Verify Add and Export reports functionality in Classic Reports
        soft_assertion.assert_false(self.dashboard.verify_classic_reports_add_report_button(), "Classic Reports - Add Report button")
        soft_assertion.assert_false(self.dashboard.verify_classic_reports_export_report_button(), "Classic Reports - Export Report button")
   
        # Verify Browse, Favorites and History tab visibility in Classic Reports
        soft_assertion.assert_false(self.dashboard.verify_classic_reports_browse_tab(), "Classic Reports - Browse tab visible")
        soft_assertion.assert_false(self.dashboard.verify_classic_reports_favorites_tab(), "Classic Reports - Favorites tab visible")
        soft_assertion.assert_false(self.dashboard.verify_classic_reports_history_tab(), "Classic Reports - History tab visible")

        # Generate report for soft assertions
        soft_assertion.generate_report("Test Results - Classic Reports", "Pro Lost Device Admin")

        # Export report to txt file
        # soft_assertion.export_report_to_txt(filename="report_classic_reports.txt", title="Soft Assert Report", message="Pro Lost Device Admin")

        # Raise exception if any soft assertions failed
        soft_assertion.raise_assertion_errors("Pro Lost Device Admin")

    def test_11_verify_pro_lost_device_admin_permission_set_for_account_page(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        soft_assertion.clear()

       # Verify Account Side Menu button
        soft_assertion.assert_false(self.home.verify_sidemenu_accounts_button(), "Side menu Account button")
        soft_assertion.assert_false(self.accounts.verify_accounts_page(), "Account page")
        soft_assertion.assert_false(self.accounts.verify_accounts_page_overview_tab(), "Account page - Overview tab")
        soft_assertion.assert_false(self.accounts.verify_accounts_page_users_tab(), "Account page - Users tab")
        soft_assertion.assert_false(self.accounts.verify_accounts_tab_add_ons_tab(), "Account page - Add-Ons tab")
        soft_assertion.assert_false(self.accounts.verify_accounts_page_licenses_tab(), "Account page - Licenses tab")
        soft_assertion.assert_false(self.accounts.verify_accounts_page_assigned_partners_tab(), "Account page - Assigned Partners tab")

        # Perform soft assertions for Account - Overview tab
        soft_assertion.assert_false(self.accounts.verify_accounts_page_overview_tab_company_size_edit_button(), "Account - Overview tab - Company Size Edit button")
        soft_assertion.assert_false(self.accounts.verify_accounts_page_overview_tab_company_name_edit_button(), "Account - Overview tab - Company Name Edit button")
        soft_assertion.assert_false(self.accounts.verify_accounts_page_overview_tab_primary_administrator_edit_button(), "Account - Overview tab - Primary Administrator Edit button")
        soft_assertion.assert_false(self.accounts.verify_accounts_page_overview_tab_company_address_edit_button(), "Account - Overview tab - Company Address Edit button")

        # Perform soft assertions for Account - Users tab
        soft_assertion.assert_false(self.accounts.verify_accounts_page_users_tab_invite_users_button(), "Account - Users tab - Invite Users button")
        soft_assertion.assert_false(self.accounts.verify_accounts_page_users_tab_delete_button(), "Account - Users tab - Delete button")
        soft_assertion.assert_false(self.accounts.verify_accounts_page_users_tab_assign_roles_button(), "Account - Users tab - Assign Roles button")

        # Perform soft assertions for Account - Licenses tab
        soft_assertion.assert_false(self.accounts.verify_accounts_page_licenses_tab_add_licenses_button(), "Account - Licenses tab - Add Licenses button")
  
        # Perform soft assertions for Account - Add-Ons tab
        soft_assertion.assert_false(self.accounts.verify_accounts_page_add_ons_tab_hp_anyware_widget_title(),"Account - Add-Ons tab - HP Anyware widget title")
        soft_assertion.assert_false(self.accounts.verify_accounts_page_add_ons_tab_hp_anyware_widget_learn_more_link(), "Account - Add-Ons tab - HP Anyware widget - Learn More button")
        soft_assertion.assert_false(self.accounts.verify_accounts_page_add_ons_tab_vyopta_widget_title(), "Account - Add-Ons tab -Collaboration Experience by Vyopta title")
        soft_assertion.assert_false(self.accounts.verify_accounts_page_add_ons_tab_vyopta_widget_connect_button(), "Account - Add-Ons tab -Collaboration Experience by Vyopta - Connect button")
        soft_assertion.assert_false(self.accounts.verify_accounts_page_add_ons_tab_vyopta_widget_learn_more_link(), "Account - Add-Ons tab -Collaboration Experience by Vyopta - Learn More button")
        soft_assertion.assert_false(self.accounts.verify_accounts_page_add_ons_tab_hp_wolf_widget_title(), "Account - Add-Ons tab - HP Wolf Protect and Trace with Wolf Connect title")
        soft_assertion.assert_false(self.accounts.verify_accounts_page_add_ons_tab_hp_wolf_widget_learn_more_link(), "Account - Add-Ons tab - HP Wolf Protect and Trace with Wolf Connect - Learn More button")

        # Generate report for soft assertions
        soft_assertion.generate_report("Test Results - Accounts", "Pro Lost Device Admin")

        # Export report to txt file
        # soft_assertion.export_report_to_txt(filename="report_help_and_support_page.txt", title="Soft Assert Report", message="Pro Lost Device Admin")
 
        # Raise exception if any soft assertions failed
        soft_assertion.raise_assertion_errors("Pro Lost Device Admin")

    def test_12_verify_pro_lost_device_admin_permission_set_for_pulses_page(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        soft_assertion.clear()

        # Verify Pulses Side Menu button
        soft_assertion.assert_false(self.home.verify_sidemenu_pulses_button(), "Side menu Pulses button")
        soft_assertion.assert_false(self.pulses.verify_pulses_page_create_pulse_button(), "Pulses page - Create Pulse button")
        soft_assertion.assert_false(self.pulses.verify_pulses_page_create_custom_pulse_button(), "Pulses page - Custom Pulse button")
        soft_assertion.assert_false(self.pulses.verify_pulses_page_create_sentiment_pulse_button(), "Pulses page - Sentiment Pulse button")

        #Create, Edit, Duplicate and Delete Custom Pulse 
        soft_assertion.assert_false(self.pulses.verify_pulses_page_create_pulse_custom_pulse_page(), "Pulses page - Create Custom Pulse header")
        soft_assertion.assert_false(self.pulses.verify_pulses_page_duplicate_pulse_button(), "Custom Pulse - Duplicate Pulse button")
        soft_assertion.assert_false(self.pulses.verify_pulses_page_edit_pulse_button(), "Custom Pulse - Edit Pulse button")
        soft_assertion.assert_false(self.pulses.verify_pulses_page_delete_pulse_button(), "Custom Pulse - Delete Pulse button")

        #Create, Edit, Duplicate and Delete Sentiment Pulse
        soft_assertion.assert_false(self.pulses.verify_pulses_page_create_pulse_sentiment_pulse_page(), "Pulses page - Create Sentiment Pulse header")
        soft_assertion.assert_false(self.pulses.verify_pulses_page_duplicate_pulse_button(), "Sentiment Pulse - Duplicate Pulse button")
        soft_assertion.assert_false(self.pulses.verify_pulses_page_edit_pulse_button(), "Sentiment Pulse - Edit Pulse button")
        soft_assertion.assert_false(self.pulses.verify_pulses_page_delete_pulse_button(), "Sentiment Pulse - Delete Pulse button")
    
        # Generate report for soft assertions
        soft_assertion.generate_report("Test Results - Pulses", "Pro Lost Device Admin")

        # Export report to txt file
        # soft_assertion.export_report_to_txt(filename="report_pulses_page.txt", title="Soft Assert Report", message="Pro Lost Device Admin")
 
        # Raise exception if any soft assertions failed
        soft_assertion.raise_assertion_errors("Pro Lost Device Admin")
    
    def test_13_verify_pro_lost_device_admin_permission_set_for_integrations_page(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        soft_assertion.clear()

        # Verify Integrations Side Menu button
        soft_assertion.assert_true(self.home.verify_sidemenu_integrations_button(), "Side menu Integrations button")
        self.home.click_sidemenu_integrations_button()

        # Perform soft assertions for Integrations page
        soft_assertion.assert_true(self.integrations.verify_integrations_page(), "Integrations page")
        soft_assertion.assert_true(self.integrations.verify_integrations_page_service_now_widget(), "Integrations page - Service Now Connector widget")
        soft_assertion.assert_true(self.integrations.verify_integrations_page_tableau_widget(), "Integrations page - Tableau widget")
        soft_assertion.assert_true(self.integrations.verify_integrations_page_entra_id_accounts_widget(), "Integrations page - Entra ID Accounts widget")
        soft_assertion.assert_true(self.integrations.verify_integrations_page_power_automate_widget(), "Integrations page - Power Automate widget")
        soft_assertion.assert_true(self.integrations.verify_integrations_page_entra_id_groups_widget(), "Integrations page - Entra ID Groups widget")
        soft_assertion.assert_true(self.integrations.verify_integrations_page_power_bi_widget(), "Integrations page - Power BI widget")

        soft_assertion.assert_false(self.integrations.verify_integrations_page_service_now_widget_connect_button(), "Integrations page - Service Now widget - Connect button")
        soft_assertion.assert_false(self.integrations.verify_integrations_page_power_bi_widget_configure_button(), "Integrations page - Power BI widget - Configure button")
        soft_assertion.assert_false(self.integrations.verify_integrations_page_power_automate_widget_connect_button(), "Integrations page - Power Automate widget - Connect button")
        soft_assertion.assert_false(self.integrations.verify_integrations_page_tableau_widget_configure_button(), "Integrations page - Tableau widget - Configure button")
        soft_assertion.assert_false(self.integrations.verify_integrations_page_entra_id_group_widget_connect_button(), "Integrations page - Entra ID Groups widget - Connect button")
        soft_assertion.assert_false(self.integrations.verify_integrations_page_entra_id_account_widget_connect_button(), "Integrations page - Entra ID Accounts widget - Connect button")
        soft_assertion.assert_false(self.integrations.verify_integrations_page_entra_id_accounts_widget_upgrade_button(), "Integrations page - Entra ID Accounts widget - Upgrade button")

        soft_assertion.assert_equal(self.integrations.get_integrations_page_info_message(), "Integrations management is only available to users with the Connector Admin role.", "Integrations page - Info message")

        soft_assertion.assert_true(self.integrations.verify_integrations_page_view_all_button(), "Integrations page - View All button")
        soft_assertion.assert_true(self.integrations.verify_integrations_page_active_button(), "Integrations page - Active button")
        soft_assertion.assert_true(self.integrations.verify_integrations_page_inactive_button(), "Integrations page - Inactive button")

        # Generate report for soft assertions
        soft_assertion.generate_report("Test Results - Integrations", "Pro Lost Device Admin")

        # Export report to txt file
        # soft_assertion.export_report_to_txt(filename="report_integrations_page.txt", title="Soft Assert Report", message="Pro Lost Device Admin")
 
        # Raise exception if any soft assertions failed
        soft_assertion.raise_assertion_errors("Pro Lost Device Admin")

    def test_14_verify_pro_lost_device_admin_permission_set_for_alerts_page(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        soft_assertion.clear()

        # Verify Alerts Side Menu button
        soft_assertion.assert_false(self.home.verify_sidemenu_alerts_button(), "Side menu Alerts button")

        #Perform soft assertions on Alerts dropdown options
        soft_assertion.assert_false(self.home.verify_sidemenu_active_alerts_button(), "Side menu Active Alerts button")
        soft_assertion.assert_false(self.home.verify_sidemenu_alerts_management_button(), "Side menu Alerts Management button")

        # Perform soft assertions for Active Alerts page
        soft_assertion.assert_false(self.alerts.verify_active_alerts_page_alerts_table(), "Active Alerts page - Active Alerts table")

        # Perform soft assertions for Alerts Management page
        soft_assertion.assert_false(self.alerts.verify_alerts_management_page_alerts_table(), "Alerts Management page - Alerts table")
        soft_assertion.assert_false(self.alerts.verify_alerts_management_page_enable_alerts_button(), "Alerts Management page - Enable Alerts button")
        soft_assertion.assert_false(self.alerts.verify_alerts_management_page_disable_alerts_button(), "Alerts Management page - Disable Alerts button")
        soft_assertion.assert_false(self.alerts.verify_alerts_management_page_delete_alerts_button(), "Alerts Management page - Delete Alerts button")

        # Generate report for soft assertions
        soft_assertion.generate_report("Test Results - Alerts", "Pro Lost Device Admin")

        # Export report to txt file
        # soft_assertion.export_report_to_txt(filename="reports_alerts_page.txt", title="Soft Assert Report", message="Pro Lost Device Admin")
 
        # Raise exception if any soft assertions failed
        soft_assertion.raise_assertion_errors("Pro Lost Device Admin")
    
    def test_15_verify_pro_lost_device_admin_permission_set_for_labs_page(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        soft_assertion.clear()

        # Perform soft assertions for Labs page
        soft_assertion.assert_false(self.home.verify_sidemenu_labs_button(), "Side menu Labs button")

        # Generate report for soft assertions
        soft_assertion.generate_report("Test Results - Labs", "Pro Lost Device Admin")

        # Export report to txt file
        # soft_assertion.export_report_to_txt(filename="reports_labs_page.txt", title="Soft Assert Report", message="Pro Lost Device Admin")

        # Raise exception if any soft assertions failed
        soft_assertion.raise_assertion_errors("Pro Lost Device Admin")

    def test_16_verify_pro_lost_device_admin_permission_set_for_onboarding_notifications(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        soft_assertion.clear()

        soft_assertion.assert_true(self.home.verify_onboarding_notifications_button(), "Onboarding Notification button")
        self.home.click_onboarding_notifications_button()
        soft_assertion.assert_true(self.home.verify_onboarding_notifications_popup(), "Onboarding Notification popup with detailed steps")

        # Onboarding Notification: Verify First Steps
        soft_assertion.assert_equal(self.home.verify_onboarding_notifications_first_steps_title(), "First steps", "Onboarding Notification - First Steps title")
        soft_assertion.assert_false(self.home.verify_add_device_notification_button(), "Onboarding Notification - Add Device button")
        soft_assertion.assert_false(self.home.verify_invite_team_notification_button(), "Onboarding Notification - Invite Team button")
        soft_assertion.assert_false(self.home.verify_complete_your_profile_notification_button(), "Onboarding Notification - Complete Your Profile button")
        soft_assertion.assert_true(self.home.verify_explore_integrations_notification_button(), "Onboarding Notification - Explore Integrations button")
        
        # Onboarding Notification: Discover More
        soft_assertion.assert_equal(self.home.verify_onboarding_notifications_discover_more_title(), "Discover more", "Onboarding Notification - Discover More title")
        soft_assertion.assert_false(self.home.verify_stay_up_to_date_alerts_button(), "Onboarding Notification - Stay Up to Date Alerts button")
        soft_assertion.assert_true(self.home.verify_troubleshoot_device_issues_button(), "Onboarding Notification - Troubleshoot Device Issues button")
        soft_assertion.assert_false(self.home.verify_improve_experience_score_notification_button(), "Onboarding Notification - Improve Experience Score button")
        soft_assertion.assert_false(self.home.verify_add_a_script_button(), "Onboarding Notification - Add a Script button")
        soft_assertion.assert_false(self.home.verify_gather_employee_feedback_notification_button(), "Onboarding Notification - Gather Employee Feedback button")
        soft_assertion.assert_false(self.home.verify_understand_workforce_sentiment_notification_button(), "Onboarding Notification - Understand Workforce Sentiment button")
        soft_assertion.assert_true(self.home.verify_get_help_and_provide_feedback_notification_button(), "Onboarding Notification - Get Help and Provide Feedback button")

        self.home.click_explore_integrations_notification_button()
        #verify after click notifications popup closes
        # soft_assertion.assert_false(self.home.verify_onboarding_notifications_popup(), "Onboarding Notification popup with detailed steps")

        soft_assertion.assert_equal(self.home.verify_explore_integrations_notification_alert_message_title(), "Explore Integrations", "Onboarding Notification - Explore Integrations alert message title")
        soft_assertion.assert_equal(self.home.verify_explore_integrations_notification_alert_message1(), "Plug-and-play your essential tools to streamline your workflow.", "Onboarding Notification - Explore Integrations alert message1")
        soft_assertion.assert_equal(self.home.verify_explore_integrations_notification_alert_message2(), "Select Integrations to continue.", "Onboarding Notification - Explore Integrations alert message2")
        soft_assertion.assert_true(self.home.verify_explore_integrations_notification_alert_message_close_button(), "Onboarding Notification - Explore Integrations alert message close button")
        self.home.click_explore_integrations_notification_alert_message_close_button()
        soft_assertion.assert_false(self.home.verify_explore_integrations_notification_alert_message_popup(), "Onboarding Notification - Explore Integrations alert message popup")

        self.home.click_onboarding_notifications_button()
        self.home.click_get_help_and_provide_feedback_notification_button()
        #verify after click notifications popup closes
        soft_assertion.assert_false(self.home.verify_onboarding_notifications_popup(), "Onboarding Notification popup with detailed steps")

        soft_assertion.assert_equal(self.home.verify_get_help_and_provide_feedback_notification_alert_message_title(), "Get help and provide feedback", "Onboarding Notification - Get Help and Provide Feedback alert message title")
        soft_assertion.assert_equal(self.home.verify_get_help_and_provide_feedback_notification_alert_message1(), 'Get self-service assistance anytime in the "Help & Support" section.', "Onboarding Notification - Get Help and Provide Feedback alert message1")
        soft_assertion.assert_equal(self.home.verify_get_help_and_provide_feedback_notification_alert_message2(), "Select Next > button to continue.", "Onboarding Notification - Get Help and Provide Feedback alert message2")

        # Generate report for soft assertions
        soft_assertion.generate_report("Test Results - Onboarding Notifications", "Pro Lost Device Admin")

        # Export report to txt file
        # soft_assertion.export_report_to_txt(filename="report_onboaring_notifications.txt", title="Soft Assert Report", message="Pro Lost Device Admin")
        
        # Raise exception if any soft assertions failed
        soft_assertion.raise_assertion_errors("Pro Lost Device Admin")

    def test_17_verify_pro_lost_device_admin_permission_set_for_notification_center(self):
        # 
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        soft_assertion.clear()

        soft_assertion.assert_true(self.home.verify_notification_bell_button(), "Notification Bell button")
        self.home.click_notification_center_bell_button()
        soft_assertion.assert_true(self.home.verify_notifications_center_popup(), "Notification Center popup")
        soft_assertion.assert_equal(self.home.get_notification_center_popup_title(), "Notification Center", "Notification Center popup title")
        
        soft_assertion.assert_false(self.home.verify_notification_center_alerts_section(), "Notification Center - Alerts section")
        soft_assertion.assert_false(self.home.verify_notification_center_notifications_section(), "Notification Center - Notifications section")

        # Generate report for soft assertions
        soft_assertion.generate_report("Test Results - Notification Center", "Pro Lost Device Admin")

        # Export report to txt file
        # soft_assertion.export_report_to_txt(filename="report_notifications_center.txt", title="Soft Assert Report", message="Pro Lost Device Admin")
        
        # Raise exception if any soft assertions failed
        soft_assertion.raise_assertion_errors("Pro Lost Device Admin")