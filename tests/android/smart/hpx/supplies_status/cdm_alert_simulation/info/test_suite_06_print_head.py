import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM
from MobileApps.libs.one_simulator.cdm_alert_simulation.information_simulator_cdm import InformationSimulatorCDM

pytest.app_info = "Smart"

class Test_Suite_06_Print_Head(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
        cls.error_manager = SimulatorErrorManagerCDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.lebi_wireless_flex
    def test_01_used_printhead_installation_66216(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66216, type="info")
        success = InformationSimulatorCDM.used_printhead_installation_66216(self.error_manager,color="k")
        assert success, "Failed to set used printhead installation info"
        # Printer Details Page
        assert self.supplies_status.verify_info_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_info_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_info_alert_in_pdp_screen()
        # printer status screen
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_primary_ok_button()

    @pytest.mark.lebi_wireless_flex
    def test_02_new_printhead_installation_66222(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66222, type="info")
        success = InformationSimulatorCDM.new_printhead_installation_66222(self.error_manager,color="k")
        assert success, "Failed to set new printhead installation info"
        # Printer Details Page
        assert self.supplies_status.verify_info_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_info_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_info_alert_in_pdp_screen()
        # printer status screen
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_primary_ok_button()

    @pytest.mark.jupiter
    def test_03_ph_replacement_flow_66640(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66640, type="info")
        success = InformationSimulatorCDM.new_printhead_installation_66640(self.error_manager,color="k")
        assert success, "Failed to set ph replacement flow"
        # Printer Details Page
        assert self.supplies_status.verify_info_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_info_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_info_alert_in_pdp_screen()
        # printer status screen
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_primary_ok_button()
