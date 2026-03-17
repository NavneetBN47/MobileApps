import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.error_simulator_ledm import ErrorSimulatorLEDM

pytest.app_info = "Smart"

class Test_Suite_12_Pen(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.malbec_yeti
    @pytest.mark.manhattan_yeti
    @pytest.mark.vasari_base_yeti
    @pytest.mark.novelli_plus_yeti
    @pytest.mark.narita_plus_yeti
    @pytest.mark.narita_base_yeti
    def test_01_validate_oobe_hp_altered_supply_refilled_66175(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorLEDM.oobe_hp_altered_supply_refilled_66175(self.error_manager, color="k")
        assert success, "Failed to set oobe_hp_altered_supply_refilled_66175 error"
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

    @pytest.mark.malbec_yeti
    @pytest.mark.manhattan_yeti
    @pytest.mark.vasari_base_yeti
    @pytest.mark.novelli_plus_yeti
    @pytest.mark.narita_plus_yeti
    @pytest.mark.narita_base_yeti
    def test_02_oobe_faulty_supply_66175(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorLEDM.oobe_faulty_supply_66175(self.error_manager, color="k")
        assert success, "Failed to set oobe_faulty_supply_66175 error"
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

    @pytest.mark.malbec_yeti
    @pytest.mark.manhattan_yeti
    @pytest.mark.vasari_base_yeti
    @pytest.mark.novelli_plus_yeti
    @pytest.mark.narita_plus_yeti
    @pytest.mark.narita_base_yeti
    def test_03_trial_pen_66175(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorLEDM.trial_pen_66175(self.error_manager, color="k")
        assert success, "Failed to set trial_pen_66175 error"
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

    @pytest.mark.malbec_yeti
    @pytest.mark.manhattan_yeti
    @pytest.mark.vasari_base_yeti
    @pytest.mark.novelli_plus_yeti
    @pytest.mark.narita_plus_yeti
    @pytest.mark.narita_base_yeti
    def test_04_incompatible_pen_66175(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorLEDM.incompatible_pen_66175(self.error_manager, color="k")
        assert success, "Failed to set incompatible_pen_66175 error"
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

    @pytest.mark.malbec_yeti
    @pytest.mark.manhattan_yeti
    @pytest.mark.vasari_base_yeti
    @pytest.mark.novelli_plus_yeti
    @pytest.mark.narita_plus_yeti
    @pytest.mark.narita_base_yeti
    def test_05_non_hp_circuitry_66175(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorLEDM.non_hp_circuitry_66175(self.error_manager, color="k")
        assert success, "Failed to set non_hp_circuitry_66175 error"
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

    @pytest.mark.malbec_yeti
    @pytest.mark.manhattan_yeti
    @pytest.mark.vasari_base_yeti
    @pytest.mark.novelli_plus_yeti
    @pytest.mark.narita_plus_yeti
    @pytest.mark.narita_base_yeti
    def test_06_protected_cartridges_66175(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorLEDM.protected_cartridges_66175(self.error_manager, color="k")
        assert success, "Failed to set protected_cartridges_66175 error"
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