import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.error_simulator_ledm import ErrorSimulatorLEDM

pytest.app_info = "Smart"

class Test_Suite_16_Error_State(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.ampere_xl
    def test_01_validate_printer_error_65541(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65541, type="error")
        success = ErrorSimulatorLEDM.printer_error_65541(self.error_manager)
        assert success, "Failed to set printer_error_65541 error"
        # printer details page verification
        assert self.supplies_status.verify_error_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_error_alert_icon_in_pdp_screen(alert_icon)
        self.supplies_status.click_error_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # need to verify primary and secondary buttons if any in future

    @pytest.mark.manhattan_yeti
    @pytest.mark.edwin
    @pytest.mark.weber_base
    @pytest.mark.tesla
    @pytest.mark.spark
    @pytest.mark.limntane_mfp
    @pytest.mark.limtane_sfp
    def test_02_validate_shaid_ooi_too_early_65800(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65800, type="error")
        success = ErrorSimulatorLEDM.shaid_ooi_too_early_65800(self.error_manager, color="y")
        assert success, "Failed to set shaid_ooi_too_early_65800 error"
        # printer details page verification
        assert self.supplies_status.verify_error_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_error_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("YELLOW")
        self.supplies_status.click_error_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_get_supplies_btn()