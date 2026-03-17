import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.information_simulator_ledm import InformationSimulatorLEDM

pytest.app_info = "Smart"

class Test_Suite_01_Single_Cartridge_Mode(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)


    @pytest.mark.shaolin
    @pytest.mark.verona
    def test_01_validate_single_cartridge_mode_65553(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65553, type="info")
        success = InformationSimulatorLEDM.single_cartridge_mode_65553(self.error_manager, color="k")
        assert success, "Failed to set single cartridge mode error"
        # printer details page verification
        assert self.supplies_status.verify_info_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_info_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_info_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify primary and secondary buttons
        assert self.supplies_status.verify_primary_ok_button()
        assert self.supplies_status.verify_get_more_help_btn()
        assert self.supplies_status.verify_get_supplies_btn()

    def test_02_validate_single_cartridge_mode_hybrid_inksub_65771(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65771, type="info")
        success = InformationSimulatorLEDM.single_cartridge_mode_hybrid_inksub_65771(self.error_manager, color="k")
        assert success, "Failed to set single cartridge mode hybrid ink sub error"
        # printer details page verification
        assert self.supplies_status.verify_info_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_info_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_info_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify primary and secondary buttons
        assert self.supplies_status.verify_primary_ok_button()
        assert self.supplies_status.verify_get_more_help_btn()
        assert self.supplies_status.verify_get_supplies_btn()
