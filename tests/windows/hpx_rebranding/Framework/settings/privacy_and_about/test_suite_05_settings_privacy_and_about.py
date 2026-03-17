import pytest
from requests import request
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_05_Settings_Privacy_And_About(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.css = request.cls.fc.fd["css"]
        yield
        request.cls.fc.consent_managed_registry_key(request.cls.driver.ssh, condition=False)
        request.cls.fc.consent_allow_support(request.cls.driver.ssh, condition=False)
        request.cls.fc.app_managed_registry_key(request.cls.driver.ssh, condition=False)

    @pytest.mark.regression                     
    def test_01_verify_app_pc_consents_not_shown_during_fuf_managed_C60498994(self):
        self.fc.consent_managed_registry_key(self.driver.ssh, condition=True)
        self.fc.consent_allow_support(self.driver.ssh,condition="Unknown")      
        self.fc.reset_myHP_app_through_command()
        self.fc.launch_myHP_and_skip_fuf()
        self.css.maximize_hp()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"

    @pytest.mark.regression
    def test_02_verify_managed_devices_functionality_C60498990(self):
        self.fc.consent_managed_registry_key(self.driver.ssh, condition=False)
        self.fc.app_managed_registry_key(self.driver.ssh, condition=True)
        self.fc.reset_myHP_app_through_command()
        self.fc.launch_myHP_and_skip_fuf()
        self.css.maximize_hp()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_profile_settings_btn(), "Profile settings button missing"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button is not displayed"
        self.hpx_settings.click_manage_privacy_btn()    
        self.hpx_settings.click_device_privacy_arrow_button()
        assert self.hpx_settings.get_computer_privacy_customer_support_toggle_state() == "ON", "customer support toggle should be ON after giving accept all consents"
        assert self.hpx_settings.get_computer_privacy_product_improvement_toggle_state() == "ON", "product improvement toggle should be ON after giving accept all consents"
        assert self.hpx_settings.get_computer_privacy_advertising_toggle_state() == "ON", "advertising toggle should be ON after giving accept all consents"

    @pytest.mark.regression  
    def test_03_managed_app_functionality_C60498988(self):
        self.fc.consent_managed_registry_key(self.driver.ssh, condition=True)
        self.fc.app_managed_registry_key(self.driver.ssh, condition=False)
        self.fc.reset_myHP_app_through_command()
        self.fc.launch_myHP_and_skip_fuf()
        self.css.maximize_hp()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_profile_settings_btn(), "Profile settings button missing"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_manage_privacy_btn(), "manage privacy settings button invisible"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_application_privacy_consents(), "Application privacy consents text is not displayed"
        assert self.hpx_settings.verify_device_privacy_text(), "Device privacy text is not displayed"
        assert self.hpx_settings.verify_product_improvement_toggle_is_clicked(), "Product improvement toggle is not clicked"
        assert self.hpx_settings.verify_advertising_toggle_is_clicked(), "Advertising toggle is not clicked"