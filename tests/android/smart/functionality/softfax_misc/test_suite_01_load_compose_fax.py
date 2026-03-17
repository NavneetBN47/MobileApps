import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.resources.const.android.const import WEBVIEW_CONTEXT, WEBVIEW_URL

pytest.app_info = "SMART"


class Test_Suite_01_Load_Compose_Fax(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.hpid = cls.fc.flow[FLOW_NAMES.HPID]
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.softfax_welcome = cls.fc.flow[FLOW_NAMES.SOFTFAX_WELCOME]
        cls.app_settings = cls.fc.flow[FLOW_NAMES.APP_SETTINGS]
        cls.vallue_prop = cls.fc.flow[FLOW_NAMES.OWS_VALUE_PROP]
        cls.ucde = cls.fc.flow[FLOW_NAMES.UCDE_PRIVACY]
        cls.chrome = cls.fc.flow[FLOW_NAMES.GOOGLE_CHROME]
        cls.fax_history =cls.fc.flow[FLOW_NAMES.SOFTFAX_FAX_HISTORY]
        cls.softfax_offer = cls.fc.flow[FLOW_NAMES.SOFTFAX_OFFER]
        cls.smb = cls.fc.flow[FLOW_NAMES.SMB]
        cls.smart_context = cls.fc.smart_context
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)

    def test_01_load_compose_fax_by_login_via_app_settings(self):
        """
            Description:
                1/ Enable Mobile Fax tile
                2/ Login to HPID in App Settings
                3/ Click on Send Fax tile on Home screen
            Expected Result:
                3/ Compose Fax screen display
        """
        self.fc.flow_home_load_compose_fax_screen(create_acc=False)

    def test_02_load_compose_fax_by_login_via_tile(self):
        """
        Precondition: App is not login to any accounts
        Description:
            1/ Enable Mobile Fax tile
            2/ Click on Mobile Fax at Home screen
            3/ Click on Sign In button on Value Prop screen
            4/ Log in into a HPID account
            5/ Dismiss App Permision
            6/ Load Home screen again-> go to App Settings.        
        Expected Result:
            4/ App Permission display
            5/ Compose Fax screen
            6/ HPID is logged in
        """
        # Make sure compose fax screen is empty, not affect by previous test suite
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.flow_home_enable_softfax_tile()
        self.home.select_tile_by_name(self.driver.return_str_id_value(TILE_NAMES.FAX))
        self.driver.wait_for_context(self.smart_context, timeout=20)
        self.vallue_prop.verify_ows_value_prop_screen(tile=True)
        self.vallue_prop.select_secondary_btn(change_check=True, timeout=10)
        self.chrome.handle_welcome_screen_if_present()
        self.driver.wait_for_context(WEBVIEW_CONTEXT.CHROME)
        self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        if self.smb.select_my_printers(raise_e=False):
            self.smb.select_continue()
        #Todo: wait for designer's reply on timeout after signing into HPID account
        self.home.check_run_time_permission(accept=True, timeout=10)
        self.driver.wait_for_context(WEBVIEW_URL.SOFTFAX, timeout=30)
        self.compose_fax.click_fax_feature_update_dismiss_btn(raise_e=False)
        self.fax_history.verify_fax_history_screen()

    def test_03_load_compose_fax_by_creating_account_via_app_settings(self):
        """
            Description: C35076251
                1/ Enable Send Fax tile and Change stack
                2/ Create a HPID account in App Settings
                3/ Click on Send Fax tile on Home screen
            Expected Result:
                3/ Compose Fax screen display
        """
        self.fc.flow_home_load_compose_fax_screen(create_acc=True)