import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.warning_simulator_ledm import WarningSimulatorLEDM

pytest.app_info = "Smart"

class Test_Suite_09_Cartridge_VeryLow_Laser(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.skyreach
    def test_01_cartridge_verylow_laser(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66085,type="warning")
        success = WarningSimulatorLEDM.cartridge_verylow(self.error_manager, color="k")
        assert success, "Failed to set cartridge very low error"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_get_more_help_btn()
        assert self.supplies_status.verify_get_supplies_btn()
