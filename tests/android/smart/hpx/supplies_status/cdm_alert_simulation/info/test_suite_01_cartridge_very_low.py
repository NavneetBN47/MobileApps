import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM
from MobileApps.libs.one_simulator.cdm_alert_simulation.information_simulator_cdm import InformationSimulatorCDM

pytest.app_info = "Smart"

class Test_Suite_01_Cartridge_Very_Low(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
        cls.error_manager = SimulatorErrorManagerCDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.moreto_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_01_validate_cartridges_very_low_66242(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66242, type="info")
        success = InformationSimulatorCDM.cartridges_low_66242(self.error_manager, color="k")
        assert success, "Failed to set cartridges very low info"
        assert self.supplies_status.verify_info_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_info_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_info_alert_in_pdp_screen()
        # printer status screen
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_primary_ok_button()
        assert self.supplies_status.verify_get_more_help_btn()
        assert self.supplies_status.verify_get_supplies_btn()

    def test_02_validate_cartridges_very_low_66711(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66711, type="info")
        success = InformationSimulatorCDM.loi_supply_66711(self.error_manager, color="k")
        assert success, "Failed to set cartridges very low info"
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
        assert self.supplies_status.verify_get_more_help_btn()
        assert self.supplies_status.verify_get_supplies_btn()

    @pytest.mark.victoria_base_yeti
    def test_03_validate_cartridge_very_low_66713(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66713, type="info")
        success = InformationSimulatorCDM.cartridges_low_66713(self.error_manager, color="k")
        assert success, "Failed to set cartridges very low info"
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
        assert self.supplies_status.verify_get_more_help_btn()
        assert self.supplies_status.verify_get_supplies_btn()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.trillium_plus
    def test_04_validate_cartridge_low_flow_65557(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65557, type="info")
        success = InformationSimulatorCDM.cartridge_low_flow_65557(self.error_manager, color="k")
        assert success, "Failed to set cartridge low flow info"
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
        assert self.supplies_status.verify_get_more_help_btn()
        assert self.supplies_status.verify_get_supplies_btn()
