import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM
from MobileApps.libs.one_simulator.cdm_alert_simulation.error_simulator_cdm import ErrorSimulatorCDM


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"


class Test_Suite_11_Print_Head(object):
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

    @pytest.mark.lebi_wireless_flex
    def test_01_printheadproblem_66207(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66207, type="error")
        success = ErrorSimulatorCDM.printheadproblem_66207(self.error_manager,color='k')
        assert success, "Failed to set printhead problem error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(error_title, error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == error_title, "Alert title Mismatched after clicked"   
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Detailed {error_title} is incorrect"
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.lebi_wireless_flex
    def test_02_incompatible_printhead_66213(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66213, type="error")
        success = ErrorSimulatorCDM.incompatible_printhead_66213(self.error_manager,color='k')
        assert success, "Failed to set incompatible printhead error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(error_title, error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == error_title, "Alert title Mismatched after clicked"   
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Detailed {error_title} is incorrect"
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.lebi_wireless_flex
    def test_03_print_head_problem_66211(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66211, type="error")
        success = ErrorSimulatorCDM.print_head_problem_66211(self.error_manager,color='k')
        assert success, "Failed to set printhead problem error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(error_title, error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == error_title, "Alert title Mismatched after clicked"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Detailed {error_title} is incorrect"
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.lebi_wireless_flex
    def test_04_hp_protected_printheads_installed_66230(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66230, type="error")
        success = ErrorSimulatorCDM.hp_protected_printheads_installed_66230(self.error_manager,color='k')
        assert success, "Failed to set HP protected printheads installed error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(error_title, error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_alert_title_in_pdp(error_title)
        assert self.supplies_status.verify_error_icon_in_pdp()
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == error_title, "Alert title Mismatched after clicked"   
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Detailed {error_title} is incorrect"
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.jupiter
    def test_05_printhead_not_present_66128(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66128, type="error")
        success = ErrorSimulatorCDM.printhead_not_present_66128(self.error_manager,color='k')
        assert success, "Failed to set printhead not present error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(error_title, error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_alert_title_in_pdp(error_title)
        assert self.supplies_status.verify_error_icon_in_pdp()
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == error_title, "Alert title Mismatched after clicked"   
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Detailed {error_title} is incorrect"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.jupiter
    def test_06_printhead_replacement_incomplete_66130(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66130, type="error")
        success = ErrorSimulatorCDM.printhead_replacement_incomplete_66130(self.error_manager,color='k')
        assert success, "Failed to set printhead replacement incomplete error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(error_title, error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_alert_title_in_pdp(error_title)
        assert self.supplies_status.verify_error_icon_in_pdp()
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == error_title, "Alert title Mismatched after clicked"   
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Detailed {error_title} is incorrect"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.jupiter
    def test_07_printhead_reseat_66131(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66131, type="error")
        success = ErrorSimulatorCDM.printhead_reseat_66131(self.error_manager,color='k')
        assert success, "Failed to set printhead reseat error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(error_title, error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_alert_title_in_pdp(error_title)
        assert self.supplies_status.verify_error_icon_in_pdp()
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == error_title, "Alert title Mismatched after clicked"   
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Detailed {error_title} is incorrect"
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.pixiu
    def test_08_printhead_failure_66442(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66442, type="error")
        success = ErrorSimulatorCDM.printhead_failure_66442(self.error_manager,color='k')
        assert success, "Failed to set printhead failure error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(error_title, error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_alert_title_after_clicked() == error_title, "Alert title Mismatched after clicked"   
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Detailed {error_title} is incorrect"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()
