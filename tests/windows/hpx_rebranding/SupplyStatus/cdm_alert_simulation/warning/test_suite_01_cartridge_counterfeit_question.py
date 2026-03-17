import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM
from MobileApps.libs.one_simulator.cdm_alert_simulation.warning_simulator_cdm import WarningSimulatorCDM


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"


class Test_Suite_01_Cartridge_Counterfeit_Question(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        request.cls.driver = request.session.driver
        request.cls.fc = request.session.fc
        cls.profile = request.cls.fc.fd["profile"]
        cls.css = request.cls.fc.fd["css"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.add_printer = request.cls.fc.fd["addprinter"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.supplies_status = request.cls.fc.fd["supplies_status"]
        cls.path = request.config.getoption("--local-build")
        cls.error_manager = SimulatorErrorManagerCDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.moreto_base_yeti
    @pytest.mark.beam
    @pytest.mark.trillium_plus
    def test_01_validate_cartridge_counterfeit_question_65592(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=65592, type="warning")
        success = WarningSimulatorCDM.cartridge_use_or_counterfeit_question_65592(self.error_manager, color="k")
        assert success, "Failed to set cartridge counterfeit question error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon("k")
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_yes_btn(), "Yes button is not displayed"
        assert self.supplies_status.verify_no_btn(), "No button is not displayed"
        assert self.supplies_status.verify_get_supplies_btn(), "Get Supplies button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_02_validate_used_or_counterfeit_cartridges_detected_66267(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=66267, type="warning")
        success = WarningSimulatorCDM.hp_altered_supply_counterfeit_66267(self.error_manager, color="k")
        assert success, "Failed to set used or counterfeit cartridges detected error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon("k")
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_yes_btn(), "Yes button is not displayed"
        assert self.supplies_status.verify_no_btn(), "No button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_03_validate_counterfeit_or_used_cartridges_identified_66268(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=66268, type="warning")
        success = WarningSimulatorCDM.hp_altered_supply_counterfeit_66268(self.error_manager, color="k")
        assert success, "Failed to set counterfeit or used cartridges identified error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon("k")
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_continue_btn(), "Continue button is not displayed"
        assert self.supplies_status.verify_get_more_help_btn(), "Get More Help button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_04_validate_counterfeit_or_used_cartridges_installed_66269(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=66269, type="warning")
        success = WarningSimulatorCDM.counterfeit_or_used_cartridges_installed_66269(self.error_manager, color="k")
        assert success, "Failed to set counterfeit or used cartridges installed error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon("k")
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_ok_btn(), "OK button is not displayed"
        assert self.supplies_status.verify_get_supplies_btn(), "Get Supplies button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.beam
    @pytest.mark.trillium_plus
    def test_05_cartridge_used_or_counterfeit_flow_65592(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=65592, type="warning")
        success = WarningSimulatorCDM.cartridge_used_or_counterfeit_flow_65592(self.error_manager, color="k")
        assert success, "Failed to set cartridge used or counterfeit flow error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon("k")
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_yes_btn(), "Yes button is not displayed"
        assert self.supplies_status.verify_no_btn(), "No button is not displayed"
        assert self.supplies_status.verify_get_supplies_btn(), "Get Supplies button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.beam
    @pytest.mark.trillium_plus
    def test_06_cartridge_usedorcounterfeit_flow_continue_cancel_65592_65617(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=65617, type="warning")
        success = WarningSimulatorCDM.cartridge_usedorcounterfeit_flow_continue_cancel_65592_65617(self.error_manager, color="k")
        assert success, "Failed to set cartridge used or counterfeit flow continue/cancel error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon("k")
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_continue_btn(), "Continue button is not displayed"
        assert self.supplies_status.verify_get_more_help_btn(), "Get More Help button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.beam
    @pytest.mark.trillium_plus
    def test_07_cartridge_usedorcounterfeit_question_65592(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=65592, type="warning")
        success = WarningSimulatorCDM.cartridge_usedorcounterfeit_question_65592(self.error_manager, color="k")
        assert success, "Failed to set cartridge used or counterfeit question error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon("k")
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_pdl
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.beam
    @pytest.mark.trillium_plus
    def test_08_cartridge_usedorcounterfeit_question_continue_65592_65594(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=65594, type="warning")
        success = WarningSimulatorCDM.cartridge_usedorcounterfeit_question_continue_65592_65594(self.error_manager, color="k")
        assert success, "Failed to set cartridge used or counterfeit question continue error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon("k")
        assert self.supplies_status.verify_alert_title_after_clicked()
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.beam
    @pytest.mark.trillium_plus
    def test_09_cartridge_usedorcounterfeit_question_yes_65592_65617(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=65592, type="warning")
        success = WarningSimulatorCDM.cartridge_usedorcounterfeit_question_yes_65592_65617(self.error_manager, color="k")
        assert success, "Failed to set cartridge used or counterfeit question yes error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon("k")
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_continue_btn(), "Continue button is not displayed"
        assert self.supplies_status.verify_get_more_help_btn(), "Get More Help button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.beam
    @pytest.mark.trillium_plus
    def test_10_cartridge_usedorCounterfeit_question_No_65592_66098(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=66098, type="warning")
        success = WarningSimulatorCDM.cartridge_usedorCounterfeit_question_No_65592_66098(self.error_manager, color="k")
        assert success, "Failed to set cartridge used or counterfeit question no error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon("k")
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_11_hp_altered_supply_anticounterfeitflow_66267(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=66267, type="warning")
        success = WarningSimulatorCDM.hp_altered_supply_anticounterfeitflow_66267(self.error_manager, color="k")
        assert success, "Failed to set HP altered supply anti-counterfeit flow error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon("k")
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_yes_btn(), "Yes button is not displayed"
        assert self.supplies_status.verify_no_btn(), "No button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_12_hp_altered_supply_counterfeitflow_continue_cancel_66268(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=66268, type="warning")
        success = WarningSimulatorCDM.hp_altered_supply_counterfeitflow_continue_cancel_66268(self.error_manager, color="k")
        assert success, "Failed to set HP altered supply counterfeit flow continue/cancel error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon("k")
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_continue_btn(), "Continue button is not displayed"
        assert self.supplies_status.verify_get_more_help_btn(), "Get More Help button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_13_hp_altered_supply_from_counterfeitinstalledflow_Yes_66269(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=66269, type="warning")
        success = WarningSimulatorCDM.hp_altered_supply_from_counterfeitinstalledflow_Yes_66269(self.error_manager, color="k")
        assert success, "Failed to set HP altered supply from counterfeit installed flow yes error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon("k")
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_ok_btn(), "OK button is not displayed"
        assert self.supplies_status.verify_get_supplies_btn(), "Get Supplies button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_14_hp_altered_supply_cartridgerefilled_yes_66269(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=66269, type="warning")
        success = WarningSimulatorCDM.hp_altered_supply_cartridgerefilled_yes_66269(self.error_manager, color="k")
        assert success, "Failed to set HP altered supply cartridge refilled yes error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon("k")
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_ok_btn(), "OK button is not displayed"
        assert self.supplies_status.verify_get_supplies_btn(), "Get Supplies button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.jupiter
    def test_15_cartridge_altered_66562(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=66562, type="warning")
        success = WarningSimulatorCDM.cartridge_altered_66562(self.error_manager, color="k")
        assert success, "Failed to set cartridge altered error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon("k")
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()
