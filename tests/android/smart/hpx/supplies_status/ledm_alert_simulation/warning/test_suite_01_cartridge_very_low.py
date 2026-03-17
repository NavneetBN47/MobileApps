import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.warning_simulator_ledm import WarningSimulatorLEDM

pytest.app_info = "Smart"

class Test_Suite_01_Cartridge_Very_Low(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.shaolin
    @pytest.mark.verona
    def test_01_validate_catridge_very_low_65546(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65546, type="warning")
        success = WarningSimulatorLEDM.cartridge_very_low_65546(self.error_manager, color="k")
        assert success, "Failed to set cartridge very low error"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() # alert_icon should be passed to verify against expected icon
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_primary_ok_button()
        assert self.supplies_status.verify_get_more_help_btn()
        assert self.supplies_status.verify_get_supplies_btn()

    def test_02_validate_cartridge_very_low_65764(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65764,type="warning")
        success = WarningSimulatorLEDM.cartridge_very_low_65764(self.error_manager, color="y")
        assert success, "Failed to set cartridge very low error"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("YELLOW")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_primary_ok_button()
        assert self.supplies_status.verify_get_more_help_btn()


    def test_03_validate_cartridge_very_low_65776(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65776,type="warning")
        success = WarningSimulatorLEDM.cartridge_very_low_inksup_65776(self.error_manager, color="k")
        assert success, "Failed to set cartridge very low error"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("YELLOW")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_primary_ok_button()
        assert self.supplies_status.verify_get_more_help_btn()
        

    def test_04_validate_cartridge_very_low_66241(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66241,type="warning")
        success = WarningSimulatorLEDM.cartridge_very_low_66241(self.error_manager, color="k")
        assert success, "Failed to set cartridge very low error"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("YELLOW")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_primary_ok_button()
        assert self.supplies_status.verify_get_more_help_btn()
        assert self.supplies_status.verify_get_supplies_btn()


    @pytest.mark.shaolin
    @pytest.mark.verona
    def test_05_validate_cartridge_refilled_65594(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65594,type="warning")
        success = WarningSimulatorLEDM.cartridge_refilled_65594(self.error_manager, color="k")
        assert success, "Failed to set cartridge refilled error"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("YELLOW")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_secondary_ok_button()
        assert self.supplies_status.verify_get_supplies_btn()


    def test_06_cartridge_very_low1_65764(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65764,type="warning")
        success = WarningSimulatorLEDM.cartridge_very_low1_65764(self.error_manager, color="k")
        assert success, "Failed to set cartridge very low error"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("YELLOW")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_primary_ok_button()
        assert self.supplies_status.verify_get_more_help_btn()


    def test_07_cartridge_very_low_65672(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65672,type="warning")
        success = WarningSimulatorLEDM.cartridge_very_low_65672(self.error_manager, color="y")
        assert success, "Failed to set cartridge very low error"
        # printer details page verification
        assert self.supplies_status.verify_warning_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("YELLOW")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify secondary buttons
        assert self.supplies_status.verify_primary_ok_button()
        assert self.supplies_status.verify_get_more_help_btn()
        assert self.supplies_status.verify_get_supplies_btn()
