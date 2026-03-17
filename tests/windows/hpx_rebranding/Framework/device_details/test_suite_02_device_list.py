import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_02_Device_List(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.css = request.cls.fc.fd["css"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        yield
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.uninstall_app()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_03_image_on_the_device_list_C53303930(self):
        device_name = self.fc.get_windows_system_name()
        logging.info(f"Device Serial Number: '{device_name}'")
        self.device_card.click_pc_devices_back_button()
        assert self.devicesMFE.verify_device_card_show_up(), "Devices card is not present"
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button invisible"
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon invisible"
        self.devicesMFE.click_device_card()
        assert self.device_card.verify_device_name_pc(), "pc device name invisible"
        self.driver.swipe("product_information",direction="down")
        assert self.device_card.verify_product_information(), "product information invisible"
        assert self.device_card.verify_warrenty_status(), "warranty status invisible"
        serial_number=self.device_card.get_copyserial_number_text()
        logging.info(f"Device Serial Number: '{serial_number}'")
        res=self.device_card.get_copyproduct_number_text()
        logging.info(f"Product Number: '{res}'") 
