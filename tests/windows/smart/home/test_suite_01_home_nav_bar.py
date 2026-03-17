import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_01_Home_NavBar(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session

        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.feedback = cls.fc.fd["feedback"]
        cls.about = cls.fc.fd["about"]
        cls.privacy_settings = cls.fc.fd["privacy_settings"]
        cls.printers = cls.fc.fd["printers"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]

        cls.stack = request.config.getoption("--stack")

    def test_01_check_nav_bar(self):
        """
        Verify navigation pane shows on the very far left side.
        Verify navigation pane closes after clicking on the hamburger btn again.
        Click on the Hamburger icon, verify functionality 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890696
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14721522
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14721521
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/16977319
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14721552
        """    
        self.fc.go_home()

        self.home.menu_expansion(expand=True)
        assert self.home.navbar_menu_expand() is True
        self.home.verify_navigation_pane_split_view()

        self.home.menu_expansion(expand=False)
        assert self.home.navbar_menu_expand() is False

    def test_02_check_home_icon(self):
        """
        Verify app stays on main page after clicking home icon on the navigation pane.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890697
        """    
        self.home.select_home_btn()
        assert self.home.navbar_menu_expand() is False

    def test_03_hover_hamburger_icon(self):
        """
        Hover over the Hamburger icon, verify it changes to grey background 	

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14721520
        """   
        self.home.hover_hamburger_icon()
        actual_img = saf_misc.load_image_from_base64(self.driver.screenshot_element('left_menu_btn'))
        hamburger_icon_hover_img = saf_misc.load_image_from_file(ma_misc.get_abs_path(w_const.TEST_DATA.IMAGE_PATH + 'hamburger_icon_hover.png'))
        assert saf_misc.img_comp(actual_img, hamburger_icon_hover_img) < 0.01

    @pytest.mark.parametrize("buttons", ["create_account", "sign_in"])
    def test_04_check_sign_in_up_page(self, buttons):
        """
        Verify HPID login dialog opens to Sign in screen by clicking on "Sign in" in the fly out page.
        Click "X" button on the HPID Sign in/Create account dialog, verify user navigates to the Home page
        Verify HPID login dialog opens to Create Account screen by clicking on "Create Account" in the fly out page.
        Click "X" button on the HPID Sign in/Create account dialog, verify user navigates to the Home page
        Check person icon on main UI, verify person icon is moved from shell title bar to the navigation pane 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28390113
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/28217256
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27997912
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/28390114
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27997912
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/16932016
        """
        if buttons == "sign_in":
            self.home.select_sign_in_btn()
            self.fc.verify_hp_id_sign_in_up_page()
        else:
            self.home.select_create_account_btn()
            self.fc.verify_hp_id_sign_in_up_page(is_sign_up=True)

        self.fc.close_hp_id_sign_in_up_page()

    def test_05_check_device_picker(self):
        """
        Verify Device Picker opens after clicking the + button.
        Verify home page shows after clicking back arrow on the screen.
        Check small + icon, verify is moved from shell title bar to the navigation pane and name updated with "Add/Setup a Printer"

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17212352
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/16942939
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/16977320
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/16932002
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/16932003
        """
        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen()
        self.home.select_navbar_back_btn()

    def test_06_check_app_settings(self):
        """
        Verify Settings section opens in nav pane after clicking the setting icon.
        Verify 5 Menu items listed in Settings.
        Verify "Personalize Tiles" option is added under the app settings list
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890700
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14721529
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/16932006
        """
        self.home.select_app_settings_btn()
        self.home.verify_app_settings_pane()

    def test_07_check_send_feedback(self):
        """
        Verify user is taken to Feedback screen.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14721543
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/15142449
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541069
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14721570
        """
        self.home.select_send_feedback_listview()
        self.feedback.verify_feedback_screen()
        self.home.select_navbar_back_btn()

    def test_08_check_privacy_settings(self):
        """
        Verify "Privacy Settings" page opens within the app.
        Account deletion : User is not able to delete app data if not signed in

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17451355
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/31463283
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14721564
        """
        self.home.select_app_settings_btn()
        self.home.verify_app_settings_pane()
        self.home.select_privacy_settings_listview()
        self.privacy_settings.verify_privacy_settings_screen()
        self.home.select_navbar_back_btn()

