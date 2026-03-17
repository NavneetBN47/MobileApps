import pytest

from MobileApps.libs.ma_misc import conftest_misc as c_misc
from selenium.common.exceptions import NoSuchElementException


pytest.app_info = "GOTHAM"
class Test_Suite_03_Device_Picker_Office_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)

    def test_01_verify_select_a_different_printer_dialog(self):
        """
        Navigate to device picker via any available entry
        Select the Offline printer from Device Picker
        Click "OK" button on the "Select a Different Printer" dialog

        Verify "Select a Different Printer" dialog shows with "OK" button
        Verify user navigates back to the device picker
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27266548
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27266549 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13311458  
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/27266550 
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.home.right_click_printer_carousel()
        self.home.click_hide_printer_list_item()
        self.home.click_hide_this_printer_dialog_hide_printer_btn()
        try:
            self.fc.trigger_printer_offline_status(self.p)
            self.fc.restart_hp_smart()
            self.home.verify_home_screen()
            self.home.select_left_add_printer_btn()
            self.printers.verify_device_picker_screen()
            hostname = self.p.get_printer_information()["host name"][:-1]
            printer = self.printers.search_printer(hostname)
            # printer = self.printers.search_printer(self.p.p_obj.ipAddress)
            self.printers.verify_printer_status_is_offline()
            printer.click()
            self.printers.verify_select_a_different_printer_dialog()
            self.printers.click_ok_btn()
            self.printers.verify_device_picker_screen()
        except NoSuchElementException:
            raise NoSuchElementException("Select a Different Printer dialog does not displays")
        finally:
            self.fc.restore_printer_online_status(self.p)
