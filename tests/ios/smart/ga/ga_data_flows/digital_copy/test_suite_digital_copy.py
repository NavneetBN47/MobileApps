import pytest
import json
from time import sleep
from datetime import datetime
import SPL.driver.driver_factory as p_driver_factory
from MobileApps.libs.ma_misc import ma_misc
from SPL.driver.reg_printer import PrinterNotReady
from SPL.driver.driver_factory import printer_driver_factory
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import OBJECT_SIZE, RESIZE

pytest.app_info = "SMART"

@pytest.mark.usefixtures("require_driver")
class Test_Class(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, require_driver):
        cls = cls.__class__
        cls.fc = FlowContainer(cls.driver)
        cls.copy = cls.fc.fd["copy"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = p_driver_factory.get_printer(cls.sys_config["printer_power_config"], printer_serial="TH84U13238")
        cls.p.set_mech_mode(mech=False)
        cls.printer_info = cls.p.get_printer_information()
        cls.printer_bonjour_name = cls.printer_info['bonjour name']
        cls.printer_ip = cls.printer_info['ip address']

    def test_01_digital_copy_data_flow1(self):
        self.fc.go_home(verify_ga=True)
        self.fc.add_printer_by_ip(printer_ip=self.printer_ip)
        self.fc.go_copy_screen_from_home()

    def test_02_digital_copy_data_flow2(self):
        self.fc.go_home(verify_ga=True)
        self.fc.add_printer_by_ip(printer_ip=self.printer_ip)
        self.fc.go_copy_screen_from_home()
        self.copy.select_object_size(object_size=OBJECT_SIZE.SIZE_US_LEGAL)
        self.copy.select_flash_button()
        self.copy.select_capture_button()
        self.copy.verify_copy_preview_screen()

    def test_03_digital_copy_data_flow3(self):
        self.fc.go_home(verify_ga=True)
        self.fc.add_printer_by_ip(printer_ip=self.printer_ip)
        self.fc.go_copy_screen_from_home()
        self.copy.select_object_size(object_size=OBJECT_SIZE.SIZE_DRIVER_LICENSE)
        self.copy.select_flash_button()
        self.copy.select_capture_button()
        self.copy.verify_copy_preview_screen()
        self.copy.select_add_more_pages()
        self.copy.verify_copy_screen()
        self.copy.select_capture_button()
        self.copy.verify_copy_preview_screen()
        self.copy.select_number_of_copies(change_copies=1)
        self.copy.select_resize_in_digital_copy(resize=RESIZE.RESIZE_FILL_PAGE)
        self.copy.select_start_color()