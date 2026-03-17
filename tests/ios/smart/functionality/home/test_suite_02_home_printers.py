import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_01_Home_Printers(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, session_setup, load_printers_session, request):
        cls = cls.__class__
        cls.p = load_printers_session
        cls.printer_info = cls.p.get_printer_information()
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.stack = request.config.getoption("--stack")
        cls.fc.go_home(stack=cls.stack)

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.go_to_home_screen()
        self.fc.remove_default_paired_printer()
        self.fc.dismiss_tap_here_to_start()
        self.home.select_get_started_by_adding_a_printer()
        self.printers.verify_choose_printer_screen_ui()
        self.printers.select_add_printer_btn()
        self.printers.verify_printers_nav()

    def test_01_verify_printers_screen_ui(self):
        """
        C31298280 Fresh install, go home, click on big + sign and verify printers screen
        """
        self.printers.verify_printers_list_screen_ui()

    def test_02_verify_back_functionality_from_printers_screen(self):
        """
        C31298281 verify back button redirects user to home screen
        """
        self.printers.select_navigate_back()
        self.printers.verify_choose_printer_screen_ui()
        self.printers.select_navigate_back()
        self.home.close_smart_task_awareness_popup()
        self.home.verify_home()

    def test_03_verify_search_field(self):
        """
        C31298283 from the add printer's page, verify search bar's presence
        """
        self.printers.select_search_bar()
        self.printers.verify_cancel()
        assert self.driver.wdvr.is_keyboard_shown() is True

    def test_04_cancel_button_functionality(self):
        """
        C31298284 verify that clicking cancel button clears search field and that cancel button disappears
        """
        self.printers.select_search_bar()
        self.printers.verify_cancel()
        sample_text = "sample test 123"
        self.printers.find_printer_using_search_bar(sample_text)
        assert ma_misc.poll(lambda: self.printers.get_search_bar_text() == sample_text, timeout=30)
        self.printers.select_cancel()
        # TODO: check if apple fixes XCTest. https://github.com/appium/appium/issues/13288#issuecomment-535745703
        assert ma_misc.poll(lambda: self.printers.get_search_bar_text() == "") or \
               ma_misc.poll(lambda: self.printers.get_search_bar_text().lower() == "search for printer") or \
               ma_misc.poll(lambda: self.printers.get_search_bar_text() is None) or \
               ma_misc.poll(lambda: self.printers.get_search_bar_text() == self.printers.get_text_from_str_id("search_txt"), timeout=30) # iOS 12
        self.printers.verify_cancel(invisible=True)

    def test_05_x_button_functionality(self):
        """
        C31298284 verify that clicking the x button clears search field
        """
        self.printers.select_search_bar()
        self.printers.verify_cancel()
        sample_text = "sample test 123"
        self.printers.find_printer_using_search_bar(sample_text)
        assert ma_misc.poll(lambda: self.printers.get_search_bar_text() == sample_text)
        self.printers.select_clear_text_button()
        # TODO: check if apple fixes XCTest. https://github.com/appium/appium/issues/13288#issuecomment-535745703
        assert ma_misc.poll(lambda: self.printers.get_search_bar_text() == "") or \
               ma_misc.poll(lambda: self.printers.get_search_bar_text().lower() == "search for printer") or \
               ma_misc.poll(lambda: self.printers.get_search_bar_text() is None) or \
               ma_misc.poll(lambda: self.printers.get_search_bar_text() == self.printers.get_text_from_str_id("search_txt"), timeout=30) # iOS 12

    def test_06_verify_no_search_results(self):
        """
        C31298285 verify "No Search Results" on printers list when inputting invalid printer name/ip
        """
        self.printers.select_search_bar()
        self.printers.find_printer_using_search_bar("sample test 123")
        self.printers.verify_no_search_results()

    @pytest.mark.parametrize("search_bar_input", ["ip address", "bonjour name"])
    def test_07_valid_search_functionality(self, search_bar_input):
        """
        C31298286, C31298287
        """
        self.printers.select_search_bar()
        self.printers.find_printer_using_search_bar(self.printer_info[search_bar_input])
        self.printers.verify_printer_in_list(self.printer_info["bonjour name"])
        self.printers.verify_printer_in_list(self.printer_info["ip address"])
        assert ma_misc.poll(lambda: self.printers.count_number_of_printers() >= 1)
        self.printers.select_printer_in_list(self.printer_info[search_bar_input])
        self.home.close_smart_task_awareness_popup()
        self.home.verify_home()
        app_printer_name = self.home.get_printer_name_from_device_carousel()
        shortened_bonjour_name = ma_misc.truncate_printer_model_name(self.printer_info["bonjour name"], case_sensitive=False)
        assert app_printer_name == self.printer_info["bonjour name"] or \
                all(word in app_printer_name.lower().split() for word in shortened_bonjour_name.split())