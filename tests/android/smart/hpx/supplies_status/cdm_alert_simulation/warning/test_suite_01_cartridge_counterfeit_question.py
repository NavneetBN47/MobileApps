import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM
from MobileApps.libs.one_simulator.cdm_alert_simulation.warning_simulator_cdm import WarningSimulatorCDM

pytest.app_info = "Smart"

class Test_Suite_01_Cartridge_Counterfeit_Question(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        cls.driver, cls.fc = request.session.driver, request.session.fc
        cls.supplies_status = cls.fc.fd[FLOW_NAMES.SUPPLIES_STATUS]
        cls.error_manager = SimulatorErrorManagerCDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.moreto_base_yeti
    @pytest.mark.beam
    def test_01_validate_cartridge_counterfeit_question_65592(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65592, type="warning")
        success = WarningSimulatorCDM.cartridge_use_or_counterfeit_question_65592(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit question error"
        # Printer details page verification
        assert self.supplies_status.verify_warning_alert_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # Printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_secondary_yes_button()
        assert self.supplies_status.verify_secondary_no_button()
        assert self.supplies_status.verify_get_supplies_btn()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_02_validate_used_or_counterfeit_cartridges_detected_66267(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66267, type="warning")
        success = WarningSimulatorCDM.hp_altered_supply_counterfeit_66267(self.error_manager, color="k")
        assert success, "Failed to set used or counterfeit cartridges detected error"
        # Printer details page verification
        assert self.supplies_status.verify_warning_alert_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # Printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_secondary_yes_button()
        assert self.supplies_status.verify_secondary_no_button()

    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_03_validate_counterfeit_or_used_cartridges_identified_66268(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66268, type="warning")
        success = WarningSimulatorCDM.hp_altered_supply_counterfeit_66268(self.error_manager, color="k")
        assert success, "Failed to set counterfeit or used cartridges identified error"
        # Printer details page verification
        assert self.supplies_status.verify_warning_alert_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # Printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_secondary_continue_button()
        assert self.supplies_status.verify_get_more_help_btn()

    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_04_validate_counterfeit_or_used_cartridges_installed_66269(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66269, type="warning")
        success = WarningSimulatorCDM.counterfeit_or_used_cartridges_installed_66269(self.error_manager, color="k")
        assert success, "Failed to set counterfeit or used cartridges installed error"
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

    @pytest.mark.moreto_base_yeti
    @pytest.mark.beam
    @pytest.mark.trillium_plus
    def test_05_cartridge_used_or_counterfeit_flow_65592(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65592, type="warning")
        success = WarningSimulatorCDM.cartridge_used_or_counterfeit_flow_65592(self.error_manager, color="k")
        assert success, "Failed to set cartridge used or counterfeit flow error"
        # Printer details page verification
        assert self.supplies_status.verify_warning_alert_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # Printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_secondary_yes_button()
        assert self.supplies_status.verify_secondary_no_button()
        assert self.supplies_status.verify_get_supplies_btn()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.beam
    @pytest.mark.trillium_plus
    def test_06_cartridge_usedorcounterfeit_flow_continue_cancel_65592_65617(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65617, type="warning")
        success = WarningSimulatorCDM.cartridge_usedorcounterfeit_flow_continue_cancel_65592_65617(self.error_manager, color="k")
        assert success, "Failed to set cartridge used or counterfeit flow continue/cancel error"
        # Printer details page verification
        assert self.supplies_status.verify_warning_alert_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # Printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_secondary_continue_button()
        assert self.supplies_status.verify_get_more_help_btn()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.beam
    @pytest.mark.trillium_plus
    def test_07_cartridge_usedorcounterfeit_question_65592(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65592, type="warning")
        success = WarningSimulatorCDM.cartridge_usedorcounterfeit_question_65592(self.error_manager, color="k")
        assert success, "Failed to set cartridge used or counterfeit question error"
        # Printer details page verification
        assert self.supplies_status.verify_warning_alert_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # Printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_secondary_yes_button()
        assert self.supplies_status.verify_secondary_no_button()
        assert self.supplies_status.verify_get_supplies_btn()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_pdl
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.beam
    @pytest.mark.trillium_plus
    def test_08_cartridge_usedorcounterfeit_question_continue_65592_65594(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65594, type="warning")
        success = WarningSimulatorCDM.cartridge_usedorcounterfeit_question_continue_65592_65594(self.error_manager, color="k")
        assert success, "Failed to set cartridge used or counterfeit question continue error"
        # Printer details page verification
        assert self.supplies_status.verify_warning_alert_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # Printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_secondary_yes_button()
        assert self.supplies_status.verify_secondary_no_button()
        assert self.supplies_status.verify_get_supplies_btn()
        assert self.supplies_status.verify_primary_ok_button()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.beam
    @pytest.mark.trillium_plus
    def test_09_cartridge_usedorcounterfeit_question_yes_65592_65617(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=65592, type="warning")
        success = WarningSimulatorCDM.cartridge_usedorcounterfeit_question_yes_65592_65617(self.error_manager, color="k")
        assert success, "Failed to set cartridge used or counterfeit question yes error"
        # Printer details page verification
        assert self.supplies_status.verify_warning_alert_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # Printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_secondary_yes_button()
        assert self.supplies_status.verify_secondary_no_button()
        assert self.supplies_status.verify_get_supplies_btn()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.beam
    @pytest.mark.trillium_plus
    def test_10_cartridge_usedorCounterfeit_question_No_65592_66098(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66098, type="warning")
        success = WarningSimulatorCDM.cartridge_usedorCounterfeit_question_No_65592_66098(self.error_manager, color="k")
        assert success, "Failed to set cartridge used or counterfeit question no error"
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

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_11_hp_altered_supply_anticounterfeitflow_66267(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66267, type="warning")
        success = WarningSimulatorCDM.hp_altered_supply_anticounterfeitflow_66267(self.error_manager, color="k")
        assert success, "Failed to set HP altered supply anti-counterfeit flow error"
        # Printer details page verification
        assert self.supplies_status.verify_warning_alert_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # Printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_secondary_yes_button()
        assert self.supplies_status.verify_secondary_no_button()

    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_12_hp_altered_supply_counterfeitflow_continue_cancel_66268(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66268, type="warning")
        success = WarningSimulatorCDM.hp_altered_supply_counterfeitflow_continue_cancel_66268(self.error_manager, color="k")
        assert success, "Failed to set HP altered supply counterfeit flow continue/cancel error"
        # Printer details page verification
        assert self.supplies_status.verify_warning_alert_in_pdp_screen(alert_title)
        assert self.supplies_status.verify_warning_icon_in_pdp_screen(alert_icon)
        assert self.supplies_status.verify_color_icon_in_pdp_screen("BLACK")
        self.supplies_status.click_warning_alert_in_pdp_screen()
        # Printer status screen verification
        assert self.supplies_status.verify_alert_severity_icon_printer_status_screen()
        assert self.supplies_status.verify_alert_title_in_printer_status_screen(alert_title)
        assert self.supplies_status.verify_sms_detailed_body(alert_body)
        assert self.supplies_status.verify_secondary_continue_button()
        assert self.supplies_status.verify_get_more_help_btn()

    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_13_hp_altered_supply_from_counterfeitinstalledflow_Yes_66269(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66269, type="warning")
        success = WarningSimulatorCDM.hp_altered_supply_from_counterfeitinstalledflow_Yes_66269(self.error_manager, color="k")
        assert success, "Failed to set HP altered supply from counterfeit installed flow yes error"
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

    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_14_hp_altered_supply_cartridgerefilled_yes_66269(self):
        alert_title, alert_icon, alert_body = self.fc.read_supplies_status_json_files(ioref=66269, type="warning")
        success = WarningSimulatorCDM.hp_altered_supply_cartridgerefilled_yes_66269(self.error_manager, color="k")
        assert success, "Failed to set HP altered supply cartridge refilled yes error"
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
