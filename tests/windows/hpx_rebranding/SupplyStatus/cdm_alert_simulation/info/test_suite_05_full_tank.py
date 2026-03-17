import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM
from MobileApps.libs.one_simulator.cdm_alert_simulation.information_simulator_cdm import InformationSimulatorCDM
from MobileApps.libs.one_simulator.printer_simulation import delete_simulator_printer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"


class Test_Suite_05_Full_Tank(object):
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
    @pytest.mark.pixiu
    def test_01_fulltank_66020(self):
        info_title, info_img, info_detailed_body = self.fc.read_supplies_status_json_files(ioref=66020, type="info")
        success = InformationSimulatorCDM.fulltank_66020(self.error_manager, color="k")
        assert success, "Failed to set full tank info"
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

    @pytest.mark.lebi_wireless_flex
    @pytest.mark.pixiu
    def test_02_tank_filled_66020(self):
        info_title, info_img, info_detailed_body = self.fc.read_supplies_status_json_files(ioref=66020, type="info")
        success = InformationSimulatorCDM.tank_filled_66020(self.error_manager, color="k")
        assert success, "Failed to set tank filled info"
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

    @pytest.mark.pixiu
    def test_03_tank_full_66437(self):
        info_title, info_img, info_detailed_body = self.fc.read_supplies_status_json_files(ioref=66437, type="info")
        success = InformationSimulatorCDM.tank_full_66437(self.error_manager, color="k")
        assert success, "Failed to set tank full info"
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
