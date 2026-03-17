import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_01_Support(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.profile = request.cls.fc.fd["profile"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.hpx_support = request.cls.fc.fd["hpx_support"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.virtual_assistant = request.cls.fc.fd["virtual_assistant"]
        cls.add_device = request.cls.fc.fd["add_device"]
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        request.cls.fc.web_password_credential_delete()
        yield
        request.cls.fc.change_system_region_to_united_states()

    @pytest.mark.regression
    def test_01_verify_sidebar_support_link_navigation_C66179104(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_profile_setting_page_content(), "Profile Settings page content missing"
        assert self.profile.verify_support_device_btn(), "Support device button missing"
        self.profile.click_support_device_btn()
        assert self.device_card.verify_pc_devices_back_button(), "PC Devices back button is not displayed"
        assert self.hpx_support.verify_add_a_device_btn_support_page(), "Add a Device button on Support page is not displayed"
        assert self.hpx_support.verify_support_side_panel_title(), "Support side panel title missing"

    @pytest.mark.regression
    def test_02_verify_more_info_tab_under_product_info_card_C66179119(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC Device name is not displayed"
        assert self.devices_details_pc_mfe.verify_product_information_title_show_up(), "Product Information title is not displayed"
        assert self.devices_details_pc_mfe.verify_more_information_button_show(), "More Information button is not displayed"
        self.devices_details_pc_mfe.click_more_information_button()
        assert self.devices_details_pc_mfe.verify_general_specifications_title_show(), "General Specifications title is not displayed"
        assert self.devices_details_pc_mfe.verify_more_information_panel(), "More Information panel is not displayed"

    @pytest.mark.regression
    def test_03_verify_get_help_card_in_device_details_page_C66179120(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC Device name is not displayed"
        logging.info("verifying Get Help card Module in Device Details Page")
        assert self.devices_details_pc_mfe.verify_get_help_module_show_up(), "Get Help module is not displayed"
        assert self.devices_details_pc_mfe.verify_start_virtual_assistant_button_show_up(), "Start Virtual Assistant button is not displayed"
        assert self.devices_details_pc_mfe.verify_view_manual_and_guides_link_show_up(), "View Manual and Guides link is not displayed"
        assert self.devices_details_pc_mfe.verify_find_a_repair_center_link_show_up(), "Find a Repair Center link is not displayed"
        assert self.devices_details_pc_mfe.verify_start_a_repair_order_link_show_up(), "Start a Repair Order link is not displayed"
        assert self.devices_details_pc_mfe.verify_get_more_help_on_our_website_link(), "Get More Help on Our Website link is not displayed"
        assert self.devices_details_pc_mfe.verify_contact_us_button_show_up(), "Contact Us button is not displayed"

    @pytest.mark.regression
    def test_04_verify_clicking_contact_us_and_virtual_assistant_C66179152(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC Device name is not displayed"
        assert self.devices_details_pc_mfe.verify_get_help_module_show_up(), "Get Help module is not displayed"
        self.devices_details_pc_mfe.click_contact_us_button()
        assert self.devices_details_pc_mfe.verify_contact_us_panel(), "Contact Us panel is not displayed"
        self.devices_details_pc_mfe.click_back_devices_button()
        assert self.devices_details_pc_mfe.verify_start_virtual_assistant_button_show_up(), "Start Virtual Assistant button is not displayed"
        self.devices_details_pc_mfe.click_start_virtual_assistant_button()
        assert self.virtual_assistant.verify_virtual_assistant_side_panel() ,"Virtual Assistant side panel is not displayed"

    @pytest.mark.regression
    def test_05_verify_troubleshooting_fixes_buttons_C66179154(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC Device name is not displayed"
        assert self.devices_details_pc_mfe.verify_trouble_shoot_fix(), "Troubleshooting & Fixes section is not displayed"
        assert self.devices_details_pc_mfe.verify_trouble_shoot_panel(), "Troubleshooting & Fixes panel is not displayed"

    @pytest.mark.regression
    def test_06_verify_device_update_card_C74902553(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC Device name is not displayed"
        assert self.devices_details_pc_mfe.verify_device_updates(), "Device Update is not displayed"

    @pytest.mark.regression
    def test_07_click_and_verify_device_updates_page_C74903300(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC Device name is not displayed"
        assert self.devices_details_pc_mfe.verify_device_updates(), "Device Update is not displayed"
        assert self.devices_details_pc_mfe.click_on_check_for_updates() ,"Virtual Assistant side panel is not displayed"
        assert self.devices_details_pc_mfe.verify_check_for_updates_page(), "No updates available message is not displayed"

    @pytest.mark.regression
    def test_08_verify_add_device_in_support_C67873688(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_profile_setting_page_content(), "Profile Settings page content missing"
        assert self.profile.verify_support_device_btn(), "Support device button missing"
        self.profile.click_support_device_btn()
        self.hpx_support.click_add_a_device_btn_support_page()
        assert self.add_device.verify_add_device_page(), "add device page is not found"
