import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const
pytest.app_info = "SMART"


class Test_Suite_01_Support_Product_Information_Card(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_ip = cls.p.get_printer_information()["ip address"]
        cls.fc.hpx = True
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.scan = cls.fc.fd["scan"]
        cls.welcome_web = cls.fc.fd["welcome_web"]
        cls.notifications = cls.fc.fd["notifications"]
        cls.support = cls.fc.fd["support"]
        cls.profile = cls.fc.fd["profile"]

    def test_01_verify_get_help_ui_card(self):
        """C52673527,C53167098,C53188286
        Description : Verify 'Get Help' UI - app Online: Printers
        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Observe the Get help card.
        Expected Result:
        Please verify only the card UI looks correct without any cropping or obvious UI issues. All the visible links should be clickable and navigate user to the correct pages.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("hpx_get_help_card")

    def test_02_verify_virtual_assistant_chat(self):
        """C52674026
        Description : Verify the behavior of Virtual Assistant Chat
        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on 'Start Virtual Assistant" button under Get help card
        Observe the behavior
        Expected Result:
        Please verify only the card UI looks correct without any cropping or obvious UI issues. All the visible links should be clickable and navigate user to the correct pages.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("start_virtual_assistant", click_obj=True)
        self.driver.click("_shared_str_ok")

    def test_03_verify_virtual_assistant_chat_closesessionpopupUI(self):
        """C44019061
        Description : Verify the behavior of Virtual Assistant Chat Close Session Popup UI
        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on 'Start Virtual Assistant" button under Get help card
        Chat with the agent
        Tap on End Session
        Observe the behavior and the Close Session UI
        Expected Result:
        Please verify only the card UI looks correct without any cropping or obvious UI issues. All the visible links should be clickable and navigate user to the correct pages.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("start_virtual_assistant", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.support.verify_end_session_btn()

    def test_04_verify_contact_us_btn(self):
        """C53149745
        Description : Verify the behavior of Contact Us button
        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on 'Contact Us' button under Get help card
        Observe the behavior
        Expected Result:
        Please verify only the card UI looks correct without any cropping or obvious UI issues. All the visible links should be clickable and navigate user to the correct pages.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("hpx_contact_us_arrow", click_obj=True)

    def test_05_verify_contact_us_change_region_option(self):
        """C53150705
        Description : Verify the behavior of Contact Us change support region option
        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on 'Contact Us' button under Get help card
        Tap on the drop down to change the support region option6.
        Observe the behavior
        Expected Result: Verify the dropdown menu content & behavior

        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("hpx_contact_us_arrow", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.driver.click("hpx_support_change_region")
        self.driver.click("hpx_change_region_text_feild")
        assert self.driver.wait_for_object(
            "hpx_change_region_text_feild", raise_e=False)

    def test_06_verify_contact_us_call_agent_option(self):
        """
        C53150729
        Description : Verify the behavior of Contact Us call agent option
        Install and launch app.
        Sign in and add printer.    
        Navigate to Printer detail page.
        Tap on 'Contact Us' button under Get help card
        Tap on the drop down to change the support region option6.
        Observe the behavior
        Expected Result: Verify the dropdown menu content behavior & call agent option

        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("hpx_contact_us_arrow", click_obj=True)
        self.driver.click("_shared_str_ok")
        assert self.driver.wait_for_object(
            "hpx_support_call_agent", raise_e=False)

    def test_07_Verify_warrantystatusActive(self):
        """
        C44018810

        Description : Verify the behavior of Warranty Status Active

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Scroll down to Product Information section
        Tap on the arrow next to Warranty Status
        Expected Result: The Factory warranty screen shows after clicking the arrow next to Warranty Status.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("warranty_status", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.support.verify_warranty_status()

    def test_08_verify_warranty_status_unknown(self):
        """C51966007
        Description : Verify the behavior of Warranty Status Unknown
        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Scroll down to Product Information section
        Tap on the arrow next to Warranty Status
        Expected Result: The Factory warranty screen shows after clicking the arrow next to Warranty Status.

        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("warranty_status", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.support.verify_warranty_status()

    def test_09_verify_subscriptions_status_arrow_link(self):
        """
        C51907640

        Description : Verify the behavior of Subscription Status Arrow Link
        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Scroll down to Product Information section
        Tap on the arrow next to Subscription Status

        Expected Result: The Factory subscription screen shows after clicking the arrow next to Subscription Status.

        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.home.click_avatar_btn()
        self.home.verify_hpx_subscription_btn()
        self.driver.click("hpx_subscription_btn")

    def test_10_verify_support_option_No_devices_added(self):
        """
        C42242136

        Description : Verify the behavior of Support Option No devices added
        Install and launch app.
        Skip Sign in and navigate to root view.
        Tap on avatar from top bar
        Tap on Support from side flyout screen.
        Observe.
        Expected Result: The Support screen shows with the message "No devices added" and the "Add Printer" button.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_avatar_btn()
        self.profile.click_support_link()
        self.profile.click_goto_hp_support()

    def test_11_verify_support_option_devices_added(self):
        """
        C53188238
        Description : Verify the behavior of Support Option Devices added

        Install and launch app.
        Skip Sign in and add printer.
        Navigate to Printer detail page.
        Tap on avatar from top bar
        Tap on Support from side flyout screen.
        Observe.
        Expected Result: The Support page opens showing all the added devices on screen
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_avatar_btn()
        self.profile.click_support_link()
        self.profile.click_goto_hp_support()

    def test_12_verify_navigation_from_support_to_get_help_card_page(self):
        """
        C53188383
        Description : Verify the behavior of Navigation from Support to Get Help Card page

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on avatar from top bar
        Tap on Support from side flyout screen.
        Observe.

        Expected Result: The Support page opens showing the get help card screen
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.home.click_avatar_btn()
        self.home.click_hpx_support_btn()
        self.support.verify_hpx_support_card_printers()
        self.driver.swipe()
        self.driver.scroll("hpx_get_help_card", click_obj=True)

    def test_13_verify_support_option_to_navigate_webpage(self):
        """
        C53221043
        Description : Verify the behavior of Support Option to navigate webpage

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on avatar from top bar
        Tap on Support from side flyout screen.
        Observe.
        Expected Result: The Support page opens showing all the added devices on screen
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.home.click_avatar_btn()
        self.home.click_hpx_support_btn()
        self.support.click_Go_to_support_hp_web()
