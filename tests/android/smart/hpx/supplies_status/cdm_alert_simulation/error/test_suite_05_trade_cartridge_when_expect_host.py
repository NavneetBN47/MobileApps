import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM
from MobileApps.libs.one_simulator.cdm_alert_simulation.error_simulator_cdm import ErrorSimulatorCDM

pytest.app_info = "Smart"


class Test_Suite_05_Trade_Cartridge_When_Expect_Host(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
        cls.error_manager = SimulatorErrorManagerCDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    def test_01_validate_trade_cartridge_when_expect_host_65590(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65590, type="error")
        success = ErrorSimulatorCDM.trade_cartridge_when_expect_host_65590(self.error_manager, color="k")
        assert success, "Failed to set trade cartridge when expect host error"
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

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_pdl
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    def test_02_host_cartridge_when_expect_trade_65591(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65591, type="error")
        success = ErrorSimulatorCDM.host_cartridge_when_expect_trade_65591(self.error_manager, color="k")
        assert success, "Failed to set host cartridge when expect trade error"
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
        assert self.supplies_status.verify_get_supplies_btn()

    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.marconi_base_yeti
    def test_03_cartridge_expected_setup_verylow_65590(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65590, type="error")
        success = ErrorSimulatorCDM.cartridge_expected_setup_verylow_65590(self.error_manager, color="k")
        assert success, "Failed to set cartridge expected setup very low error"
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

    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    def test_04_cartridge_expected_setup_low_65590(self): 
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65590, type="error")
        success = ErrorSimulatorCDM.cartridge_expected_setup_low_65590(self.error_manager, color="k")
        assert success, "Failed to set cartridge expected setup low error"
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

    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    def test_05_cartridge_expected_setup_altered_supply_65590(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65590, type="error")
        success = ErrorSimulatorCDM.cartridge_expected_setup_altered_supply_65590(self.error_manager, color="k")
        assert success, "Failed to set cartridge expected setup altered supply error"
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
