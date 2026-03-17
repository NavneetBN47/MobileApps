import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.error_simulator_ledm import ErrorSimulatorLEDM

pytest.app_info = "Smart"

class Test_Suite_02_Incompatible_Cartridge(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.malbec_trad
    @pytest.mark.muscatel
    @pytest.mark.manhattan_yeti
    @pytest.mark.edwin
    @pytest.mark.weber_base
    @pytest.mark.tesla
    @pytest.mark.poseidon_wl_flex
    @pytest.mark.kronos_ik_tank_flex
    @pytest.mark.ampere_xl
    @pytest.mark.spark
    @pytest.mark.limtane_mfp
    @pytest.mark.limtane_sfp
    @pytest.mark.shaolin
    @pytest.mark.verona
    @pytest.mark.palermo_fast
    def test_01_validate_incompatible_ink_cartridge_65543(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65543, type="error")
        success = ErrorSimulatorLEDM.incompatible_ink_cartridge_65543(self.error_manager, color="k")
        assert success, "Failed to set incompatible_ink_cartridge_65543 error"
        # printer details page verification
        assert self.supplies_status.verify_error_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_error_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_error_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_get_more_help_btn()
        assert self.supplies_status.verify_get_supplies_btn()

    @pytest.mark.muscatel
    @pytest.mark.taccola_base_yeti
    def test_02_validate_incompatible_cartridges_65676(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65676, type="error")
        success = ErrorSimulatorLEDM.incompatible_cartridges_65676(self.error_manager, color="y")
        assert success, "Failed to set incompatible_cartridges_65676 error"
        # printer details page verification
        assert self.supplies_status.verify_error_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_error_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("YELLOW")
        self.supplies_status.click_error_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_get_more_help_btn()

    @pytest.mark.muscatel
    @pytest.mark.taccola_base_yeti
    def test_03_validate_regional_cartridges_65676(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65676, type="error")
        success = ErrorSimulatorLEDM.regional_cartridges_65676(self.error_manager, color="y")
        assert success, "Failed to set regional_cartridges_65676 error"
        # printer details page verification
        assert self.supplies_status.verify_error_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_error_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("YELLOW")
        self.supplies_status.click_error_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_get_more_help_btn()
