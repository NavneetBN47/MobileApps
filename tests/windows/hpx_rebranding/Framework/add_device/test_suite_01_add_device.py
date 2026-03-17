import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_01_Add_Device(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile= request.cls.fc.fd["profile"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.add_device= request.cls.fc.fd["add_device"]

    @pytest.mark.regression
    def test_01_verify_add_device_button_clickable_and_opens_sidebar_page_C55687256(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.profile.verify_add_device_button(), "add device button is not found"
        self.profile.click_add_device_button()
        assert self.add_device.verify_add_device_page(), "add device page is not found"

    @pytest.mark.regression
    def test_02_verify_navigation_of_need_help_finding_serial_number_link_C61716550(self):
        self.devices_details_pc_mfe.verify_pc_device_name_show_up()
        self.profile.verify_add_device_button()
        self.profile.click_add_device_button()
        assert self.add_device.verify_add_device_page(), "add device page is not found"
        assert self.add_device.verify_search_by_serial_number_btn(), "search by serial number button not found"
        self.add_device.click_search_by_serial_number_btn()
        assert self.add_device.verify_serial_number_textbox(), "text input field “Serial Number” not visible"
        assert self.add_device.verify_need_help_finding_your_serial_number_link(), "need help finding your serial number link not found"
        self.add_device.click_need_help_finding_your_serial_number_link()
        self.devicesMFE.verify_browser_webview_pane()

    @pytest.mark.regression
    def test_03_verify_the_back_button_for_the_add_device_C61716558(self):
        self.devices_details_pc_mfe.verify_pc_device_name_show_up()
        self.profile.verify_add_device_button()
        self.profile.click_add_device_button()
        assert self.add_device.verify_add_device_page(), "add device page is not found"
        assert self.add_device.verify_search_by_serial_number_btn(), "search by serial number button not found"
        self.add_device.click_search_by_serial_number_btn()
        assert self.add_device.verify_serial_number_textbox(), "text input field “Serial Number” not visible"
        assert self.add_device.verify_add_a_device_back_btn(), "Add a device back button not visible"
        self.add_device.click_add_a_device_back_btn()
        assert self.add_device.verify_add_device_page(), "add device page is not found"

    @pytest.mark.regression
    def test_04_verify_the_close_button_for_the_add_device_C61716559(self):
        self.devices_details_pc_mfe.verify_pc_device_name_show_up()
        self.profile.verify_add_device_button()
        self.profile.click_add_device_button()
        assert self.add_device.verify_add_device_page(), "add device page is not found"
        assert self.add_device.verify_close_button_on_add_device_page(), "Close button not present on add device page"
        self.add_device.click_close_button_on_add_device_page()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"

    @pytest.mark.regression
    def test_05_verify_entered_serial_number_is_accepted_and_displayed_correctly_C63813594(self):
        self.devices_details_pc_mfe.verify_pc_device_name_show_up()
        self.profile.verify_add_device_button()
        self.profile.click_add_device_button()
        assert self.add_device.verify_add_device_page(), "add device page is not found"
        assert self.add_device.verify_search_by_serial_number_btn(), "search by serial number button not found"
        self.add_device.click_search_by_serial_number_btn()
        assert self.add_device.verify_serial_number_textbox(), "text input field “Serial Number” not visible"
        self.add_device.input_enter_serial_number("8CC5281Y49")
        entered_value = self.add_device.get_entered_serial_number()
        assert entered_value == "8CC5281Y49", f"Serial number not displayed correctly, found: {entered_value}"

    @pytest.mark.regression
    def test_06_verify_the_content_in_add_a_printer_C63813978(self):
        self.devices_details_pc_mfe.verify_pc_device_name_show_up()
        self.profile.verify_add_device_button()
        self.profile.click_add_device_button()
        assert self.add_device.verify_add_device_page(), "add device page is not found"
        assert self.add_device.verify_add_printer_content(), "content in add a printer is not matching"

    @pytest.mark.regression
    def test_07_verify_the_content_in_missing_a_device_C63815104(self):
        self.devices_details_pc_mfe.verify_pc_device_name_show_up()
        self.profile.verify_add_device_button()
        self.profile.click_add_device_button()
        assert self.add_device.verify_add_device_page(), "add device page is not found"
        assert self.add_device.verify_missing_device_content(), "content in missing device is not matching"
