import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM
from MobileApps.libs.one_simulator.cdm_alert_simulation.warning_simulator_cdm import WarningSimulatorCDM

pytest.app_info = "Smart"

class Test_Suite_02_Cartridge_Very_Low(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
        cls.error_manager = SimulatorErrorManagerCDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.moreto_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_01_validate_cartridge_very_low_66241(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66241, type="warning")
        success = WarningSimulatorCDM.cartridge_very_low_66241(self.error_manager, color="k")
        assert success, "Failed to set anti-theft enabled error"
        # Printer details page verification
        assert self.supplies_status.verify_warning_alert_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # Printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_primary_ok_button()
        assert self.supplies_status.verify_get_supplies_btn()
        assert self.supplies_status.verify_get_more_help_btn()

    def test_02_validate_cartridges_very_low_66710(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66710, type="warning")
        success = WarningSimulatorCDM.vloi_supply_66710(self.error_manager, color="k")
        assert success, "Failed to set cartridges very low error"
        # Printer details page verification
        assert self.supplies_status.verify_warning_alert_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # Printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_primary_ok_button()
        assert self.supplies_status.verify_get_supplies_btn()
        assert self.supplies_status.verify_get_more_help_btn()

    @pytest.mark.victoria_base_yeti
    def test_03_validate_cartridge_very_low_66712(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66712, type="warning")
        success = WarningSimulatorCDM.vloi_supply_66712(self.error_manager, color="k")
        assert success, "Failed to set cartridge very low error"
        # Printer details page verification
        assert self.supplies_status.verify_warning_alert_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # Printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_primary_ok_button()
        assert self.supplies_status.verify_get_supplies_btn()
        assert self.supplies_status.verify_get_more_help_btn()

    def test_04_vloi_supply_66710(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66710, type="warning")
        success = WarningSimulatorCDM.vloi_supply_66710(self.error_manager, color="k")
        assert success, "Failed to set vloi supply error"
        # Printer details page verification
        assert self.supplies_status.verify_warning_alert_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # Printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_primary_ok_button()
        assert self.supplies_status.verify_get_supplies_btn()
        assert self.supplies_status.verify_get_more_help_btn()

    @pytest.mark.victoria_base_yeti
    def test_05_vloi_supply_66712(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66712, type="warning")
        success = WarningSimulatorCDM.vloi_supply_66712(self.error_manager, color="k")
        assert success, "Failed to set vloi supply error"
        # Printer details page verification
        assert self.supplies_status.verify_warning_alert_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # Printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_primary_ok_button()
        assert self.supplies_status.verify_get_supplies_btn()
        assert self.supplies_status.verify_get_more_help_btn()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_06_vloi_supply_66241(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66241, type="warning")
        success = WarningSimulatorCDM.vloi_supply_66241(self.error_manager, color="k")
        assert success, "Failed to set vloi supply error"
        # Printer details page verification
        assert self.supplies_status.verify_warning_alert_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # Printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_primary_ok_button()
        assert self.supplies_status.verify_get_supplies_btn()
        assert self.supplies_status.verify_get_more_help_btn()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.trillium_plus
    def test_07_cartridge_very_low_flow_65546(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65546, type="warning")
        success = WarningSimulatorCDM.cartridge_very_low_flow_65546(self.error_manager, color="k")
        assert success, "Failed to set anti-theft enabled error"
        # Printer details page verification
        assert self.supplies_status.verify_warning_alert_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # Printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_primary_ok_button()
        assert self.supplies_status.verify_get_supplies_btn()
        assert self.supplies_status.verify_get_more_help_btn()

    @pytest.mark.selene
    def test_08_cartridge_verylow_continue_66085(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66085, type="warning")
        success = WarningSimulatorCDM.cartridge_verylow_continue_66085(self.error_manager, color="k")
        assert success, "Failed to set cartridge very low continue error"
        # Printer details page verification
        assert self.supplies_status.verify_warning_alert_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # Printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_primary_ok_button()
        assert self.supplies_status.verify_get_supplies_btn()
        assert self.supplies_status.verify_get_more_help_btn()
