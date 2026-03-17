import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.error_simulator_ledm import ErrorSimulatorLEDM

pytest.app_info = "Smart"

class Test_Suite_01_Cartridge_Missing(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.manhattan_yeti
    def test_01_validate_cartridge_missing_65690(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65690, type="error")
        success = ErrorSimulatorLEDM.cartridge_missing_65690(self.error_manager, color="y")
        assert success, "Failed to set cartridge_missing_65690 error"
        # printer details page verification
        assert self.supplies_status.verify_error_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_error_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("YELLOW")
        self.supplies_status.click_error_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # need to verify primary and secondary buttons if any in future


    @pytest.mark.poseidon_wl_flex
    @pytest.mark.kronos_ik_tank_flex
    @pytest.mark.infinity
    @pytest.mark.shaolin
    @pytest.mark.verona
    def test_02_validate_cartridge_missing_65537(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65537, type="error")
        success = ErrorSimulatorLEDM.cartridge_missing_65537(self.error_manager, color="k")
        assert success, "Failed to set cartridge_missing_65537 error"
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


    @pytest.mark.taccola_base_yeti
    @pytest.mark.narita_plus_yeti
    @pytest.mark.narita_base_yeti
    def test_03_missing_cartridge_hybrid_inksub_65769(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65769, type="error")
        success = ErrorSimulatorLEDM.missing_cartridge_hybrid_inksub_65769(self.error_manager, color="k")
        assert success, "Failed to set missing_cartridge_hybrid_inksub_65769 error"
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


    @pytest.mark.vasari_base_yeti
    @pytest.mark.novelli_plus_yeti
    def test_04_cartridges_missing_66262(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66262, type="error")
        success = ErrorSimulatorLEDM.cartridges_missing_66262(self.error_manager, color="y")
        assert success, "Failed to set cartridges_missing_66262 error"
        # printer details page verification
        assert self.supplies_status.verify_error_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_error_alert_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("YELLOW")
        self.supplies_status.click_error_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        # need to verify primary and secondary buttons if any in future


    @pytest.mark.taccola_base_yeti
    @pytest.mark.narita_plus_yeti
    @pytest.mark.narita_base_yeti
    def test_05_validate_missing_cartridge_instantinksub_65769(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65769, type="error")
        success = ErrorSimulatorLEDM.missing_cartridge_instantinksub_65769(self.error_manager, color="k")
        assert success, "Failed to set missing_cartridge_instantinksub_65769 error"
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


    @pytest.mark.poseidon_wl_flex
    @pytest.mark.kronos_ik_tank_flex
    @pytest.mark.infinity
    @pytest.mark.shaolin
    @pytest.mark.verona
    def test_06_validate_missing_cartridge_single_65537(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65537, type="error")
        success = ErrorSimulatorLEDM.cartridge_missing_single_65537(self.error_manager, color="k")
        assert success, "Failed to set cartridge_missing_single_65537 error"
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


    @pytest.mark.manhattan_yeti
    @pytest.mark.edwin
    @pytest.mark.weber_base
    @pytest.mark.tesla
    @pytest.mark.ampere_xl
    @pytest.mark.spark
    @pytest.mark.limtane_mfp
    @pytest.mark.limtane_sfp
    def test_07_validate_cartridge_missing_65589(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65589, type="error")
        success = ErrorSimulatorLEDM.cartridge_missing_65589(self.error_manager, color="y")
        assert success, "Failed to set cartridge_missing_65589 error"
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
        assert self.supplies_status.verify_get_supplies_btn()
