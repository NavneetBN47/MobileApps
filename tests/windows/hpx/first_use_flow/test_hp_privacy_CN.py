import time
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities



pytest.app_info = "HPX"
class Test_Suite_HP_Privacy_CN(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.re = RegistryUtilities(cls.driver.ssh)

    
    def test_01_set_all_consent_accepted_C32019454(self):
        registry_path = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent"

        registry_list = [["AllowProductEnhancement", "Accepted"], ["AllowMarketing", "Accepted"], ["AllowSupport", "Accepted"], ["AllowTransferOutOfCountry", "Accepted"]]

        self.fc.set_privacy_consents(registry_path, registry_list)

        self.fc.re_install_app_and_skip_login_page(self.driver.session_data["installer_path"])
        time.sleep(2)

        assert  bool(self.fc.fd["hp_privacy_setting_cn"].verify_hp_privacy_show()) is False
    
    def test_02_set_all_consent_rejected_C32019455(self):
        registry_path = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent"

        registry_list = [["AllowProductEnhancement", "Rejected"], ["AllowMarketing", "Rejected"], ["AllowSupport", "Rejected"], ["AllowTransferOutOfCountry", "Rejected"]]

        self.fc.set_privacy_consents(registry_path, registry_list)

        self.fc.re_install_app_and_skip_login_page(self.driver.session_data["installer_path"])
        time.sleep(2)
        
        assert  bool(self.fc.fd["hp_privacy_setting_cn"].verify_hp_privacy_show()) is False
    
    def test_03_set_transfer_yes_other_no_C32019457(self):
        registry_path = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent"

        registry_list = [["AllowProductEnhancement", "Rejected"], ["AllowMarketing", "Rejected"], ["AllowSupport", "Rejected"], ["AllowTransferOutOfCountry", "Accepted"]]

        self.fc.set_privacy_consents(registry_path, registry_list)

        self.fc.re_install_app_and_skip_login_page(self.driver.session_data["installer_path"])
        time.sleep(2)
        
        assert  bool(self.fc.fd["hp_privacy_setting_cn"].verify_hp_privacy_show()) is False

    
    def test_04_set_transfer_no_other_yes_C32019463(self):
        registry_path = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent"

        registry_list = [["AllowProductEnhancement", "Accepted"], ["AllowMarketing", "Accepted"], ["AllowSupport", "Accepted"], ["AllowTransferOutOfCountry", "Rejected"]]

        self.fc.set_privacy_consents(registry_path, registry_list)

        self.fc.re_install_app_and_skip_login_page(self.driver.session_data["installer_path"])
        time.sleep(2)
        
        assert  bool(self.fc.fd["hp_privacy_setting_cn"].verify_hp_privacy_show()) is False
    
    def test_05_set_transfer_no_other_yes_and_no_C32009383(self):
        registry_path = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent"

        registry_list = [["AllowProductEnhancement", "Rejected"], ["AllowMarketing", "Accepted"], ["AllowSupport", "Accepted"], ["AllowTransferOutOfCountry", "Rejected"]]

        self.fc.set_privacy_consents(registry_path, registry_list)

        self.fc.re_install_app_and_skip_login_page(self.driver.session_data["installer_path"])
        time.sleep(2)
        
        assert  bool(self.fc.fd["hp_privacy_setting_cn"].verify_hp_privacy_show()) is False
    
    def test_06_set_transfer_no_1_unknown_other_yes_C32021442(self):
        registry_path = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent"

        registry_list = [["AllowProductEnhancement", "Unknown"], ["AllowMarketing", "Accepted"], ["AllowSupport", "Accepted"], ["AllowTransferOutOfCountry", "Accepted"]]

        self.fc.set_privacy_consents(registry_path, registry_list)

        self.fc.re_install_app_and_skip_login_page(self.driver.session_data["installer_path"])
        time.sleep(2)
        
        assert  bool(self.fc.fd["hp_privacy_setting_cn"].verify_hp_privacy_show()) is True

    
    def test_07_set_transfer_unknown_other_yes_C32019471(self):
        registry_path = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent"

        registry_list = [["AllowProductEnhancement", "Accepted"], ["AllowMarketing", "Accepted"], ["AllowSupport", "Accepted"], ["AllowTransferOutOfCountry", "Unknown"]]

        self.fc.set_privacy_consents(registry_path, registry_list)

        self.fc.re_install_app_and_skip_login_page(self.driver.session_data["installer_path"])
        time.sleep(2)
        
        assert self.fc.fd["hp_privacy_setting_cn"].verify_hp_privacy_show() is True
    
    def test_08_set_transfer_unknown_other_no_C32607498(self):
        registry_path = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent"

        registry_list = [["AllowProductEnhancement", "Rejected"], ["AllowMarketing", "Rejected"], ["AllowSupport", "Rejected"], ["AllowTransferOutOfCountry", "Unknown"]]

        self.fc.set_privacy_consents(registry_path, registry_list)

        self.fc.re_install_app_and_skip_login_page(self.driver.session_data["installer_path"])
        time.sleep(2)
        
        assert  bool(self.fc.fd["hp_privacy_setting_cn"].verify_hp_privacy_show()) is True

    def test_09_set_transfer_unknown_other_yes_and_no_C32021441(self):
        registry_path = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent"

        registry_list = [["AllowProductEnhancement", "Rejected"], ["AllowMarketing", "Accepted"], ["AllowSupport", "Accepted"], ["AllowTransferOutOfCountry", "Unknown"]]

        self.fc.set_privacy_consents(registry_path, registry_list)

        self.fc.re_install_app_and_skip_login_page(self.driver.session_data["installer_path"])
        time.sleep(2)
        
        assert  bool(self.fc.fd["hp_privacy_setting_cn"].verify_hp_privacy_show()) is True
    
    def test_10_set_transfer_unknown_other_no_and_yes_C32607512(self):
        registry_path = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent"

        registry_list = [["AllowProductEnhancement", "Accepted"], ["AllowMarketing", "Rejected"], ["AllowSupport", "Rejected"], ["AllowTransferOutOfCountry", "Unknown"]]

        self.fc.set_privacy_consents(registry_path, registry_list)

        self.fc.re_install_app_and_skip_login_page(self.driver.session_data["installer_path"])
        time.sleep(2)
        
        assert  bool(self.fc.fd["hp_privacy_setting_cn"].verify_hp_privacy_show()) is True


    def test_11_set_transfer_unknown_other_yes_and_unknown_C32607480(self):
        registry_path = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent"

        registry_list = [["AllowProductEnhancement", "Unknown"], ["AllowMarketing", "Accepted"], ["AllowSupport", "Accepted"], ["AllowTransferOutOfCountry", "Unknown"]]

        self.fc.set_privacy_consents(registry_path, registry_list)

        self.fc.re_install_app_and_skip_login_page(self.driver.session_data["installer_path"])
        time.sleep(2)
        
        assert  bool(self.fc.fd["hp_privacy_setting_cn"].verify_hp_privacy_show()) is True

    def test_12_set_transfer_unknown_other_no_and_unknown_C32607513(self):
        registry_path = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent"

        registry_list = [["AllowProductEnhancement", "Unknown"], ["AllowMarketing", "Rejected"], ["AllowSupport", "Rejected"], ["AllowTransferOutOfCountry", "Unknown"]]

        self.fc.set_privacy_consents(registry_path, registry_list)

        self.fc.re_install_app_and_skip_login_page(self.driver.session_data["installer_path"])
        time.sleep(2)
        
        assert  bool(self.fc.fd["hp_privacy_setting_cn"].verify_hp_privacy_show()) is True
