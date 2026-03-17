import pytest
import logging

from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_05_non_hero_computer_on_ethernet_2(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.moobe = cls.fc.fd["moobe"]
        cls.print = cls.fc.fd["print"]

        cls.stack = request.config.getoption("--stack")
        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, cls.ssid, cls.password)
        logging.debug("reset printer ....")
        cls.p.oobe_reset_printer()
        logging.debug("skip oobe ...")
        cls.p.exit_oobe()

    def test_01_go_through_awc_flow(self):
        """
        Verify the flow is successful
        Verify printer is added to main UI after the flow
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/19536588
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/19536589
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28717723
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28718580
        """
        self.fc.go_home()
        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen()
        self.printers.select_my_printer_isnt_listed_link()
        self.moobe.verify_we_found_your_printer_screen(title=True)
        self.moobe.select_continue()
        self.moobe.verify_access_wifi_password_dialog()
        self.moobe.select_continue()
        self.moobe.verify_connect_to_wifi_progress_screen()
        self.moobe.handle_popup_on_connect_to_wifi_progress_screen(self.p)
        self.moobe.go_through_connect_to_wifi_process()
        self.printers.verify_install_success_dialog(timeout=180)
        self.printers.click_install_success_dialog_continue_btn()
        self.home.verify_home_screen()
        self.home.verify_carousel_finish_setup_btn()

    def test_02_send_print_job(self):
        """
        Send a print job to the printer
        """
        self.home.select_print_documents_tile()
        self.print.verify_supported_document_file_types_dialog()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.COLOR_PDF)
        self.print.verify_simple_print_dialog()
        self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()
        