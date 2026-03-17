import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_04_Potg_Printers_Enhancement(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        """
        Printer is remote
        Printer has Smart Driver capability
        Printer is not optimized
        Computer does not have smart driver installed
        User is HP+/UCDE
        """
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.printers = cls.fc.fd["printers"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.pepto = cls.fc.fd["pepto"]
        cls.scan = cls.fc.fd["scan"]

        cls.stack = request.config.getoption("--stack")
        if 'pie' in cls.stack:
            pytest.skip("Skip this test as there is no remote printer with a pie account")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

    def test_01_sign_in_to_add_a_remote_printer(self):
        """
        Add the remote printer
        Observe Main UI for status icon, Ink icon and Paper level Icon

        Verify the printer image display with Cloud icon.
        Verify ink status and paper status (if available).
        Verify the Cloud icons can be clickable.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14064642
        https://hp-testrail.external.hp.com/index.php?/cases/view/14072228
        """
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.fc.select_a_remote_printer()
        self.fc.enable_print_anywhere_dialog()
        self.home.select_paw_x_btn()
        assert self.home.verify_print_anywhere_dialog(raise_e=False) is False
        self.home.verify_printer_add_to_carousel()
        
    def test_02_verfiy_printer_status_tab_hidden(self):
        """
        Click on the status icon.

        Verify user is taken to Printer Information and that Printer Status tab is hidden.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14064643
        """
        self.home.click_carousel_printer_status_icon()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.verify_status_tile(is_remote=True)

    def test_03_check_private_pickup_combox_on_value(self):
        """
        Verify the Private Pickup combo box shows on the preview screen
        Verify the value in the combo box is 'required' if private pickup is on
        Verify the "optimize and print" button continues the print job.
        Verify the print job can be sent out successfully with "required" as the value in the private pickup combo box.
       
        https://hp-testrail.external.hp.com/index.php?/cases/view/28483722
        https://hp-testrail.external.hp.com/index.php?/cases/view/28469646
        https://hp-testrail.external.hp.com/index.php?/cases/view/28483724
        https://hp-testrail.external.hp.com/index.php?/cases/view/28483725
        """
        self.printer_settings.verify_print_anywhere_option_display()
        self.printer_settings.select_print_anywhere()
        self.printer_settings.verify_print_anywhere_screen()
        self.printer_settings.switch_private_pickup_toggle(toggle='on')
        self.printer_settings.switch_printing_anywhere_toggle(toggle='on')
        self.home.select_navbar_back_btn()
        self.__check_private_pickup_combo_box_flow(toggle='on')
        
    def test_04_check_private_pickup_combox_off_value(self):
        """
        Trigger remote print or IPP print when Privat Pickup combo box set to "Off"

        Verify the print job can be sent out successfully with "Off" as the value in the private pickup combo box.

        https://hp-testrail.external.hp.com/index.php?/cases/view/28483726
        """
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_print_anywhere_option_display()
        self.printer_settings.select_print_anywhere()
        self.printer_settings.verify_print_anywhere_screen()
        self.printer_settings.switch_private_pickup_toggle(toggle='on')
        self.printer_settings.switch_printing_anywhere_toggle(toggle='off')
        self.home.select_navbar_back_btn()
        self.__check_private_pickup_combo_box_flow(toggle='off')
        
    def test_05_click_cancel_print_button(self):
        """
        Verify "cancel print" button cancels out the flow and go to home page/scan (if from scan result screen).
        Verify the "optimize and print" button continues the print job.

        https://hp-testrail.external.hp.com/index.php?/cases/view/28389631 (#4 #5)
        """
        self.__via_print_documents_tile(toggle='off')
        self.print.select_dialog_cancel_print_btn()
        self.home.verify_home_screen()

    def test_06_restore_print_anywhere_toggle(self):
        """
        "Allow printing from Anywhere" toggle: On
        "Require Private Pickup" toggle: Off
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.home.select_printer_settings_tile()
        self.printer_settings.restore_print_anywhere_toggle()


    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __via_print_documents_tile(self, toggle):
        """
        Verify the UI matches design

        https://hp-testrail.external.hp.com/index.php?/cases/view/28469644 (#4 #5)
        """
        self.home.select_print_documents_tile()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.COLOR_PDF)
        self.print.verify_getting_remote_printer_status_text()
        self.print.check_private_pickup_box_value(toggle)
        self.print.verify_ipp_print_screen_btn_text(toggle)
        self.print.select_ipp_print_screen_print_btn()
        self.print.verify_optimize_for_faster_remote_printing_dialog()
        self.print.verify_sending_file_dialog()

    def __check_private_pickup_combo_box_flow(self, toggle):
        self.__via_print_documents_tile(toggle)
        self.print.select_dialog_optimize_and_print_btn()
        self.print.verify_sending_file_dialog()
        self.print.verify_file_send_dialog(timeout=120)
        self.print.select_dialog_ok_btn()
        self.home.verify_home_screen()
