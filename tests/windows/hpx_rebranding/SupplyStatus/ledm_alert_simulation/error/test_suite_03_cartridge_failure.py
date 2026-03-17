import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import SimulatorErrorManagerLEDM
from MobileApps.libs.one_simulator.ledm_alert_simulation.error_simulator_ledm import ErrorSimulatorLEDM
from MobileApps.libs.one_simulator.printer_simulation import delete_simulator_printer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_03_Cartridge_Failure(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request):
        cls = cls.__class__
        request.cls.driver = request.session.driver
        request.cls.fc = request.session.fc
        cls.supplies_status = request.cls.fc.fd["supplies_status"]
        cls.path = request.config.getoption("--local-build")
        cls.error_manager = SimulatorErrorManagerLEDM(printer_ip=request.session.printer_ip, serial_number=request.session.printer_serial_number)

    @pytest.mark.malbec_trad
    @pytest.mark.muscatel
    @pytest.mark.vasari_base_yeti
    @pytest.mark.novelli_plus_yeti
    @pytest.mark.poseidon_wl_flex
    @pytest.mark.kronos_ik_tank_flex
    @pytest.mark.spark
    @pytest.mark.shaolin
    @pytest.mark.verona
    @pytest.mark.palermo_fast
    def test_01_validate_cartridge_failure_65542(self):
        supply_error_title, supply_error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=65542, type="error")
        success = ErrorSimulatorLEDM.cartridge_failure_65542(self.error_manager, color="k")
        assert success, "Failed to set cartridge_failure_65542 error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(supply_error_title, supply_error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(supply_error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == supply_error_title, f"Alert Title text: '{supply_error_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Alert Body text: '{supply_error_title}' is incorrect/mismatching"
        assert self.supplies_status.verify_get_more_help_btn()
        assert self.supplies_status.verify_get_supplies_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.muscatel
    @pytest.mark.taccola_base_yeti
    @pytest.mark.narita_plus_yeti
    def test_02_validate_cartridge_failure_65675(self):
        supply_error_title, supply_error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=65675, type="error")
        success = ErrorSimulatorLEDM.cartridge_failure_65675(self.error_manager, color="k")
        assert success, "Failed to set cartridge_failure_65675 error"
        assert self.supplies_status.verify_printer_card_present()
        assert self.fc.validate_supplies_status_headers_home_page(supply_error_title, supply_error_img, type="error")
        self.supplies_status.click_printer_card()
        assert self.supplies_status.verify_error_icon_in_pdp()
        assert self.supplies_status.verify_error_alert_title_in_pdp(supply_error_title)
        self.supplies_status.click_error_alert_in_pdp()
        assert self.supplies_status.verify_cartridge_colour_icon('k')
        assert self.supplies_status.verify_alert_title_after_clicked() == supply_error_title, f"Alert Title text: '{supply_error_title}' is incorrect/mismatching"
        assert self.fc.verify_detailed_body_about_printer_status_alert(error_detailed_info), f"Alert Body text: '{supply_error_title}' is incorrect/mismatching"
        assert self.supplies_status.verify_get_more_help_btn()
        self.fc.verify_supplies_status_buttons_after_clicked_alert()

    @pytest.mark.muscatel
    @pytest.mark.taccola_base_yeti
    def test_03_validate_insert_non_setup_cartridge_65688(self):
        supply_error_title, supply_error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=65688, type="error")
        success = ErrorSimulatorLEDM.insert_non_setup_cartridge_65688(self.error_manager, color="y")
        assert success, "Failed to set insert_non_setup_cartridge_65688 error"
        assert self.supplies_status.verify_printer_card_present()
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
