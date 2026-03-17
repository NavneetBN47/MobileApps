import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.ledm_alert_simulation.information_simulator_ledm import InformationSimulatorLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM

pytest.app_info = "Smart"

class Test_Suite_07_HP_Cartridges_Installed(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)


    def test_01_validate_new_hp_cartridges_installed_66265(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66265, type="info")
        success = InformationSimulatorLEDM.new_hp_cartridges_installed_66265(self.error_manager, color="y")
        assert success, "Failed to set new_hp_cartridges_installed_66265 error"
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

    def test_02_validate_hp_cartridges_installed_66264(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66264, type="info")
        success = InformationSimulatorLEDM.hp_cartridges_installed_66264(self.error_manager, color="y")
        assert success, "Failed to set hp_cartridges_installed_66264 error"
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

    def test_03_validate_cartridges_low_66242(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66242, type="info")
        success = InformationSimulatorLEDM.cartridges_low_66242(self.error_manager, color="y")
        assert success, "Failed to set cartridges_low_66242 error"
        # printer details page verification
        assert self.supplies_status.verify_info_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_info_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("YELLOW")
        self.supplies_status.click_info_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify primary and secondary buttons
        assert self.supplies_status.verify_primary_ok_button()
        assert self.supplies_status.verify_get_more_help_btn()
        assert self.supplies_status.verify_get_supplies_btn()

    def test_04_validate_genuine_hp_inklevelzero_65684(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65684, type="info")
        success = InformationSimulatorLEDM.genuine_hp_inklevelzero_65684(self.error_manager, color="k")
        assert success, "Failed to set genuine_hp_inklevelzero_65684 error"
        # printer details page verification
        assert self.supplies_status.verify_info_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_info_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_info_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # verify primary buttons
        assert self.supplies_status.verify_primary_ok_button()
