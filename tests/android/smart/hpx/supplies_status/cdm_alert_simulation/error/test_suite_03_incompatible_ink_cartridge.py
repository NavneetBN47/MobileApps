import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM
from MobileApps.libs.one_simulator.cdm_alert_simulation.error_simulator_cdm import ErrorSimulatorCDM

pytest.app_info = "Smart"


class Test_Suite_03_Incompatible_Ink_Cartridge(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
        cls.error_manager = SimulatorErrorManagerCDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_pdl
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.beam
    @pytest.mark.trillium_plus
    def test_01_validate_incompatible_ink_cartridge_65543(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65543, type="error")
        success = ErrorSimulatorCDM.incompatible_ink_cartridge_65543(self.error_manager, color="k")
        assert success, "Failed to set incompatible ink cartridge error"
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

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_pdl
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.beam
    @pytest.mark.trillium_plus
    def test_02_incompatible_cartridge_region_65543(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65543, type="error")
        success = ErrorSimulatorCDM.incompatible_cartridge_region_65543(self.error_manager, color="k")
        assert success, "Failed to set incompatible cartridge region error"
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

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_03_incompatible_hp_instant_ink_66175(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorCDM.incompatible_hp_instant_ink_66175(self.error_manager, color="k")
        assert success, "Failed to set incompatible hp instant ink error"
        # printer details page verification
        assert self.supplies_status.verify_error_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_error_alert_icon_in_pdp_screen(alert_icon)
        self.supplies_status.click_error_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_get_more_help_btn()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_04_incompatible_cartridge_region_66175(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorCDM.incompatible_cartridge_region_66175(self.error_manager, color="k")
        assert success, "Failed to set incompatible cartridge region error"
        # printer details page verification
        assert self.supplies_status.verify_error_alert_title_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_error_alert_icon_in_pdp_screen(alert_icon)
        self.supplies_status.click_error_alert_in_pdp_screen()
        # printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen() 
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_get_more_help_btn()

    @pytest.mark.jupiter
    def test_05_incompatible_cartridge_65543(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65543, type="error")
        success = ErrorSimulatorCDM.incompatible_cartridge_65543(self.error_manager,color='k')
        assert success, "Failed to set incompatible cartridge error"
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

    @pytest.mark.jupiter
    def test_06_incompatible_cartridge_65939(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65939, type="error")
        success = ErrorSimulatorCDM.incompatible_cartridge_65939(self.error_manager,color='k')
        assert success, "Failed to set incompatible cartridge error"
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