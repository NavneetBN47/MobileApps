import pytest
import logging
import time

from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow
from MobileApps.libs.flows.web.ows.yeti_flow_container import YetiFlowContainer
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.common.gotham.ows_flow import OwsFlow

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"

class Test_Suite_01_2N_from_app_launch(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.web_driver = utility_web_session
        cls.home = cls.fc.fd["home"]
        cls.sf = SystemFlow(cls.driver)
        cls.yf = YetiFlowContainer(cls.driver)
        cls.moobe = cls.fc.fd["moobe"]
        cls.ows = OwsFlow(cls.driver, cls.web_driver)
        cls.stack = request.config.getoption("--stack")
                                                        
        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        cls.host_name = cls.p.get_printer_information()['host name']
        cls.firmware = cls.p.get_printer_information()["firmware version"]
        logging.info("host name:\n {}".format(cls.host_name))
        logging.debug("reset printer ....")
        cls.p.oobe_reset_printer()
        logging.debug("skip oobe ...")
        cls.p.exit_oobe()
        logging.debug("printer connecting wifi...")
        cls.p.connect_to_wifi(ssid, password)
        logging.debug("All preparations are complete!")
        meg = cls.p.is_connected_to_wifi()
        logging.info("is connected wifi?:\n {}".format(meg))

    def test_01_check_finish_btn_on_main_ui(self):
        """
        Install the latest Gotham app. (if there is one installed, uninstall it first)
        Prepare 1 or more not installed printer.
        Printer has not run Gotham OOBE/Or Post OOBE flow,
        Install 1 or more printers to the computer.
        Launch app.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890710
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27731313
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890709
        """ 
        value_name = self.host_name.split("HP")[1]
        printer_type = (self.firmware)[:3]
        close_activity = eval("w_const.CLOSE_ACTIVITY." + pytest.set_info + '_' + pytest.app_info)
        self.driver.terminate_app(close_activity)
        time.sleep(1)
        self.driver.ssh.send_command('Start-Process "ms-settings:printers" -windowstyle Maximized') 
        self.sf.select_printer_on_win_settings(value_name)
        self.sf.launch_app_on_settings()
        self.fc.fd["gotham_utility"].click_maximize()
        assert self.fc.fd["gotham_utility"].verify_window_visual_state_maximized() is True 
        self.fc.go_home()
        self.home.verify_carousel_finish_setup_btn()
        self.home.click_finish_setup_btn()
        self.moobe.click_button_on_fp_from_printer(self.p)
        self.ows.go_through_ows_flow(printer_type)
     