import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from SAF.misc import saf_misc
from SAF.misc import windows_utils
import pytest
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities



pytest.app_info = "HPX"
class Test_Suite_HP_Privacy(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        re = RegistryUtilities(cls.driver.ssh)
        return re

    
    def test_01_click_yes_to_all_btn_C32613386(self, install_app):

        self.fc.turn_on_hp_privacy_page(self.driver.ssh)

        self.fc.re_install_app(install_app)
        time.sleep(3)
        self.fc.launch_app()
        time.sleep(3)
        self.fc.click_login_page()
        time.sleep(3)
        
        self.fc.fd["hp_privacy_setting"].click_manage_options_button()
        time.sleep(2)


        self.fc.fd["hp_privacy_setting"].click_yes_to_all()
        time.sleep(2)
        warranty_status = self.driver.wait_for_object("warranty_consent_yes_button").get_attribute("SelectionItem.IsSelected")
        assert warranty_status == "true"
        time.sleep(2)
        sysinfo_status = self.driver.wait_for_object("sysinfo_consent_yes_button").get_attribute("SelectionItem.IsSelected")
        assert sysinfo_status == "true"
        time.sleep(2)
        marketing_status = self.driver.wait_for_object("marketing_consent_yes_button").get_attribute("SelectionItem.IsSelected")
        assert marketing_status == "true"
        time.sleep(2)
        self.fc.fd["hp_privacy_setting"].click_done_button()
        time.sleep(2)

        assert self.fc.fd["hp_registration"].verify_hp_registration_show() is True
    
    def test_02_set_all_consent_accepted_C32019446(self, install_app, class_setup):

        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Accepted") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Accepted")
        time.sleep(2)
        
        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Accepted") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Accepted")
        time.sleep(2)
        
        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        time.sleep(2)

        self.fc.re_install_app(install_app)
        time.sleep(3)
        self.fc.launch_app()
        time.sleep(3)

        self.fc.click_login_page()
        time.sleep(2)

        assert  self.fc.fd["hp_privacy_setting"].verify_hp_privacy_show() is False
        time.sleep(2)

        assert class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Accepted") is True
        assert class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Accepted") is True
        assert class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted") is True
    
    def test_03_set_all_consent_rejected_C32019447(self, install_app, class_setup):

        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Rejected") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Rejected")
        
        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Rejected") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Rejected")
        
        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")

        self.fc.re_install_app(install_app)
        time.sleep(3)
        self.fc.launch_app()
        time.sleep(3)
        self.fc.click_login_page()
        time.sleep(2)
        
        assert self.fc.fd["hp_privacy_setting"].verify_hp_privacy_show() is False
    

    def test_04_click_decline_all_btn_C32023564(self, install_app):

        self.fc.turn_on_hp_privacy_page(self.driver.ssh)

        self.fc.re_install_app(install_app)
        time.sleep(5)
        self.fc.launch_app()
        time.sleep(5)
        self.fc.click_login_page()
        time.sleep(2)
        
        self.fc.fd["hp_privacy_setting"].click_decline_all_button()

        assert self.fc.fd["hp_registration"].verify_hp_registration_show() is True

    def test_05_click_accept_all_btn_C32023455(self, install_app):

        self.fc.turn_on_hp_privacy_page(self.driver.ssh)

        self.fc.re_install_app(install_app)
        time.sleep(5)
        self.fc.launch_app()
        time.sleep(5)
        self.fc.click_login_page()
        time.sleep(2)
        
        self.fc.fd["hp_privacy_setting"].click_accept_all_button()

        assert self.fc.fd["hp_registration"].verify_hp_registration_show() is True

    def test_06_click_manage_options_btn_C32023567(self, install_app):

        self.fc.turn_on_hp_privacy_page(self.driver.ssh)

        self.fc.re_install_app(install_app)
        time.sleep(5)
        self.fc.launch_app()
        time.sleep(5)
        self.fc.click_login_page()
        time.sleep(2)
        
        self.fc.fd["hp_privacy_setting"].click_manage_options_button()
        time.sleep(2)
        assert self.fc.fd["hp_privacy_setting"].vreify_yes_to_all_btn() is True
    
    def test_07_set_all_consent_unknown_accepted_C32009392(self, install_app, class_setup):

        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Unknown") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Unknown")
        time.sleep(2)
        
        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Accepted") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Accepted")
        time.sleep(2)
        
        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        time.sleep(2)

        self.fc.re_install_app(install_app)
        time.sleep(3)
        self.fc.launch_app()
        time.sleep(3)

        self.fc.click_login_page()
        time.sleep(2)

        assert  self.fc.fd["hp_privacy_setting"].verify_hp_privacy_show() is True
    
    def test_08_set_all_consent_1rejected_2accepted_C32019450(self, install_app, class_setup):

        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Accepted") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Accepted")
        time.sleep(2)
        
        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Accepted") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Accepted")
        time.sleep(2)
        
        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        time.sleep(2)

        self.fc.re_install_app(install_app)
        time.sleep(3)
        self.fc.launch_app()
        time.sleep(3)

        self.fc.click_login_page()
        time.sleep(2)

        assert  self.fc.fd["hp_privacy_setting"].verify_hp_privacy_show() is False
    
    def test_09_set_all_consent_2rejected_1accepted_C32019452(self, install_app, class_setup):

        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Accepted") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Accepted")
        time.sleep(2)
        
        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Rejected") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Rejected")
        time.sleep(2)
        
        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        time.sleep(2)

        self.fc.re_install_app(install_app)
        time.sleep(3)
        self.fc.launch_app()
        time.sleep(3)

        self.fc.click_login_page()
        time.sleep(2)

        assert  self.fc.fd["hp_privacy_setting"].verify_hp_privacy_show() is False
    
    def test_10_set_all_consent_1unknown_2rejected_C32610252(self, install_app, class_setup):

        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Unknown") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Unknown")
        time.sleep(2)
        
        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Rejected") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Rejected")
        time.sleep(2)
        
        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        time.sleep(2)

        self.fc.re_install_app(install_app)
        time.sleep(3)
        self.fc.launch_app()
        time.sleep(3)

        self.fc.click_login_page()
        time.sleep(2)

        assert  self.fc.fd["hp_privacy_setting"].verify_hp_privacy_show() is True
    
    def test_11_set_all_consent_3unknown_C32610253(self, install_app, class_setup):

        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Unknown") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Unknown")
        time.sleep(2)
        
        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Unknown") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Unknown")
        time.sleep(2)
        
        if class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Unknown") is False:
            class_setup.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Unknown")
        time.sleep(2)

        self.fc.re_install_app(install_app)
        time.sleep(3)
        self.fc.launch_app()
        time.sleep(3)

        self.fc.click_login_page()
        time.sleep(2)

        assert  self.fc.fd["hp_privacy_setting"].verify_hp_privacy_show() is True
