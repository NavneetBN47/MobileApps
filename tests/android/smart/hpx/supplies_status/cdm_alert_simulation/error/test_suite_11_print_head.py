import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM
from MobileApps.libs.one_simulator.cdm_alert_simulation.error_simulator_cdm import ErrorSimulatorCDM

pytest.app_info = "Smart"


class Test_Suite_11_Print_Head(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
        cls.error_manager = SimulatorErrorManagerCDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.lebi_wireless_flex
    def test_01_printheadproblem_66207(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66207, type="error")
        success = ErrorSimulatorCDM.printheadproblem_66207(self.error_manager,color='k')
        assert success, "Failed to set printhead problem error"
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

    @pytest.mark.lebi_wireless_flex
    def test_02_incompatible_printhead_66213(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66213, type="error")
        success = ErrorSimulatorCDM.incompatible_printhead_66213(self.error_manager,color='k')
        assert success, "Failed to set incompatible printhead error"
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

    @pytest.mark.lebi_wireless_flex
    def test_03_print_head_problem_66211(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66211, type="error")
        success = ErrorSimulatorCDM.print_head_problem_66211(self.error_manager,color='k')
        assert success, "Failed to set printhead problem error"
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

    @pytest.mark.lebi_wireless_flex
    def test_04_hp_protected_printheads_installed_66230(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66230, type="error")
        success = ErrorSimulatorCDM.hp_protected_printheads_installed_66230(self.error_manager,color='k')
        assert success, "Failed to set HP protected printheads installed error"
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

    @pytest.mark.jupiter
    def test_05_missing_printheads_66128(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66128, type="error")
        success = ErrorSimulatorCDM.missing_printheads_66128(self.error_manager,color='k')
        assert success, "Failed to set missing printheads error"
        # printer details page verification
        assert self.supplies_status.verify_error_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_error_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_error_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # need to verify primary and secondary buttons if any in future

    @pytest.mark.jupiter
    def test_06_printhead_replacement_incomplete_66130(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66130, type="error")
        success = ErrorSimulatorCDM.printhead_replacement_incomplete_66130(self.error_manager,color='k')
        assert success, "Failed to set printhead replacement incomplete error"
        # printer details page verification
        assert self.supplies_status.verify_error_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_error_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_error_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # need to verify primary and secondary buttons if any in future

    @pytest.mark.jupiter
    def test_07_printhead_failure_66131(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66131, type="error")
        success = ErrorSimulatorCDM.printhead_failure_66131(self.error_manager,color='k')
        assert success, "Failed to set printhead failure error"
        # printer details page verification
        assert self.supplies_status.verify_error_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_error_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_error_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # need to verify primary and secondary buttons if any in future

    @pytest.mark.pixiu
    def test_08_printhead_failure_66442(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66442, type="error")
        success = ErrorSimulatorCDM.printhead_failure_66442(self.error_manager,color='k')
        assert success, "Failed to set printhead failure error"
        # printer details page verification
        assert self.supplies_status.verify_error_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_error_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_error_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # need to verify primary and secondary buttons if any in future
