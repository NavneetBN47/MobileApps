import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.ledm_alert_simulation.information_simulator_ledm import InformationSimulatorLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM

pytest.app_info = "Smart"

class Test_Suite_10_Setup_Cartridge(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)


    @pytest.mark.verona
    @pytest.mark.palermo_fast
    def test_01_setup_cartridge_for_pha_65591_65851(self):
        # error alert for PHA 65591 and 65851
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65591,type="error")
        success = InformationSimulatorLEDM.setup_cartridge_for_pha_65591_65851(self.error_manager, color="y")
        assert success, "Failed to set up cartridge for PHA error"
        # printer details page verification
        assert self.supplies_status.verify_info_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_info_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("YELLOW")
        self.supplies_status.click_info_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify primary buttons
        assert self.supplies_status.verify_primary_ok_button()
