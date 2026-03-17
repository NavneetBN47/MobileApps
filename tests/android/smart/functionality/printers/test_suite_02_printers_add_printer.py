from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import PACKAGE
import pytest

pytest.app_info = "SMART"

class Test_Suite_02_Printers_Add_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.printers = cls.fc.flow[FLOW_NAMES.PRINTERS]

    @pytest.fixture(scope="function")
    def disable_location_services(self):
        """Fixture to turn off location services for a single test"""
        self.driver.toggle_location_services(on=False)
        yield
        self.driver.toggle_location_services(on=True)

    @pytest.fixture(scope="function")
    def disable_bluetooth(self):
        """Fxture to turn off bluetooth for a single test"""
        self.driver.toggle_bluetooth(on=False)
        yield
        self.driver.toggle_bluetooth(on=True)

    def test_01_add_printer_ui(self):
        """
        Description: C31297093, C31297094, C31297095, C31297528
         1. Load Home screen
         2. Click on big "+" or small "+" icon on Home screen
         3. Click on Get Started
         4. Select Wifi and continue
         5. Select continue
         6. Allow App permission
        Expected Results:
         6. Verify Add Printer screen
           + Title
           + Message screen
           + My Printer is not listed button
        """
        # Make sure the printer isn't connected when launch the app
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.load_printer_selection()
        self.printers.load_printer_setup_screen()
        if int(self.driver.platform_version) > 9:
            # Timeout 25s here, because Printer searching lists need take a while, and Printer Not Listed? button will display after that
            self.printers.verify_printer_setup_screen(timeout=25)
        else:
            self.printers.verify_add_printers_screen()

    def test_02_my_printer_not_listed_cancel_btn(self):
        """
        Description: C31297096
         1. Load to Add Printer screen
         2. Click on My Printer is not listed button
         3. Click on Cancel button

        Expected Result:
         2. Verify My Printer is not listed screen:
            + Dropdown menu button
            + Message: Use this app to set up the following wireless printers....
         3. Verify Home screen without printer connected
        """
        self.__load_my_printer_is_not_listed_screen()
        self.printers.verify_setup_printers_instruction_screen()
        self.printers.verify_try_again_button()
        self.printers.select_print_setup_cancel()
        self.home.verify_home_no_printer_connected()

    def test_03_instruction_my_printer_not_listed(self):
        """
        Description: C31297097
         1. Load to Add Printer screen
         2. Click on My Printer is not listed button
         3. Click on dropdown menu
         4. Select -My Printer is not listed-


        Expected Result:
         4. Verify Setup printer instruction screen with below message:
            + Your printer cannot be configured with this app. To ...etc (Verify the text)
        """
        self.__load_printer_setup_printer_model_screen(model=self.driver.return_str_id_value(self.printers.MY_PRINTER_IS_NOT_LISTED,
                                                                                               project="smart",
                                                                                               flow="printers"))
        self.printers.verify_my_printer_not_listed_help_msg()

    def test_04_my_printer_not_listed_instruction_setup_mode_link(self):
        """
        Description: C31297098, C31297099
         1. Load to Select your printer dropdown lists
         2. Click on any printer from the list
         3. Click on "How do I do this?" link
         4. Click on Ok button

        Expected Result:
         3. Verify How do I make sure printer in setup mode screen:
            + Title
        """
        self.__load_printer_setup_printer_model_screen(model="HP Envy")
        self.printers.verify_my_printer_setup_instruction()
        self.printers.select_setup_instruction_link(is_network=False)
        self.printers.verify_setup_instruction_link_popup(is_network=False)
        self.printers.select_setup_instruction_popup_ok(is_network=False)

    def test_05_my_printer_not_listed_instruction_network_link(self):
        """
        Description: C31297100
         1. Load to Select your printer dropdown lists
         2. Click on any printer from the list
         3. Click on "How do I do this?" link
         4. Click on Ok button

        Expected Result:
         3. Verify How do I find my network name and pwd screen:
            + Title
        :return:
        """
        self.__load_printer_setup_printer_model_screen(model="HP Envy")
        self.printers.select_setup_instruction_link(is_network=True)
        self.printers.verify_setup_instruction_link_popup(is_network=True)
        self.printers.select_setup_instruction_popup_ok(is_network=True)

    def test_06_my_printer_not_listed_instruction_try_again(self):
        """
        Description:
         1. Load to Select your printer dropdown lists
         2. Click on any printer from the list
         3. Check one of 2 check boxes
         4. Check another check box, and Click Try Again button

        Expected Result:
         3. Try Again button is still disabled to click
         6. Verify Add Printer screen
        """
        self.__load_printer_setup_printer_model_screen(model="HP Envy")
        self.printers.toggle_setup_instruction_checkbox(is_network=False, enable=True)
        self.printers.verify_try_again_button()
        self.printers.toggle_setup_instruction_checkbox(is_network=True, enable=True)
        self.printers.verify_try_again_button(is_enabled=True)
        self.printers.select_printer_setup_try_again()
        if int(self.driver.platform_version) > 9:
            # Timeout 25s here, because Printer searching lists need take a while, and Printer Not Listed? button will display after that
            self.printers.verify_printer_setup_screen(timeout=25)
        else:
            self.printers.verify_add_printers_screen()

    @pytest.mark.parametrize("connection,route", [("ethernet", "home"), ("ethernet", "value_prop"), ("wifi", "home"), ("wifi", "value_prop")])
    def test_07_load_printer_setup_screen(self, connection, route):
        """
        Description: C29504500, C29504502, C29504499 & C29504501
         1. Open Smart app
         2. Load Printer connection screen
          a. If route is "value_prop", At Value Prop select "Set up a new printer"
          b. Else, Load to home screen and Select Add new printer or + button on top navbar
         3. Select connection type(Wifi or Ethernet) and continue
         4. Select continue
        Expected Result:
         3. Verify connectivity screen(C29504500/C29504499)
          - header text
          - continue button
         4. Verify Printers setup screen(C29504502/C29504501)
        """
        if route == "value_prop":
            self.fc.flow_load_printer_screen_from_value_prop()
        else:
            self.fc.flow_load_home_screen(skip_value_prop=True)
            self.home.load_printer_selection()
            self.printers.select_printer_option_get_started()
        if connection == "ethernet":
            self.printers.select_ethernet_connection()
            self.printers.verify_connect_ethernet_screen()
            self.printers.select_setup_continue()
        else:
            self.printers.select_wifi_connection()
            self.printers.verify_connect_wifi_screen()
            self.printers.select_setup_continue(is_permission=int(self.driver.platform_version) > 11)
            self.printers.select_location_usage_ok_button()
        self.printers.verify_printer_setup_screen(connection=connection)

    @pytest.mark.parametrize("connection", ["ethernet", "wifi"])
    def test_08_back_from_prepare_connection_screen(self, connection):
        """
        Description: C29504515 & C29504504
         1. Open Smart app
         2. From Value Prop screen select "Setup a new printer"
         3. Select connection type(Wifi or Ethernet) and continue
         4. Press back button
        Expected Result:
         4. Verify connection type screen
        """
        self.fc.flow_load_printer_screen_from_value_prop()
        if connection == "ethernet":
            self.printers.select_ethernet_connection()
        else:
            self.printers.select_wifi_connection()
        self.driver.press_key_back()
        self.printers.verify_printer_connection_type_screen()

    def test_09_wifi_learn_more(self):
        """
        Description: C29504559 & C29504564
         1. Open Smart app
         2. From Value Prop screen select "Setup a new printer"
         3. Select Wifi and continue
         4. Select Learn More
         5. Select Ok
        Expected Results:
         4. Verify learn more popup(C29504559)
          - title text
          - body text
          - ok button
         5. Verify learn more popup is invisible
        """
        self.fc.flow_load_printer_screen_from_value_prop()
        self.printers.select_wifi_connection()
        self.printers.select_wifi_screen_learn_more()
        self.printers.verify_prepare_wifi_learn_more_popup()
        self.printers.select_wifi_learn_more_ok_button()
        self.printers.verify_prepare_wifi_learn_more_popup(invisible=True)

    @pytest.mark.parametrize("path", ["value_prop", "home"])
    def test_10_exit_printer_setup(self, path):
        """
        Description: C31297531, C31297529
         1. Open Smart app
         2. Navigate to Add Printer screen
          if path == "value_prop"
           a. At value prop select "Setup a new printer"
           b. Select Ethernet
           c. Select Continue
          if path == "home"
           a. Skip value prop
           b. Select Add your first printer(or + on top navbar)
           c. Select Add Printer
         3. Select Printer's not listed
         4. Select Search again
         5. Select Printer's not listed
         6. Select Exit Setup
        Expected Results:
         4. Verify add printer screen
         6. Verify home screen
        """
        if path == "home":
            self.fc.flow_load_home_screen(skip_value_prop=True)
            self.home.load_printer_selection()
            self.printers.select_printer_option_add_printer()
        else:
            self.fc.flow_load_printer_screen_from_value_prop()
            self.printers.select_ethernet_connection()
            self.printers.select_setup_continue()
        self.printers.select_my_printer_is_not_listed()
        self.printers.select_search_again_button()
        self.printers.verify_add_printers_screen()
        self.printers.select_my_printer_is_not_listed()
        self.printers.select_exit_setup_button()
        self.home.verify_home_nav()

    @pytest.mark.parametrize("consent", ["allow", "deny"])
    def test_11_wifi_printer_location_consent(self, consent):
        """
        Description: C29735176, C29735177, C29735178 & C29735179
         1. Open Smart app(may reset to access value_prop)
         2. Select "Setup a new Printer" at value prop
         3. Select Wifi and continue
         4. Select continue
         5. Select OK
         6. Allow or Deny permission based on consent param
        Expected Results:
         4. Verify "Using Location Data" popup
         5. Verify consent popup
         6. If consent == "allow" verify printer setup screen
            If consent == "deny" verify all permissions popup
        """
        if int(self.driver.platform_version) > 11:
            pytest.skip("Test case covered by test_16_advanced_location_consent for android 12+")
        self.driver.toggle_location_services()
        self.fc.flow_load_printer_screen_from_value_prop()
        self.printers.select_wifi_connection()
        self.printers.select_setup_continue(is_permission=int(self.driver.platform_version) > 11)
        self.printers.verify_location_usage_popup()
        self.printers.select_location_usage_ok_button(is_permission=False)
        assert self.printers.is_app_permission_popup(), "Expected permission popup"
        self.printers.check_run_time_permission(accept=consent == "allow")
        if consent == "allow":
            self.printers.verify_printer_setup_screen()
        else:
            self.printers.verify_provide_permissions_popup(permission="all_permissions")

    @pytest.mark.parametrize("consent", ["allow", "deny"])
    def test_12_wifi_printer_bluetooth_consent(self, consent, disable_bluetooth):
        """
        Description: C29735180, C29735181 & C29735182
         1. Toggle Bluetooth Off and Open Smart app
         2. Select "Setup a new Printer" at value prop
         3. Select Wifi and continue
         4. Select continue
         5. Select OK
         6. Grant location permission
         7. Select Continue
         8. Allow or Deny permission based on consent param
        Expected Results:
         7. Verify Turn on Bluetooth popup
         8. if consent == "allow": Verify printer setup screen
            if consent == "deny": Verify "Provide Location and Bluetooth..." screen
        """
        if int(self.driver.platform_version) < 10:
            pytest.skip("Only applies to android 10+")
        self.fc.flow_load_printer_screen_from_value_prop()
        self.printers.select_wifi_connection()
        self.printers.select_setup_continue(is_permission=int(self.driver.platform_version) > 11)
        self.printers.select_location_usage_ok_button()
        self.printers.verify_turn_on_bluetooth_popup()
        self.printers.select_turn_on_bluetooth_continue_btn()
        assert self.printers.is_app_permission_popup(), "Expected permissions popup"
        self.printers.check_run_time_permission(accept=consent == "allow")
        if consent == "allow":
            self.printers.verify_printer_setup_screen()
        else:
            self.printers.verify_provide_permissions_popup(permission="all_permissions")

    def test_13_location_services_off(self, disable_location_services):
        """
        Description: C29735643 & C29735176
         1. Turn off location services
         2. Reset and launch smart app
         3. Select "Set up a new printer" from value prop
         4. Select Wifi and Continue
         5. Select Continue
         6. Accept Permissions
        Expected Results:
         6. Verify "Turn on location..." popup
        """
        if int(self.driver.platform_version) < 10:
            pytest.skip("Only applies to android 10+")
        self.fc.flow_load_printer_screen_from_value_prop()
        self.printers.select_wifi_connection()
        self.printers.select_setup_continue(is_permission=int(self.driver.platform_version) > 11)
        self.printers.verify_location_usage_popup()
        self.printers.select_location_usage_ok_button(is_permission=False)
        assert self.printers.is_app_permission_popup(), "Expected permissions popup"
        self.printers.check_run_time_permission()
        self.printers.verify_turn_on_location_popup()
        self.driver.press_key_back()  # close location popup to avoid impacting subsequent tests

    @pytest.mark.parametrize("consent,path", [("allow", None), ("deny", "exit"), ("deny", "permissions")])
    def test_14_nearby_device_permission(self, consent, path):
        """
        Description: C29736264, C29736265, C29736266, C29736267, C29736268, C29735598, C29735597, C29735634 & C29735642
         1. Open Smart app(may reset to access value_prop)
         2. Select "Setup a new Printer" at value prop
         3. Select Wifi and continue
         4. Select continue
         5. Select "Allow" or "Deny" based on consent param
         If consent == "deny"
          6. Select "Open Permissions" or "Exit Setup" on location usage popup
         If consent == "allow"
          6. Select continue on location usage popup
          7. Allow location usage
        Expected Results:
         4. Verify system permissions popup appeared
         6. If consent == "deny" and path == "exit" Verify smart home screen
          If consent == "deny" and path == "permissions" Verify Android Settings app opened
         7. If consent == "allow" Verify printer setup screen
        """
        if int(self.driver.platform_version) < 12:
            pytest.skip("Only applies to android 12+")
        self.driver.toggle_location_services()
        self.fc.flow_load_printer_screen_from_value_prop()
        self.printers.select_wifi_connection()
        self.printers.select_setup_continue(is_permission=consent == "allow")
        self.printers.check_run_time_permission(accept=consent == "allow")
        if consent == "allow":
            self.printers.select_location_usage_ok_button()
            self.printers.verify_printer_setup_screen()
        elif consent == "deny":
            self.printers.select_permissions_popup_button(path)
            if path == "exit":
                self.home.verify_home_nav()
            else:
                assert self.driver.get_current_app_activity()[0] == PACKAGE.SETTINGS, "Expected android settings to open"

    @pytest.mark.parametrize("consent,precision", [("allow", "precise"), ("deny", "precise"), ("deny", "approximate")])
    def test_15_advanced_location_consent(self, consent, precision):
        """
        Description: C29736272 & C29736274
         1. Open Smart app(may reset to access value_prop)
         2. Select "Setup a new Printer" at value prop
         3. Select Wifi and continue
         4. Select continue
         5. Select OK button
         6. Handle location consent
          Select Approximate or Precise based on precision param
          Select consent response based on consent param
        Expected Results:
         6. If consent is allow
           Verify printer setup screen
          If consent is deny
           Verify provide precise location permissions popup
        """
        if int(self.driver.platform_version) < 12:
            pytest.skip("Only applies to android 12+")
        self.fc.reset_app()
        self.fc.flow_load_printer_screen_from_value_prop()
        self.printers.select_wifi_connection()
        self.printers.select_setup_continue(is_permission=True)
        self.printers.check_run_time_permission()
        self.printers.select_location_usage_ok_button(is_permission=False)
        self.printers.check_run_time_permission(accept=consent == "allow", location_precision=precision)
        if consent == "allow":
            self.printers.verify_printer_setup_screen()
        else:
            self.printers.verify_provide_permissions_popup(permission="precise_location")

    @pytest.mark.parametrize("consent,consent_type", [("allow", "foreground_only"), ("allow", "one_time"), ("deny", None)])
    def test_16_approximate_location_redirect(self, consent, consent_type):
        """
        Description: C29736275, C29736276, C29736278 & C29736279
         1. Open Smart app(may reset to access value_prop)
         2. Select "Setup a new Printer" at value prop
         3. Select Wifi and continue
         4. Select continue
         5. Select OK button
         6. Select approximate location and select consent based on consent_type param
         7. Approve or deny permission popup based on consent param
         8. If consent == "deny" deny additional permission request
        Expected Results:
         6. Verify a system permission popup appears
         7. If consent == "allow"
          Verify printer setup screen
         8. If consent == "deny"
          Verify provide permissions popup
        """
        if int(self.driver.platform_version) < 12:
            pytest.skip("Only applies to android 12+")
        self.fc.reset_app()
        self.fc.flow_load_printer_screen_from_value_prop()
        self.printers.select_wifi_connection()
        self.printers.select_setup_continue(is_permission=True)
        self.printers.select_location_usage_ok_button(is_permission=False)
        self.printers.check_run_time_permission(location_precision="approximate", consent_type=consent_type)
        assert self.printers.is_app_permission_popup(), "Expected permissions popup"
        self.printers.check_run_time_permission(accept=consent == "allow")
        if consent == "allow":
            self.printers.verify_printer_setup_screen()
        else:
            self.printers.check_run_time_permission(accept=False)
            self.printers.verify_provide_permissions_popup(permission="all_permissions")

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_my_printer_is_not_listed_screen(self):
        """
       - Click on My printer is not listed button on Android 7/8/9 or click on Get More Help button on Android 10 or higher
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.load_printer_selection()
        self.printers.load_printer_setup_screen()
        if self.printers.verify_search_printers_popup(raise_e=False):
            self.printers.select_search_printers_popup_continue(is_permission=True)
        if int(self.driver.platform_version) > 9:
            # Timeout 25s here, because Printer searching lists need take a while, and Printer Not Listed? button will display after that
            self.printers.verify_printer_setup_screen(timeout=25)
        else:
            self.printers.verify_add_printers_screen()
        
        self.printers.select_my_printer_is_not_listed()
        if int(self.driver.platform_version) > 9:
            #App need to some time to load printer list
            if self.printers.verify_printer_setup_with_printer_not_listed_msg(timeout=30,raise_e=False):
                self.printers.select_get_more_help_button()
            else:
                pytest.skip("Can not test Get More Help Page")

    def __load_printer_setup_printer_model_screen(self, model=None):
        """
        - Load My printer is not listed screen
        - Click on Select your printer, and select a model
        """
        self.__load_my_printer_is_not_listed_screen()
        self.printers.select_printer_setup_printer_model(model=model)