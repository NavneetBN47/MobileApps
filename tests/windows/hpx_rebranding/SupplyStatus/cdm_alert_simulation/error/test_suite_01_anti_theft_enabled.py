import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM
from MobileApps.libs.one_simulator.cdm_alert_simulation.error_simulator_cdm import ErrorSimulatorCDM
from MobileApps.libs.one_simulator.printer_simulation import delete_simulator_printer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"


class Test_Suite_01_Anti_Theft_Enabled(object):
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

    @pytest.mark.tassel_base_yeti
    @pytest.mark.trillium_plus
    def test_01_validate_anti_theft_enabled_error_65612(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=65612, type="error")
        success = ErrorSimulatorCDM.anti_theft_enabled_error_65612(self.error_manager, color="k")
        assert success, "Failed to set anti-theft enabled error"
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
        assert self.supplies_status.verify_get_supplies_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_02_validate_anti_theft_enabled_error_66175(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorCDM.anti_theft_enabled_error_66175(self.error_manager, color="k")
        assert success, "Failed to set anti-theft enabled error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(error_title, error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_alert_title_after_clicked() == error_title, "Alert title Mismatched after clicked"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Detailed {error_title} is incorrect"
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.selene
    def test_03_antitheft_enabled_supplyerror_66035(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66035, type="error")
        success = ErrorSimulatorCDM.antitheft_enabled_supplyerror_66035(self.error_manager, color="k")
        assert success, "Failed to set anti-theft enabled supply error"
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
        assert self.supplies_status.verify_get_supplies_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()
