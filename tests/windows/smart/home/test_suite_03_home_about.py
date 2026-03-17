import pytest
import datetime
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_03_Home_About(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session

        cls.home = cls.fc.fd["home"]
        cls.about = cls.fc.fd["about"]
        cls.stack = request.config.getoption("--stack")

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        def tab_clean_up():
            self.web_driver.close_window(self.web_driver.current_window)
        request.addfinalizer(tab_clean_up)


    def test_01_check_copyright_year(self):
        """
        Verify user is taken to "About" screen with current software version.
        Verify Correct Copyright year shows.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14721546
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14721572
        """
        self.fc.go_home()
        self.home.select_app_settings_btn()
        self.home.select_about_listview()
        self.about.verify_about_screen()

        current_year = datetime.datetime.now().year
        copyright_year = self.about.get_copyright_year()

        assert copyright_year == current_year

    def test_02_check_app_instance_id(self):
        """
        Add App instance id to about page
        Hover on APP Instance ID, check the tool tip message

        - Verify APP id displays with 10 characters and all in CAPS.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43091726
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/44453199
        """
        app_instance_id = self.about.get_app_instance_id()
        logging.info("App Instance Id: {}".format(app_instance_id))
        assert len(app_instance_id) == 10
        assert app_instance_id.isupper() == True

        self.about.click_app_id_copy_btn()
        self.about.verify_copied_tips_load()

        copied_app_instance_id = self.driver.get_clipboard_contents()
        assert app_instance_id == copied_app_instance_id.strip()

        self.about.hover_app_id_link()
        assert self.about.verify_copied_tips_load(raise_e=False) == False

        self.about.hover_app_id_copy_btn()
        actual_img = saf_misc.load_image_from_base64(self.driver.screenshot_element('app_id_copy_btn'))
        copy_icon_hover_img = saf_misc.load_image_from_file(ma_misc.get_abs_path(w_const.TEST_DATA.IMAGE_PATH + 'copy_icon_hover.png'))
        assert saf_misc.img_comp(actual_img, copy_icon_hover_img) < 0.01

    @pytest.mark.parametrize("webpage", ["PRIVACY", "EULA", "TOU"])
    def test_03_verify_links_on_about_page(self, webpage):
        """
        Verify the correct website opens after clicking the "HP Privacy" link.
        Verify the correct website opens after clicking the "End User License Agreement" link.
        Verify the correct website opens after clicking the "Term of USE" link.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27633155
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27633156
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27633157
            
        """
        webpage_links = {"PRIVACY": self.about.PRIVACY_LINK,
                 "EULA": self.about.EULA_LINK,
                 "TOU": self.about.TOU_LINK}
        
        webpage_urls = {"PRIVACY": self.about.PRIVACY_URL,
                "EULA": self.about.EULA_URL,
                "TOU": self.about.TOU_URL}

        self.about.click_link(webpage_links[webpage])
        self.web_driver.add_window(webpage)
        if webpage not in self.web_driver.session_data["window_table"].keys():
            self.about.click_link(webpage_links[webpage])
            self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)

        current_url = self.web_driver.get_current_url()

        for sub_url in webpage_urls[webpage]:
            assert sub_url in current_url

