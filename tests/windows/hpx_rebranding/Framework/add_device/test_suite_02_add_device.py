import pytest

from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
 
pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
 
@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_02_Add_Device(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.web_driver = utility_web_session
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        cls.profile= request.cls.fc.fd["profile"]
        cls.add_device= request.cls.fc.fd["add_device"]
        request.cls.devicesMFE = cls.fc.fd["devicesMFE"]
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.profile.minimize_chrome()

    @pytest.mark.regression
    def test_01_verify_device_add_via_product_number_C55687272(self):
        self.devicesMFE.click_home_loggedin()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.verify_add_device_button()
        self.profile.click_add_device_button()
        assert self.add_device.verify_add_device_page(), "Add device page is not displayed"
        assert self.add_device.verify_search_by_serial_number_btn(), "search by serial number button not found"
        self.add_device.click_search_by_serial_number_btn()
        self.add_device.input_enter_serial_number("8CC5281Y49")
        entered_value = self.add_device.get_entered_serial_number()
        assert entered_value == "8CC5281Y49", f"Serial number not displayed correctly, found: {entered_value}"  
        assert self.add_device.verify_product_number_textbox(), "Product number textbox not found"  
        self.add_device.input_enter_product_number("9U886PA#ACJ")
        entered_value = self.add_device.get_entered_product_number()
        assert entered_value == "9U886PA#ACJ", f"Product number not displayed correctly, found: {entered_value}"  
        self.add_device.click_add_device_hyperlink()
        assert self.add_device.verify_newly_added_devicename(), "Newly added device name is not displayed"
 
    @pytest.mark.regression
    def test_02_verify_device_addition_via_serial_number_C55687266(self):
        self.devicesMFE.click_home_loggedin()
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.verify_add_device_button()
        self.profile.click_add_device_button()
        assert self.add_device.verify_add_device_page(), "Add device page is not displayed"
        assert self.add_device.verify_search_by_serial_number_btn(), "search by serial number button not found"
        self.add_device.click_search_by_serial_number_btn()
        self.add_device.input_enter_serial_number("8CC5281Y49")
        entered_value = self.add_device.get_entered_serial_number()
        assert entered_value == "8CC5281Y49", f"Serial number not displayed correctly, found: {entered_value}"  
        self.add_device.click_add_device_hyperlink()
        assert self.add_device.verify_newly_added_devicename(), "Newly added device name is not displayed"
 
 

 

   