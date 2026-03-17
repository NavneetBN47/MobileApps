import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import logging

pytest.app_info = "GOTHAM"
class Test_Suite_12_Printer_Status_Hover(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.printer_status = cls.fc.fd["printer_status"]
        cls.serial_number = cls.p.get_printer_information()["serial number"]

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    def test_01_go_home_and_add_a_printer(self):
        """ 
        Use Flag 7 to bring up all supported printer status messages.
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.fc.trigger_printer_status(self.serial_number, ioref_list=False)

    def test_02_hover_and_select_ioref_item(self):
        """ 
        Hover over the list item on Printer Status screen.
        Pressed on the list item on Printer Status screen. (not covered)
        Selected the list item on Printer Status screen.

        Verify background of list item turns to light gray when hover.
        Verify background of list item turns to a little darker than light gray when pressed. (not covered)
        Verify background of list item turns to light blue when selected.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14102976
        """
        self.printer_status.click_ps_ioref_item('65548')
        self.fc.save_image('middle_status_list', 'printer_status', 'ioref_o.png', value=0.5)
        self.printer_status.hover_ioref_item('65536')
        self.fc.save_image('middle_status_list', 'printer_status', 'ioref_h.png', value=0.5)
        value = self.fc.check_element_background('middle_status_list', 'printer_status', 'ioref_o.png', value=0.5)
        logging.info("hover vs org: {}".format(value))
        assert 0.0075 > value > 0.007
        value = self.fc.check_element_background('middle_status_list', 'printer_status', 'ioref_h.png', value=0.5)
        logging.info("hover vs hover: {}".format(value))
        assert value < 0.001

        self.printer_status.click_ps_ioref_item('65536')
        self.fc.save_image('middle_status_list', 'printer_status', 'ioref_s.png', value=0.5)
        value = self.fc.check_element_background('middle_status_list', 'printer_status', 'ioref_o.png', value=0.5)
        logging.info("select vs org: {}".format(value))
        assert 0.0035 > value > 0.003
        value = self.fc.check_element_background('middle_status_list', 'printer_status', 'ioref_s.png', value=0.5)
        logging.info("select vs select: {}".format(value))
        assert value < 0.001

