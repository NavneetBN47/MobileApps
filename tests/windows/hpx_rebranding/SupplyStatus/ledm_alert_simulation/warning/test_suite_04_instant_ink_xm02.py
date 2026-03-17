import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.warning_simulator_ledm import WarningSimulatorLEDM
from MobileApps.libs.one_simulator.printer_simulation import delete_simulator_printer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_04_Instant_Ink_XMO2(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        request.cls.driver = request.session.driver
        request.cls.fc = request.session.fc
        cls.supplies_status = request.cls.fc.fd["supplies_status"]
        cls.path = request.config.getoption("--local-build")
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)


    def test_01_validate_instantink_xmos2_trialcartridge_vloi_65848(self):
        warning_title, warning_img, warning_detailed_info = self.fc.read_supplies_status_json_files(ioref=65848,type="warning")
        success = WarningSimulatorLEDM.instantink_xmos2_trialcartridge_vloi_65848(self.error_manager, color="y")
        assert success, "Failed to set upgradable supply error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_warning_icon_in_pdp()
        assert self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('y')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, f"Alert Title text: '{warning_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_info), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_ok_btn()
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()
