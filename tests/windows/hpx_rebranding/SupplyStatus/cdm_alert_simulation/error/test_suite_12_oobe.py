import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM
from MobileApps.libs.one_simulator.cdm_alert_simulation.error_simulator_cdm import ErrorSimulatorCDM
from MobileApps.libs.one_simulator.printer_simulation import delete_simulator_printer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"


class Test_Suite_12_Oobe(object):
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
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_01_oobe_hp_trade_66175(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorCDM.oobe_hp_trade_66175(self.error_manager, color="k")
        assert success, "Failed to set HP trade error"
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

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_02_oobe_hp_altered_supply_anti_theft_66175(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorCDM.oobe_hp_altered_supply_anti_theft_66175(self.error_manager, color="k")
        assert success, "Failed to set HP altered supply anti-theft error"
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

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_03_oobe_hp_altered_supply_66175_hpplus(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorCDM.oobe_hp_altered_supply_66175_hpplus(self.error_manager, color="k")
        assert success, "Failed to set HP altered supply 66175 hpplus error"
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

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_04_oobe_loi_supply_66175(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorCDM.oobe_loi_supply_66175(self.error_manager, color="k")
        assert success, "Failed to set LOI supply 66175 error"
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

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_05_oobe_vloi_supply_66175(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorCDM.oobe_vloi_supply_66175(self.error_manager, color="k")
        assert success, "Failed to set VLOI supply 66175 error"
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

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_06_oobe_faulty_supply_shorted_contactpads_66175(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorCDM.oobe_faulty_supply_shorted_contactpads_66175(self.error_manager, color="k")
        assert success, "Failed to set faulty supply shorted contact pads 66175 error"
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

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_07_do_not_use_setup_oobe_printer_trial_pen_66175(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorCDM.do_not_use_setup_oobe_printer_trial_pen_66175(self.error_manager, color="k")
        assert success, "Failed to set do not use setup OOBE printer trial pen 66175 error"
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

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_08_hp_altered_supply_insert_t4_pen_from_another_printer_66175(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorCDM.hp_altered_supply_insert_t4_pen_from_another_printer_66175(self.error_manager, color="k")
        assert success, "Failed to set HP altered supply insert T4 pen from another printer 66175 error"
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

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_09_hppi_circuitry_pen_digital_signature_66175(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorCDM.hppi_circuitry_pen_digital_signature_66175(self.error_manager, color="k")
        assert success, "Failed to set HPPI circuitry pen digital signature 66175 error"
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

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_10_pen_type_proto_bit_regionalisation_section_66175(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorCDM.pen_type_proto_bit_regionalisation_section_66175(self.error_manager, color="k")
        assert success, "Failed to set pen type proto bit regionalisation section 66175 error"
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

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_11_misinstalled_cartridge_66175(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorCDM.misinstalled_cartridge_66175(self.error_manager, color="k")
        assert success, "Failed to set misinstalled cartridge 66175 error"
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

    @pytest.mark.moreto_base_yeti
    @pytest.mark.marconi_base_yeti
    @pytest.mark.kebin_eddington_yeti
    @pytest.mark.victoria_base_yeti
    @pytest.mark.tassel_base_yeti
    def test_12_oobe_faulty_supply_shorted_contactpads_66175(self):
        error_title, error_img, error_detailed_info = self.fc.read_supplies_status_json_files(ioref=66175, type="error")
        success = ErrorSimulatorCDM.oobe_faulty_supply_shorted_contactpads_66175(self.error_manager, color="k")
        assert success, "Failed to set OOBE faulty supply shorted contact pads 66175 error"
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
