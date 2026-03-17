import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_01_HPX_Close_Device_List(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.css = request.cls.fc.fd["css"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.feedback = request.cls.fc.fd["feedback"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        yield
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.uninstall_app()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_01_verify_hpx_app_launch_C44414919_C53303959(self):
        device_name = self.fc.get_windows_system_name()
        logging.info(f"Device Serial Number: '{device_name}'")
        assert self.devicesMFE.verify_profile_icon_show_up(), "profile icon invisible"
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button invisible"
        assert self.device_card.verify_bell_icon_present(), "bell icon invisible"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_02_verify_hpx_app_close_C44415042_C53303963(self):
        device_name = self.fc.get_windows_system_name()
        logging.info(f"Device Serial Number: '{device_name}'")
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button invisible"
        assert self.device_card.verify_bell_icon_present(), "bell icon invisible"
        self.profile.click_close_hpx_btn()
        logging.info(f"Device Serial Number: '{self.fc.get_windows_serial_number()}'")
        logging.info(f"Device Serial Number: '{self.fc.get_machine_type()}'")
        assert self.fc.is_app_open() is False, "HPX app did not close on clicking top X button"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_03_verify_hpx_app_close_on_selecting_alt_f4_C45384933_C53303964(self):
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button invisible"
        assert self.device_card.verify_bell_icon_present(), "bell icon invisible"
        self.devicesMFE.click_profile_button()
        self.profile.click_feedback_btn()
        self.feedback.terminate_hp_app_with_alt_f4()
        logging.info(f"Device Serial Number: '{self.fc.get_windows_serial_number()}'")
        logging.info(f"Device Serial Number: '{self.fc.get_machine_type()}'")
        assert self.fc.is_app_open() is False, "HPX app did not close on pressing Alt+F4"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_04_verify_device_details_page_C44415037_C53303962(self):
        device_name = self.fc.get_windows_system_name()
        logging.info(f"Device Serial Number: '{device_name}'")
        assert self.devicesMFE.verify_profile_icon_show_up(), "profile icon invisible"
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button invisible"
        assert self.device_card.verify_bell_icon_present(), "bell icon invisible"
        self.driver.swipe(distance=9, direction="down")
        assert self.device_card.verify_product_information(), "product information invisible"
        assert self.device_card.verify_warrenty_status(), "warranty status invisible"
        product_number = self.device_card.get_copyproduct_number_text()
        logging.info(f"Product Number: '{product_number}'")
        serial_num=self.device_card.get_copyserial_number_text()
        logging.info(f"Device Serial Number: '{serial_num}'")
        assert self.device_card.verify_warrenty_status(), "warranty status invisible"

    @pytest.mark.smoke
    @pytest.mark.ota
    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    def test_05_verify_top_app_bar_icons_C53303960(self):
        assert self.devices_details_pc_mfe.verify_back_devices_button_on_pc_devices_page_show_up(), "Device details page not loaded"
        self.device_card.click_pc_devices_back_button()
        assert self.device_card.verify_homepage_plus_button(), "add device button invisible"
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon invisible"
        assert self.devicesMFE.verify_profile_icon_show_up(), "profile icon invisible"
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button invisible"
        assert self.devicesMFE.verify_device_card_show_up(), "device card invisible"
