import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
 
pytest.app_info = "HPX"
 
@pytest.mark.usefixtures("function_setup_myhp_launch")
class Test_Suite_01_Shortcuts(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.devicesMFE = cls.fc.fd["devicesMFE"]
        cls.devicesDetailsMFE = cls.fc.fd["devicesDetailsMFE"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.scan = cls.fc.fd["scan"]
        cls.p = load_printers_session
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.serial_number = cls.p.get_printer_information()['serial number']
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.devicesMFE.click_home_loggedin()
        cls.fc.sign_in(cls.user_name, cls.password, cls.web_driver, user_icon_click=False)
        cls.fc.add_a_printer(cls.p)
 
 
    @pytest.mark.regression
    def test_01_end_to_end_flow_create_new_shortcut_C50837281(self):
        self.devicesMFE.click_windows_dummy_printer(self.printer_name)
        self.devicesDetailsMFE.win_scroll_element("shortcuts_tile", direction="down")
        assert self.devicesDetailsMFE.verify_shortcuts_tile(), "Shortcuts tile is not displayed on printer details page."
        self.devicesDetailsMFE.click_shortcuts_tile()
        assert self.shortcuts.verify_add_new_shortcuts(), "Add new shortcuts screen is not displayed after clicking shortcuts tile."
        self.shortcuts.click_add_new_shortcuts()
        assert self.shortcuts.verify_create_your_own_shortcut(), "Create your own shortcut option is not displayed on add new shortcuts screen."
        self.shortcuts.click_create_your_own_shortcut()
        self.shortcuts.enter_shortcut_name("print_shortcut")
        assert self.shortcuts.verify_print_shortcut_btn(), "Save shortcut button is not displayed after entering shortcut name."
        self.shortcuts.click_print_shortcut_btn()
        self.driver.swipe(direction="down", distance=15)
        assert self.shortcuts.verify_save_btn(), "Save button is not present"
        self.shortcuts.click_save_btn()
        assert self.shortcuts.verify_you_just_created_a_shortcut_popup(), "You just created a Shortcut! popup is not displayed"

    @pytest.mark.regression
    def test_02_verify_delete_shortcut_confirmation_pop_up_C50837255(self):
        self.devicesMFE.click_windows_dummy_printer(self.printer_name)
        self.devicesDetailsMFE.click_shortcuts_tile()
        assert self.shortcuts.verify_add_new_shortcuts(),"Shortcuts list screen is not displayed."
        assert self.shortcuts.verify_edit_btn(),"Edit button is not displayed on shortcuts screen."
        self.shortcuts.click_edit_btn()
        assert self.shortcuts.verify_delete_icon(),"Delete icon is not displayed on shortcuts screen."
        self.shortcuts.click_delete_icon()
        assert self.shortcuts.verify_delete_cancel_popup(),"Delete confirmation popup is not displayed when user clicks cancel"
        self.shortcuts.click_delete_cancel_button()
        assert self.shortcuts.verify_add_new_shortcuts(),"Shortcuts list screen is not displayed"