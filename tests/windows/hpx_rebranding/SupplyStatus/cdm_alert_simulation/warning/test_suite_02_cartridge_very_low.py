import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM
from MobileApps.libs.one_simulator.cdm_alert_simulation.information_simulator_cdm import InformationSimulatorCDM
from MobileApps.libs.one_simulator.cdm_alert_simulation.warning_simulator_cdm import WarningSimulatorCDM
from MobileApps.libs.one_simulator.printer_simulation import delete_simulator_printer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"


class Test_Suite_02_Cartridge_Very_Low(object):
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
    @pytest.mark.tassel_base_yeti
    def test_01_validate_cartridge_very_low_66241(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=66241, type="warning")
        success = WarningSimulatorCDM.cartridge_very_low_66241(self.error_manager, color="k")
        assert success, "Failed to set anti-theft enabled error"
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
        assert self.supplies_status.verify_get_more_help_btn(), "Get More Help button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()
    
    def test_02_validate_cartridges_very_low_66710(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=66710, type="warning")
        success = WarningSimulatorCDM.vloi_supply_66710(self.error_manager, color="k")
        assert success, "Failed to set cartridges very low error"
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
        assert self.supplies_status.verify_get_more_help_btn(), "Get More Help button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.victoria_base_yeti
    def test_03_validate_cartridge_very_low_66712(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=66712, type="warning")
        success = WarningSimulatorCDM.vloi_supply_66712(self.error_manager, color="k")
        assert success, "Failed to set cartridge very low error"
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
        assert self.supplies_status.verify_get_more_help_btn(), "Get More Help button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    def test_04_vloi_supply_66710(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=66710, type="warning")
        success = WarningSimulatorCDM.vloi_supply_66710(self.error_manager, color="k")
        assert success, "Failed to set vloi supply error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_ok_btn(), "OK button is not displayed"
        assert self.supplies_status.verify_get_supplies_btn(), "Get Supplies button is not displayed"
        assert self.supplies_status.verify_get_more_help_btn(), "Get More Help button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.victoria_base_yeti
    def test_05_vloi_supply_66712(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=66712, type="warning")
        success = WarningSimulatorCDM.vloi_supply_66712(self.error_manager, color="k")
        assert success, "Failed to set vloi supply error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_ok_btn(), "OK button is not displayed"
        assert self.supplies_status.verify_get_supplies_btn(), "Get Supplies button is not displayed"
        assert self.supplies_status.verify_get_more_help_btn(), "Get More Help button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_06_vloi_supply_66241(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=66241, type="warning")
        success = WarningSimulatorCDM.vloi_supply_66241(self.error_manager, color="k")
        assert success, "Failed to set vloi supply error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_ok_btn(), "OK button is not displayed"
        assert self.supplies_status.verify_get_supplies_btn(), "Get Supplies button is not displayed"
        assert self.supplies_status.verify_get_more_help_btn(), "Get More Help button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()
    
    @pytest.mark.moreto_base_yeti
    @pytest.mark.trillium_plus
    def test_07_cartridge_very_low_flow_65546(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=65546, type="warning")
        success = WarningSimulatorCDM.cartridge_very_low_flow_65546(self.error_manager, color="k")
        assert success, "Failed to set anti-theft enabled error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_ok_btn(), "OK button is not displayed"
        assert self.supplies_status.verify_get_supplies_btn(), "Get Supplies button is not displayed"
        assert self.supplies_status.verify_get_more_help_btn(), "Get More Help button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.selene
    def test_08_cartridge_verylow_continue_66085(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=66085, type="warning")
        success = WarningSimulatorCDM.cartridge_verylow_continue_66085(self.error_manager, color="k")
        assert success, "Failed to set cartridge very low continue error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is not matched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_get_supplies_btn(), "Get Supplies button is not displayed"
        assert self.supplies_status.verify_get_more_help_btn(), "Get More Help button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.jupiter
    def test_09_printhead_used_with_non_hp_ink_66413(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=66413, type="warning")
        success = WarningSimulatorCDM.printhead_used_with_non_hp_ink(self.error_manager, color="k")
        assert success, "Failed to set printhead used with non-HP ink warning"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is not matched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_ok_btn(), "OK button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.jupiter
    def test_10_cartridge_very_low_66515(self):
        warning_title, warning_img, warning_detailed_body = self.fc.read_supplies_status_json_files(ioref=66515, type="warning")
        success = WarningSimulatorCDM.cartridge_very_low_66515(self.error_manager, color="k")
        assert success, "Failed to set cartridge very low warning"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(warning_title, warning_img, type="warning")
        self.supplies_status.click_printer_card()
        self.supplies_status.verify_warning_icon_in_pdp()
        self.supplies_status.verify_warning_alert_title_in_pdp(warning_title)
        self.supplies_status.click_warning_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == warning_title, "Alert title is not matched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(warning_detailed_body), f"Detailed {warning_title} is incorrect"
        assert self.supplies_status.verify_ok_btn(), "OK button is not displayed"
        assert self.supplies_status.verify_get_supplies_btn(), "Get Supplies button is not displayed"
        assert self.supplies_status.verify_get_more_help_btn(), "Get More Help button is not displayed"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()