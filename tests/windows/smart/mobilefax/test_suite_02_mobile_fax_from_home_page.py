import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
from selenium.common.exceptions import NoSuchElementException


pytest.app_info = "GOTHAM"
class Test_Suite_02_Mobile_Fax_From_Home_Page(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.scan = cls.fc.fd["scan"]
        cls.print = cls.fc.fd["print"]
        cls.ows_ucde_value_prop = cls.fc.fd["ows_value_prop"]
        cls.mobile_fax = cls.fc.fd["softfax_home"]
        cls.softfax_landing = cls.fc.fd["softfax_landing"]
        cls.softfax_welcome = cls.fc.fd["softfax_welcome"]
        cls.softfax_offer = cls.fc.fd["softfax_offer"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)


    def test_01_go_to_mobile_fax_langding_page(self):
        """
        Click "Mobile Fax" tile
        Do sign in/ sign up on value prompt screen.
        verify mobile fax landing page shows with "Get Started" button
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17149720   
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17149717
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        if self.driver.session_data["request"].config.getoption("--stack") == "production":
            self.home.enable_logging()
        self.home.select_mobile_fax_tile()
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()
        self.ows_ucde_value_prop.select_native_value_prop_buttons(index=0)
        self.fc.verify_hp_id_sign_in_up_page(is_sign_up=True)
        self.fc.handle_web_login(create_account=True)
        self.softfax_landing.verify_mobile_fax_landing_screen()

    def test_02_go_to_mobile_fax_langding_page(self):
        """
        Click "Get Started" button on mobile fax value prompt screen.
        Click the Check box on the agreement screen
        Click Yes/No radio button  
        Click on "Continue" button on the Business Associate Agreement screen.
        Checkbox and then click on "Back" button on the Business Associate Agreement screen
        Click Back arrow (win) / Home icon (mac) on the shell title bar/Title bar
        Verify "Mobile Fax" agreement page shows 
        verify the "Continue" button get enabled and the user can continue the flow
        Verify the "Compose Fax" screen shows
        Verify the user navigates to the main UI.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30163156 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/16861533   
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/16861534
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30163154
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/25338897
        """
        self.softfax_landing.select_get_started_btn()
        self.softfax_welcome.verify_your_trial_starts_screen()
        self.softfax_welcome.verify_continue_btn_is_disabled()
        self.softfax_welcome.skip_welcome_screen(True)
        self.softfax_offer.verify_business_associate_agreement_screen()
        self.softfax_offer.click_back_btn()
        self.softfax_welcome.verify_your_trial_starts_screen()
        self.softfax_welcome.skip_welcome_screen(is_fist_time=False)
        self.mobile_fax.verify_mobile_fax_home_screen()
        self.home.select_navbar_back_btn()
        self.home.verify_home_screen()

    def test_03_select_each_type_of_supported_file(self):
        """
        Click "Mobile Fax" tile on the Main UI
        Click on "File & Photos" option on the Compose Fax screen
        Select each type of file
        
        Verify "Sent" screen with the string 
        "You haven't sent any faxes yet Click on "Compose Fax" above to send a Fax!"
        Verify file picker opens.
        Verify supported file types pdf, jpeg, & PNG shows on the file picker
        Verify the user can select all the supported file type.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/16861538
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/16861539 
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30163155  
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17320139
        """
        self.home.select_mobile_fax_tile()
        self.mobile_fax.verify_mobile_fax_home_screen()
        self.mobile_fax.verify_no_faxes_yet()
        self.mobile_fax.select_compose_fax_menu()
        for file_type in [w_const.TEST_DATA.FISH_PNG, w_const.TEST_DATA.COLOR_PDF, w_const.TEST_DATA.WORM_JPEG]:
            self.mobile_fax.click_add_files_option_btn(self.mobile_fax.FILES_PHOTOS_BTN)
            self.print.input_file_name(file_type)
            self.mobile_fax.verify_add_files_successfully()
            self.mobile_fax.click_trash_icon()

    def test_04_click_scanner_opt(self):
        """
        Click on "Scanner" option on the Compose Fax screen
        Go to the scan preview screen
        Verify Scan intro page opens with the all available scan option 
        Verify button title shows as "Continue to Fax" 
        after adding a scan job from the compos fax experience.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/16861540
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17464751   
        """
        self.mobile_fax.click_add_files_option_btn(self.mobile_fax.SCANNER_BTN)
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.verify_scanner_screen()
        self.scan.click_scan_btn()
        self.scan.verify_continue_to_fax_btn_display()

    def test_05_check_gotham_log(self):
        """
        Check Gotham log 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17491195  
        """
        event_msg = '"callback_schema":"hpsmart://softfax/"'
        self.fc.check_gotham_log(event_msg)
    