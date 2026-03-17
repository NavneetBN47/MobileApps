import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM
from MobileApps.libs.one_simulator.cdm_alert_simulation.information_simulator_cdm import InformationSimulatorCDM
from MobileApps.libs.one_simulator.printer_simulation import delete_simulator_printer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"


class Test_Suite_03_Hp_Cartridges_Installed(object):
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
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.tassel_base_yeti
    def test_01_validate_used_supply_prompt_66264(self):
        info_title, info_img, info_detailed_body = self.fc.read_supplies_status_json_files(ioref=66264, type="info")
        success = InformationSimulatorCDM.used_supply_prompt_66264(self.error_manager, color="k")
        assert success, "Failed to set HP cartridges installed info"
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
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.tassel_base_yeti
    def test_02_used_supply_flow_66264(self):
        info_title, info_img, info_detailed_body = self.fc.read_supplies_status_json_files(ioref=66264, type="info")
        success = InformationSimulatorCDM.used_supply_flow_66264(self.error_manager, color="k")
        assert success, "Failed to set used supply flow info"
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
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.tassel_base_yeti
    def test_03_genuine_hp_supply_flow_66265(self):
        info_title, info_img, info_detailed_body = self.fc.read_supplies_status_json_files(ioref=66265, type="info")
        success = InformationSimulatorCDM.genuine_hp_supply_flow_66265(self.error_manager, color="k")
        assert success, "Failed to set genuine HP supply flow info"
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
