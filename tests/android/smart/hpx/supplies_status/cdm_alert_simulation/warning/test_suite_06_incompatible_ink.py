import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM
from MobileApps.libs.one_simulator.cdm_alert_simulation.warning_simulator_cdm import WarningSimulatorCDM

pytest.app_info = "Smart"


class Test_Suite_06_Incompatable_Ink(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
        cls.error_manager = SimulatorErrorManagerCDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.moreto_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_01_unsubscribedstate_incompatible_ink_66241(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66241, type="warning")
        success = WarningSimulatorCDM.unsubscribedstate_incompatible_ink_66241(self.error_manager, color="k")
        assert success, "Failed to set insubscribed incompatible ink error"
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

    @pytest.mark.tassel_base_yeti
    def test_02_vloi_supply_66241(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66241, type="warning")
        success = WarningSimulatorCDM.vloi_supply_66241(self.error_manager, color="k")
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
