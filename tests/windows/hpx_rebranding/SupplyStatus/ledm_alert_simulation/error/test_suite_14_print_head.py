import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.error_simulator_ledm import ErrorSimulatorLEDM
from MobileApps.libs.one_simulator.printer_simulation import delete_simulator_printer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_14_Print_Head(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        request.cls.driver = request.session.driver
        request.cls.fc = request.session.fc
        cls.supplies_status = request.cls.fc.fd["supplies_status"]
        cls.path = request.config.getoption("--local-build")
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.manhattan_yeti
    @pytest.mark.edwin
    @pytest.mark.weber_base
    @pytest.mark.tesla
    @pytest.mark.spark
    def test_01_validate_missing_printhead_65536(self):
        supply_error_title, supply_error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=65536, type="error")
        success = ErrorSimulatorLEDM.missing_printhead_65536(self.error_manager)
        assert success, "Failed to set missing_printhead_65536 error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(supply_error_title, supply_error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(supply_error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_alert_title_after_clicked()==supply_error_title, f"Alert Title text: '{supply_error_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Alert Body text: '{supply_error_title}' is incorrect/mismatching"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.manhattan_yeti
    @pytest.mark.edwin
    @pytest.mark.weber_base
    @pytest.mark.spark
    def test_02_validate_incompatible_printhead_65536(self):
        supply_error_title, supply_error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=65536, type="error")
        success = ErrorSimulatorLEDM.incompatible_printhead_65536(self.error_manager)
        assert success, "Failed to set incompatible_printhead_65536 error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(supply_error_title, supply_error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(supply_error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_alert_title_after_clicked() == supply_error_title, f"Alert Title text: '{supply_error_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Alert Body text: '{supply_error_title}' is incorrect/mismatching"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.edwin
    @pytest.mark.weber_base
    @pytest.mark.spark
    def test_03_validate_failed_printhead_65536(self):
        supply_error_title, supply_error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=65536, type="error")
        success = ErrorSimulatorLEDM.failed_printhead_65536(self.error_manager)
        assert success, "Failed to set failed_printhead_65536 error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(supply_error_title, supply_error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(supply_error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_alert_title_after_clicked() == supply_error_title, f"Alert Title text: '{supply_error_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Alert Body text: '{supply_error_title}' is incorrect/mismatching"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.sayan_wireless_flex
    def test_04_validate_shared_select_address_error_66209(self):
        supply_error_title, supply_error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66209, type="error")
        success = ErrorSimulatorLEDM.shared_select_address_error_66209(self.error_manager)
        assert success, "Failed to set shared_select_address_error_66209 error"
        self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(supply_error_title, supply_error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(supply_error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_alert_title_after_clicked() == supply_error_title, f"Alert Title text: '{supply_error_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Alert Body text: '{supply_error_title}' is incorrect/mismatching"
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert() 

    @pytest.mark.sayan_wireless_flex
    def test_05_validate_hp_protected_printheads_installed_66230(self):
        supply_error_title, supply_error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66230, type="error")
        success = ErrorSimulatorLEDM.hp_protected_printheads_installed_66230(self.error_manager,color='y')
        assert success, "Failed to set hp_protected_printheads_installed_66230 error"
        self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(supply_error_title, supply_error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(supply_error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('y')
        assert self.supplies_status.verify_alert_title_after_clicked() == supply_error_title, f"Alert Title text: '{supply_error_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Alert Body text: '{supply_error_title}' is incorrect/mismatching"
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.sayan_wireless_flex
    def test_06_validate_printhead_cartridge_missing_66207(self):
        supply_error_title, supply_error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66207, type="error")
        success = ErrorSimulatorLEDM.printhead_cartridge_missing_66207(self.error_manager,color='y')
        assert success, "Failed to set printhead_cartridge_missing_66207 error"
        self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(supply_error_title, supply_error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(supply_error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('y')
        assert self.supplies_status.verify_alert_title_after_clicked() == supply_error_title, f"Alert Title text: '{supply_error_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Alert Body text: '{supply_error_title}' is incorrect/mismatching"
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.sayan_wireless_flex
    def test_07_validate_printhead_failure_66211(self):
        supply_error_title, supply_error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66211, type="error")
        success = ErrorSimulatorLEDM.printhead_failure_66211(self.error_manager,color='y')
        assert success, "Failed to set printhead_failure_66211 error"
        self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(supply_error_title, supply_error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(supply_error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('y')
        assert self.supplies_status.verify_alert_title_after_clicked() == supply_error_title, f"Alert Title text: '{supply_error_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Alert Body text: '{supply_error_title}' is incorrect/mismatching"
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.sayan_wireless_flex
    def test_08_validate_incompatible_printhead_66213(self):
        supply_error_title, supply_error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66213, type="error")
        success = ErrorSimulatorLEDM.incompatible_printhead_66213(self.error_manager,"y")
        assert success, "Failed to set incompatible_printhead_66213 error"
        self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(supply_error_title, supply_error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(supply_error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('y')
        assert self.supplies_status.verify_alert_title_after_clicked() == supply_error_title, f"Alert Title text: '{supply_error_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Alert Body text: '{supply_error_title}' is incorrect/mismatching"
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()
