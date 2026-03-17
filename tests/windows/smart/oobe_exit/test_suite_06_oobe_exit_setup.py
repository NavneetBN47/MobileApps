import pytest
import logging

from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.web.ows.yeti_flow_container import YetiFlowContainer

pytest.app_info = "GOTHAM"
class Test_Suite_06_OOBE_Exit_Setup(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.yf = YetiFlowContainer(cls.driver)
        cls.moobe = cls.fc.fd["moobe"]
        cls.printers = cls.fc.fd["printers"]
        cls.stack = request.config.getoption("--stack")
   
        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        logging.debug("reset printer ....")
        cls.p.oobe_reset_printer()
        logging.debug("skip oobe ...")
        cls.p.exit_oobe()
        logging.debug("printer connecting wifi...")
        cls.p.connect_to_wifi(ssid, password)

    def test_01_click_exit_setup_btn_on_oobe_flow(self):
        """
        In any OOBE flow that app can tell device is yeti
        Click Exit Setup button
        Check "Setup not complete" modal UI
        Verify the "Setup not completed" modal shows.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28564478(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28564486
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28564488(One of them)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28564487
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28564489
        """
        self.fc.go_home()
        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen()
        printer = self.printers.search_printer(self.p.p_obj.ipAddress)
        printer.click()
        self.moobe.click_button_on_fp_from_printer(self.p)
        self.yf.flow["smart_printer_consent"].verify_printer_consent_screen()
        self.yf.flow["smart_printer_consent"].click_exit_setup_btn()
        if self.printers.verify_setup_incomplete_dialog(raise_e=False):
            self.printers.click_exit_setup_btn()
            self.home.verify_home_screen()
            self.home.verify_carousel_finish_setup_btn()
        else:
            self.printers.verify_printer_setup_is_incomplete_dialog_2()
  