import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.ledm_alert_simulation.information_simulator_ledm import InformationSimulatorLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM

pytest.app_info = "Smart"

class Test_Suite_02_Used_Consumable(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.shaolin
    @pytest.mark.verona
    @pytest.mark.palermo_fast
    def test_01_validate_used_consumable_65554(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65554,type="info")
        success = InformationSimulatorLEDM.used_consumable_65554(self.error_manager, color="k")
        assert success, "Failed to set used consumable error"
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

    def test_02_validate_usedconsumable_inksub_65680(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65680,type="info")
        success = InformationSimulatorLEDM.used_consumable_inksub_65680(self.error_manager, color="k")
        assert success, "Failed to set used consumable inksub error"
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

    def test_03_validate_previously_used_consumable_instant_ink_sub_65680(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65680,type="info")
        success = InformationSimulatorLEDM.previously_used_consumable_instant_ink_sub_65680(self.error_manager, color="k")
        assert success, "Failed to set previously used consumable instant ink sub error"
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

    def test_04_validate_used_consumable_66216(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66216,type="info")
        success = InformationSimulatorLEDM.used_consumable_66216(self.error_manager, color="y")
        assert success, "Failed to set used consumable sms alert"
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
