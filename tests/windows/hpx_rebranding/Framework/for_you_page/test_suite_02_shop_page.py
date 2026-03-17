import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_02_Shop_Page(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.web_driver = utility_web_session
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.bell_icon = request.cls.fc.fd["bell_icon"]
        cls.for_you_page = request.cls.fc.fd["for_you_page"]
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]

    @pytest.mark.regression
    def test_01_verify_shop_page_ui_after_signin_C60534016(self):
        assert self.devicesMFE.verify_bell_icon_show_up(), "Bell icon not visible on device details page"
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon not visible on device details page"
        assert self.device_card.verify_pc_devices_back_button(), "Device back button not visible"
        assert self.for_you_page.verify_shop_nav_pill(), "Shop nav pill not visible"
        self.for_you_page.click_shop_nav_pill()
        assert self.for_you_page.verify_create_account(), "Create account link not visible"
        assert self.for_you_page.verify_sign_in_btn(), "Sign in button not visible"
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        assert self.for_you_page.verify_top_recommended_for_you(), "Top recommended for you section not visible"
        self.driver.swipe(distance=10)
        assert self.for_you_page.verify_featured_offers(), "Featured offers section not visible"
        self.driver.swipe(distance=10)
        assert self.for_you_page.verify_shop_by_product(), "Shop by product section not visible"
        self.driver.swipe(distance=10)
        assert self.for_you_page.verify_looking_for_more(), "looking for more section invisible"
        assert self.for_you_page.verify_visit_hpcom(), "visit hp.com invisible"
