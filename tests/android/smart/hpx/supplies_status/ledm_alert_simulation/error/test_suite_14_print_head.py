import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.error_simulator_ledm import ErrorSimulatorLEDM

pytest.app_info = "Smart"

class Test_Suite_14_Print_Head(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.manhattan_yeti
    @pytest.mark.edwin
    @pytest.mark.weber_base
    @pytest.mark.tesla
    @pytest.mark.ampere_xl
    @pytest.mark.spark
    def test_01_validate_missing_printhead_65536(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65536, type="error")
        success = ErrorSimulatorLEDM.missing_printhead_65536(self.error_manager)
        assert success, "Failed to set missing_printhead_65536 error"
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
    @pytest.mark.ampere_xl
    @pytest.mark.spark
    def test_02_validate_incompatible_printhead_65536(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65536, type="error")
        success = ErrorSimulatorLEDM.incompatible_printhead_65536(self.error_manager)
        assert success, "Failed to set incompatible_printhead_65536 error"
        # printer details page verification
        assert self.supplies_status.verify_error_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_error_alert_icon_in_pdp_screen(alert_icon)
        self.supplies_status.click_error_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # need to verify primary and secondary buttons if any in future

    @pytest.mark.edwin
    @pytest.mark.weber_base
    @pytest.mark.ampere_xl
    @pytest.mark.spark
    def test_03_validate_failed_printhead_65536(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65536, type="error")
        success = ErrorSimulatorLEDM.failed_printhead_65536(self.error_manager)
        assert success, "Failed to set failed_printhead_65536 error"
        # printer details page verification
        assert self.supplies_status.verify_error_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_error_alert_icon_in_pdp_screen(alert_icon)
        self.supplies_status.click_error_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # need to verify primary and secondary buttons if any in future

    @pytest.mark.sayan_wireless_flex
    @pytest.mark.sayan_paas
    def test_04_validate_shared_select_address_error_66209(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66209, type="error")
        success = ErrorSimulatorLEDM.shared_select_address_error_66209(self.error_manager)
        assert success, "Failed to set shared_select_address_error_66209 error"
        # printer details page verification
        assert self.supplies_status.verify_error_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_error_alert_icon_in_pdp_screen(alert_icon)
        self.supplies_status.click_error_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_get_more_help_btn()

    @pytest.mark.sayan_wireless_flex
    @pytest.mark.sayan_paas
    def test_05_validate_hp_protected_printheads_installed_66230(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66230, type="error")
        success = ErrorSimulatorLEDM.hp_protected_printheads_installed_66230(self.error_manager,color='y')
        assert success, "Failed to set hp_protected_printheads_installed_66230 error"
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

    @pytest.mark.sayan_wireless_flex
    @pytest.mark.sayan_paas
    def test_06_validate_printhead_cartridge_missing_66207(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66207, type="error")
        success = ErrorSimulatorLEDM.printhead_cartridge_missing_66207(self.error_manager,color='y')
        assert success, "Failed to set printhead_cartridge_missing_66207 error"
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

    @pytest.mark.sayan_wireless_flex
    @pytest.mark.sayan_paas
    def test_07_validate_printhead_failure_66211(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66211, type="error")
        success = ErrorSimulatorLEDM.printhead_failure_66211(self.error_manager,color='y')
        assert success, "Failed to set printhead_failure_66211 error"
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

    @pytest.mark.sayan_wireless_flex
    @pytest.mark.sayan_paas
    def test_08_validate_incompatible_printhead_66213(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66213, type="error")
        success = ErrorSimulatorLEDM.incompatible_printhead_66213(self.error_manager,"y")
        assert success, "Failed to set incompatible_printhead_66213 error"
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
