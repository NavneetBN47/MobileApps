import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM
from MobileApps.libs.one_simulator.cdm_alert_simulation.information_simulator_cdm import InformationSimulatorCDM
from MobileApps.libs.one_simulator.printer_simulation import delete_simulator_printer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"


class Test_Suite_02_Single_Cartridge_mode(object):
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

    @pytest.mark.trillium_plus
    def test_01_validate_single_cartridge_mode_65553(self):
        info_title, info_img, info_detailed_body = self.fc.read_supplies_status_json_files(ioref=65553, type="info")
        success = InformationSimulatorCDM.single_cartridge_mode_65553(self.error_manager, color="k")
        assert success, "Failed to set cartridge very low info"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(info_title, info_img, type="info")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_info_icon_in_pdp()
        assert self.supplies_status.verify_info_alert_title_in_pdp(info_title)
        self.supplies_status.click_info_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == info_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(info_detailed_body), f"Detailed {info_title} is incorrect"
        assert self.supplies_status.verify_ok_btn(), "OK button is not present"
        assert self.supplies_status.verify_get_more_help_btn(), "Get More Help button is not present"
        assert self.supplies_status.verify_get_supplies_btn(), "Get Supplies button is not present"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_pdl
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.beam
    @pytest.mark.trillium_plus
    def test_02_used_hp_cartridge_65554(self):
        info_title, info_img, info_detailed_body = self.fc.read_supplies_status_json_files(ioref=65554, type="info")
        success = InformationSimulatorCDM.used_hp_cartridge_65554(self.error_manager, color="k")
        assert success, "Failed to set used_hp_cartridge_65554 info"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(info_title, info_img, type="info")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_info_icon_in_pdp()
        assert self.supplies_status.verify_info_alert_title_in_pdp(info_title)
        self.supplies_status.click_info_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == info_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(info_detailed_body), f"Detailed {info_title} is incorrect"
        assert self.supplies_status.verify_ok_btn(), "OK button is not present"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_pdl
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.beam
    @pytest.mark.trillium_plus
    def test_03_cartridge_expected_setup_65561(self):
        info_title, info_img, info_detailed_body = self.fc.read_supplies_status_json_files(ioref=65561, type="info")
        success = InformationSimulatorCDM.cartridge_expected_setup_65561(self.error_manager, color="k")
        assert success, "Failed to set genuine HP info"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(info_title, info_img, type="info")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_info_icon_in_pdp()
        assert self.supplies_status.verify_info_alert_title_in_pdp(info_title)
        self.supplies_status.click_info_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == info_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(info_detailed_body), f"Detailed {info_title} is incorrect"
        assert self.supplies_status.verify_ok_btn(), "OK button is not present"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_04_single_ink_cartridge_mode_66263(self):
        info_title, info_img, info_detailed_body = self.fc.read_supplies_status_json_files(ioref=66263, type="info")
        success = InformationSimulatorCDM.single_ink_cartridge_mode_66263(self.error_manager, color="k")
        assert success, "Failed to set single ink cartridge mode info"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(info_title, info_img, type="info")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_info_icon_in_pdp()
        assert self.supplies_status.verify_info_alert_title_in_pdp(info_title)
        self.supplies_status.click_info_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == info_title, "Alert title is mismatched"
        assert self.fc.verify_detailed_body_about_printer_status_alert(info_detailed_body), f"Detailed {info_title} is incorrect"
        assert self.supplies_status.verify_ok_btn(), "OK button is not present"
        assert self.supplies_status.verify_get_more_help_btn(), "Get More Help button is not present"
        assert self.supplies_status.verify_get_supplies_btn(), "Get Supplies button is not present"
        self.fc.verify_supplies_status_buttons_after_clicked_alert()
