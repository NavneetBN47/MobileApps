import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.ledm_alert_simulation.information_simulator_ledm import InformationSimulatorLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM
from MobileApps.libs.one_simulator.printer_simulation import delete_simulator_printer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_09_Nonhp_Supply_Printing(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        request.cls.driver = request.session.driver
        request.cls.fc = request.session.fc
        cls.supplies_status = request.cls.fc.fd["supplies_status"]
        cls.path = request.config.getoption("--local-build")
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)


    def test_01_nonhp_supply_detected_printing_65559(self):
        info_title, info_img, info_detailed_body = self.fc.read_supplies_status_json_files(ioref=65559,type="info")
        success = InformationSimulatorLEDM.nonhp_supply_detected_printing_65559(self.error_manager, color="y")
        assert success, "Failed to set nonhp supply detected printing error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(info_title, info_img, type="info")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_info_icon_in_pdp()
        assert self.supplies_status.verify_info_alert_title_in_pdp(info_title)
        self.supplies_status.click_info_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('y')
        assert self.supplies_status.verify_alert_title_after_clicked() == info_title, f"Alert Title text: '{info_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(info_detailed_body), f"Alert Body text: '{info_title}' is incorrect/mismatching"
        assert self.supplies_status.verify_ok_btn()
        assert self.supplies_status.verify_get_supplies_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    def test_02_nonhp_supply_detected_printing_66092(self):
        info_title, info_img, info_detailed_body = self.fc.read_supplies_status_json_files(ioref=66092,type="info")
        success = InformationSimulatorLEDM.nonhp_supply_detected_printing_66092(self.error_manager, color="y")
        assert success, "Failed to set nonhp supply detected printing error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(info_title, info_img, type="info")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_info_icon_in_pdp()
        assert self.supplies_status.verify_info_alert_title_in_pdp(info_title)
        self.supplies_status.click_info_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('y')
        assert self.supplies_status.verify_alert_title_after_clicked() == info_title, f"Alert Title text: '{info_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(info_detailed_body), f"Alert Body text: '{info_title}' is incorrect/mismatching"
        assert self.supplies_status.verify_ok_btn()
        assert self.supplies_status.verify_get_supplies_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()
