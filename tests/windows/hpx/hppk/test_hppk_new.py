from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
soft_assertion = SoftAssert()

class Test_Suite_HPPK_New_UI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
        time.sleep(5)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()


    @pytest.mark.function
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.ota
    def test_01_programmable_key_ui_C38499258(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(2)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_prog_key_card()
        programmable_key_heading = self.fc.fd["hppk"].verify_programmable_key_heading()
        soft_assertion.assert_equal(programmable_key_heading, "Create personalized shortcuts with the press of a button", "Create personalized shortcuts title is not visible")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_hppk_icon(), "HPPK icon is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_automation_radio_btn(), "Automation", "Automation radio button is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_key_sequence_radio_btn(), "Key sequence", "Key sequence radio button is not visible") 
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_text_input_radio_btn(), "Text input", "Text input radio button is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_myhp_programmable_key_radio_btn(), "myHP Programmable Key", "myHP Programmable Key radio button is not visible")
        soft_assertion.raise_assertion_errors()


    @pytest.mark.function
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.ota
    def test_02_add_action_dropdown_C38499268(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(2)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_prog_key_card()
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_hppk_icon(), "HPPK icon is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_automation_radio_btn(), "Automation", "Automation radio button is not visible")
        self.fc.fd["hppk"].click_automation_radio_btn()
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_add_action(), "Add action button is not visible")
        self.fc.fd["hppk"].click_add_action()
        soft_assertion.assert_equal(self.fc.fd["hppk"].get_application_text(), "Application", "Application text is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].get_folder_text(), "Folder", "Folder text is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].get_file_text(), "File", "File text is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].get_website_text(), "Website", "Website text is not visible")
        soft_assertion.raise_assertion_errors()


    @pytest.mark.ota
    def test_05_programmable_key_ui_hpone_devices_C38499260(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_prog_key_card()
        programmable_key_heading = self.fc.fd["hppk"].verify_programmable_key_heading()
        soft_assertion.assert_equal(programmable_key_heading, "Create personalized shortcuts with the press of a button", "Create personalized shortcuts title is not visible")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_hppk_icon(), "HPPK icon is not visible")
        assert bool(self.fc.fd["hppk"].verify_hppk_icon()) is True
        assert bool(self.fc.fd["hppk"].verify_supportkey_icon()) is True
        assert bool(self.fc.fd["hppk"].verify_pc_prog_key_icon()) is True
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_automation_radio_btn(), "Automation", "Automation radio button is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_key_sequence_radio_btn(), "Key sequence", "Key sequence radio button is not visible") 
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_text_input_radio_btn(), "Text input", "Text input radio button is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_myhp_programmable_key_radio_btn(), "myHP Programmable Key", "myHP Programmable Key radio button is not visible")
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_programmable_key_radio_button_is_selected()))
        soft_assertion.raise_assertion_errors()

    @pytest.mark.ota
    def test_06_programmable_key_icon_s4_ui_C38499261(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_prog_key_card()
        programmable_key_heading = self.fc.fd["hppk"].verify_programmable_key_heading()
        soft_assertion.assert_equal(programmable_key_heading, "Create personalized shortcuts with the press of a button", "Create personalized shortcuts title is not visible")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_hppk_icon(), "HPPK icon is not visible")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_supportkey_icon(), "Support key icon is not visible")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_pc_prog_key_icon(), "PCDevice key icon is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_automation_radio_btn(), "Automation", "Automation radio button is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_key_sequence_radio_btn(), "Key sequence", "Key sequence radio button is not visible") 
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_text_input_radio_btn(), "Text input", "Text input radio button is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_myhp_programmable_key_radio_btn(), "myHP Programmable Key", "myHP Programmable Key radio button is not visible")
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_programmable_key_radio_button_is_selected()))
        soft_assertion.raise_assertion_errors()

    @pytest.mark.ota
    def test_07_support_key_icon_s2_ui_C38499263(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_prog_key_card()
        programmable_key_heading = self.fc.fd["hppk"].verify_programmable_key_heading()
        soft_assertion.assert_equal(programmable_key_heading, "Create personalized shortcuts with the press of a button", "Create personalized shortcuts title is not visible")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_hppk_icon(), "HPPK icon is not visible")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_supportkey_icon(), "Support key icon is not visible")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_pc_prog_key_icon(), "PCDevice key icon is not visible")
        self.fc.fd["hppk"].click_supportkey_icon()
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_automation_radio_btn(), "Automation", "Automation radio button is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_key_sequence_radio_btn(), "Key sequence", "Key sequence radio button is not visible") 
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_text_input_radio_btn(), "Text input", "Text input radio button is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_hp_support_key_radio_btn(), "myHP Support", "myHP support Key radio button is not visible")
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_hpsupport_key_radio_button_is_selected()))
        soft_assertion.raise_assertion_errors()

    @pytest.mark.ota
    def test_08_pc_device_key_icon_s3_ui_C38499265(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_prog_key_card()
        programmable_key_heading = self.fc.fd["hppk"].verify_programmable_key_heading()
        soft_assertion.assert_equal(programmable_key_heading, "Create personalized shortcuts with the press of a button", "Create personalized shortcuts title is not visible")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_hppk_icon(), "HPPK icon is not visible")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_supportkey_icon(), "Support key icon is not visible")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_pc_prog_key_icon(), "PCDevice key icon is not visible")
        self.fc.fd["hppk"].click_pcpkprogrammablekey_icon()
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_automation_radio_btn(), "Automation", "Automation radio button is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_key_sequence_radio_btn(), "Key sequence", "Key sequence radio button is not visible") 
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_text_input_radio_btn(), "Text input", "Text input radio button is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_pc_device_key_radio_btn(), "myHP PC Device", "myHP PC Device radio button is not visible")
        soft_assertion.assert_true(bool(self.fc.fd["hppk"].verify_pcdevice_radio_button_is_selected()))
        soft_assertion.raise_assertion_errors()

    def test_09_verify_invalid_website_url_C38499274(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_prog_key_card()
        self.fc.fd["hppk"].click_automation_radio_btn()
        self.fc.fd["hppk"].click_add_action()
        self.fc.fd["hppk"].click_website()
        self.fc.fd["hppk"].input_url("abcd")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_website_invalid_url_warning_text(), "Invalid website url warning text is not visible")
        self.fc.fd["hppk"].input_url("849876")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_website_invalid_url_warning_text(), "Invalid website url warning text is not visible")
        self.fc.fd["hppk"].input_url("*$test")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_website_invalid_url_warning_text(), "Invalid website url warning text is not visible")
        self.fc.fd["hppk"].input_url(".com")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_website_invalid_url_warning_text(), "Invalid website url warning text is not visible")
        self.fc.fd["hppk"].input_url("www hp com")
        soft_assertion.assert_true(self.fc.fd["hppk"].verify_website_invalid_url_warning_text(), "Invalid website url warning text is not visible")
        soft_assertion.raise_assertion_errors()

    def test_10_verify_website_popup_C38499273(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_prog_key_card()
        self.fc.fd["hppk"].click_automation_radio_btn()
        soft_assertion.assert_equal(self.fc.fd["hppk"].get_assign_text(), "Assign apps, websites, files or folders to open for your shortcut", "automation desc- assign app is not visible")
        self.fc.fd["hppk"].click_add_action()
        soft_assertion.assert_equal(self.fc.fd["hppk"].get_file_text(), "File", "files text is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].get_folder_text(), "Folder", "Folder text is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].get_application_text(), "Application", "Application text is not visible")
        soft_assertion.assert_equal(self.fc.fd["hppk"].get_website_text(), "Website", "Application text is not visible")
        self.fc.fd["hppk"].click_website()
        self.fc.fd["hppk"].input_url("www.google.com")
        self.fc.fd["hppk"].click_website_cancel()
        soft_assertion.assert_equal(self.fc.fd["hppk"].verify_automation_radio_btn(), "Automation", "Automation radio button is not visible")
        soft_assertion.raise_assertion_errors()
