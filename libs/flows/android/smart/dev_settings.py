from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
from MobileApps.resources.const.android.const import PACKAGE, LAUNCH_ACTIVITY


class DevSettings(SmartFlow):
    flow_name = "dev_settings"

    PIE_STACK = "pie_stack_cb"
    STAGE_STACK = "stage_stack_cb"
    PRODUCTION_STACK = "production_stack_cb"

    WEBAPP_PIE_STACK = "webapps_stack_pie"
    WEBAPP_STAGE_STACK = "webapps_stack_stage"
    WEBAPP_PRODUCTION_STACK = "webapps_stack_prod"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def open_select_settings_page(self):
        """
        Launch Select Settings Page Screen
        """
        package_name = PACKAGE.SMART(self.driver.session_data["pkg_type"])
        self.driver.start_activity(package_name, LAUNCH_ACTIVITY.SMART_DEV_SETTINGS)

    def change_stack_server(self, stack_name, webapp_stack_name):
        """
        change stack server in HPC Settings
        :param stack_name: using class constant
                    - PIE_STACK
                    - STAGE_STACK
                    - PRODUCTION_STACK
        """
        setting_str = self.driver.return_str_id_value("server_stack_txt")
        self._search_for_setting(setting_str)
        self.driver.click("server_stack_cell", format_specifier=[setting_str])
        self.driver.click(stack_name)

        webapp_stack_str = self.driver.return_str_id_value("web_app_stack_txt")
        self._search_for_setting(webapp_stack_str)
        self.driver.click("server_stack_cell", format_specifier=[webapp_stack_str])
        self.driver.click(webapp_stack_name)

    def toggle_authz_credentials(self, on=True):
        """
        Toggle the Authz Credentials option
        """
        setting_str = self.driver.return_str_id_value("authz_credentials_txt")
        self._search_for_setting(setting_str)
        self.driver.wait_for_object("toggle_switch", format_specifier=[setting_str])
        self.driver.check_box("toggle_switch", format_specifier=[setting_str], uncheck=not on)

    def toggle_detect_leaks_switch(self, on=True):
        """
        toggle switch of Detect leaks option 
        """
        setting_str = self.driver.return_str_id_value("detect_leaks_txt")
        self._search_for_setting(setting_str)
        self.driver.wait_for_object("toggle_switch", format_specifier=[setting_str])
        self.driver.check_box("toggle_switch", format_specifier=[setting_str], uncheck=not on)

    def toggle_log_unloggables(self, on=True):
        """
        Toggle the Log Unloggables option
        """
        setting_str = self.driver.return_str_id_value("log_unloggables_txt")
        self._search_for_setting(setting_str)
        self.driver.wait_for_object("toggle_switch", format_specifier=[setting_str])
        self.driver.check_box("toggle_switch", format_specifier=[setting_str], uncheck=not on)

    def toggle_shortened_token_lifespan(self, on=True):
        setting_str = self.driver.return_str_id_value("shortened_token_lifespan")
        self._search_for_setting(setting_str)
        self.driver.wait_for_object("toggle_switch", format_specifier=[setting_str])
        self.driver.check_box("toggle_switch", format_specifier=[setting_str], uncheck=not on)

    def _search_for_setting(self, search_txt):
        """
        Searches dev setting with the specified string
        :param search_txt: The string to use for the search
        """
        self.driver.click("search_btn", raise_e=False)
        self.driver.send_keys("search_txtbox", search_txt)

    def toggle_delete_account(self, on=True):
        """
        Toggle the Delete Account option
        """
        setting_str = self.driver.return_str_id_value("delete_account_title")
        self.driver.wait_for_object("toggle_switch", format_specifier=[setting_str])
        self.driver.check_box("toggle_switch", format_specifier=[setting_str], uncheck=not on)

    def toggle_duplex_photo_printing(self, on=True):
        """
        Toggle the Duplex Photo Printing option
        """
        setting_str = self.driver.return_str_id_value("duplex_photo_printing_title")
        self._search_for_setting(setting_str)
        self.driver.wait_for_object("toggle_switch", format_specifier=[setting_str])
        self.driver.check_box("toggle_switch", format_specifier=[setting_str], uncheck=not on)

    def toggle_mfe_flow(self, on=True):
        """
        Enable MFE Flow for HPX project
        """
        locator_list = [
                            "enable_mfe_flow_title", "enable_mfe_flow_activities_nav_title",
                            "enable_hpx_ui_style","enable_hpx_print_ui_style","enable_hpx_consents_reskin_ui_style",
                            "enable_oobe_reskin_ui_style","enable_becon_flow_reskin_ui_style",
                            "enable_oobe_reskin_ui_style","enable_becon_flow_reskin_ui_style", "enable_formadjr_theme",
                            "hpx_od_clientid", "hpx_ows_clientid", "mns_hpx_clientid", "hpx_od_clientid", 
                            "hpx_ows_clientid", "mns_hpx_clientid", "enable_hpx_shorcuts_web_solution"
                    ]
        for locator in locator_list:
            setting_str = self.driver.return_str_id_value(locator)
            self._search_for_setting(setting_str)
            self.driver.wait_for_object("toggle_switch", format_specifier=[setting_str])
            self.driver.check_box("toggle_switch", format_specifier=[setting_str], uncheck=not on)