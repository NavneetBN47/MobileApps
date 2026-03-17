import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression","function_setup_myhp_launch")
class Test_Suite_04_Device_Details_Page(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile= request.cls.fc.fd["profile"]
        cls.css = request.cls.fc.fd["css"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        request.cls.fc.web_password_credential_delete()

    @pytest.mark.regression
    def test_01_verify_nickname_on_device_details_page_C65209952(self):
        self.devices_details_pc_mfe.verify_pc_device_name_show_up(raise_e=True)
        assert self.devices_details_pc_mfe.return_nick_name_of_pc_device().lower() == "my computer", "Nick name is not matching"

    @pytest.mark.regression
    def test_02_verify_device_model_name_on_device_details_page_C65215540(self):
        self.devices_details_pc_mfe.verify_pc_device_name_show_up(raise_e=True)
        model_name = self.fc.get_windows_system_module_name()
        assert self.devices_details_pc_mfe.verify_device_details_device_name() == model_name, "System model name is not matching"

    @pytest.mark.regression
    @pytest.mark.ota
    def test_03_verify_device_list_page_C65209940(self):
        self.devices_details_pc_mfe.verify_pc_device_name_show_up()
        assert self.devices_details_pc_mfe.verify_back_devices_button_on_pc_devices_page_show_up()
        self.devices_details_pc_mfe.click_back_devices_button()
        assert self.devicesMFE.verify_device_card_show_up(),"Device card is not displayed"

    @pytest.mark.regression
    def test_04_verify_more_information_button_under_product_information_C65209941(self):
        self.devices_details_pc_mfe.verify_pc_device_name_show_up()
        assert self.devices_details_pc_mfe.verify_product_information_title_show_up(), "Product Information title is not displayed"
        assert self.devices_details_pc_mfe.verify_more_information_button_show(), "More Information button is not displayed"
        self.devices_details_pc_mfe.click_more_information_button()
        assert self.devices_details_pc_mfe.verify_general_specifications_title_show(), "General Specifications title is not displayed"
        self.devices_details_pc_mfe.verify_more_information_panel()

    @pytest.mark.regression
    def test_05_verify_whether_get_help_card_is_present_in_ddp_C65209945(self):
        self.devices_details_pc_mfe.verify_pc_device_name_show_up()
        logging.info("verifying Get Help card Module in Device Details Page")
        assert self.devices_details_pc_mfe.verify_get_help_module_show_up(), "Get Help module is not displayed"
        assert self.devices_details_pc_mfe.verify_start_virtual_assistant_button_show_up(), "Start Virtual Assistant button is not displayed"
        assert self.devices_details_pc_mfe.verify_view_manual_and_guides_link_show_up(), "View Manual and Guides link is not displayed"
        assert self.devices_details_pc_mfe.verify_find_a_repair_center_link_show_up(), "Find a Repair Center link is not displayed"
        assert self.devices_details_pc_mfe.verify_start_a_repair_order_link_show_up(), "Start a Repair Order link is not displayed"
        assert self.devices_details_pc_mfe.verify_get_more_help_on_our_website_link(), "Get More Help on Our Website link is not displayed"
        assert self.devices_details_pc_mfe.verify_contact_us_button_show_up(), "Contact Us button is not displayed"

    @pytest.mark.regression
    def test_06_verify_contact_us_under_get_help_module_C65209946(self):
        self.devices_details_pc_mfe.verify_pc_device_name_show_up()
        assert self.devices_details_pc_mfe.verify_get_help_module_show_up(), "Get Help module is not displayed"
        self.devices_details_pc_mfe.click_contact_us_button()
        self.devices_details_pc_mfe.verify_contact_us_panel()
        self.devices_details_pc_mfe.click_back_devices_button()
        assert self.devices_details_pc_mfe.verify_get_help_module_show_up(), "Get Help module is not displayed"
        assert self.devices_details_pc_mfe.verify_start_virtual_assistant_button_show_up()
        self.devices_details_pc_mfe.click_start_virtual_assistant_button()
        assert self.fc.fd["virtual_assistant"].verify_virtual_assistant_side_panel() ,"Virtual Assistant side panel is not displayed"

    @pytest.mark.regression
    def test_07_verify_all_modules_on_device_details_page_C65209948(self):
        self.devices_details_pc_mfe.verify_pc_device_name_show_up()
        assert self.devices_details_pc_mfe.verify_campaign_ads_show_up(), " Campaign Ads is not displayed"
        assert self.devices_details_pc_mfe.verify_get_help_module_show_up()," Get Help module is not displayed"
        assert self.devices_details_pc_mfe.verfiy_product_information_header_show(), " Product Information header is not displayed"

    @pytest.mark.regression
    def test_08_verify_product_information_on_device_details_page_C65209949(self):
        self.devices_details_pc_mfe.verify_pc_device_name_show_up(raise_e=True)
        assert self.devices_details_pc_mfe.verfiy_product_information_header_show(), "Product Information header is not displayed"
        assert self.devices_details_pc_mfe.verfiy_product_number_show(), "Product number is not displayed"
        product_number = self.device_card.get_copyproduct_number_text()
        logging.info(f"product number of the machine displayed on device details page is: '{product_number}'")
        assert self.devices_details_pc_mfe.verfiy_warranty_status_show(), "Warranty status is not displayed"
        assert self.devices_details_pc_mfe.verfiy_serial_number_show(), "Serial number is not displayed"
        assert self.devices_details_pc_mfe.verify_more_information_button_show(), "More Information button is not displayed"

    @pytest.mark.regression
    def test_09_verify_buttons_in_troubleshooting_and_fixes_C65730391(self):
        self.devices_details_pc_mfe.verify_pc_device_name_show_up(raise_e=True)
        self.devices_details_pc_mfe.verify_optimize_performance_button_show_up()
        self.devices_details_pc_mfe.verify_check_for_audio_issues_button_show_up()
        self.devices_details_pc_mfe.verify_run_system_tests_button_show_up()
        self.devices_details_pc_mfe.verify_run_hardware_tests_button_show_up()
        assert self.devices_details_pc_mfe.click_optimize_performance_button()
        self.devices_details_pc_mfe.close_optimize_performance_popup()
        assert self.devices_details_pc_mfe.click_check_for_audio_issues_button()
        self.devices_details_pc_mfe.close_check_for_audio_issues_popup()
        assert self.devices_details_pc_mfe.click_run_system_tests_button()
        self.devices_details_pc_mfe.close_run_system_tests_popup()
        assert self.devices_details_pc_mfe.click_run_hardware_tests_button()
        self.devices_details_pc_mfe.close_run_hardware_tests_popup()