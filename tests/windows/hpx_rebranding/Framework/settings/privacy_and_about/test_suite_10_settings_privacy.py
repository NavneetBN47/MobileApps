import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_10_Settings_Privacy(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.web_driver = utility_web_session
        request.cls.fc.kill_hpx_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]

    @pytest.mark.regression
    def test_01_verify_delete_account_link_logged_in_C59446404(self):
        self.devicesMFE.click_home_loggedin()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        user_initials = self.profile.get_user_initials_after_signin()
        assert user_initials in ("RG", "RP"), "User not signed in/credentials not matching"
        self.profile.click_top_profile_icon_signed_in()
        self.profile.click_profile_settings_btn()
        # Step 2: Navigate to Privacy settings
        logging.info("Navigated to Privacy settings.")
        # Step 3: Verify "Delete your Account" link is present
        assert self.hpx_settings.verify_delete_your_account_link(), "Delete your Account link is not present in Privacy settings."
        logging.info("Delete your Account link is present in Privacy settings.")