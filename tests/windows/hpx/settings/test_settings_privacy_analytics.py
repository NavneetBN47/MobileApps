import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from SAF.misc import saf_misc
from SAF.misc import windows_utils
import pytest
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from SAF.misc.ssh_utils import SSH
import logging

pytest.app_info = "HPX"
class Test_Suite_Settings_Privacy_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.ssh = SSH(request.config.getoption('--mobile-device'), "exec")
        cls.re = RegistryUtilities(cls.driver.ssh)



    def test_01_set_country_to_us_and_one_consent_to_yes_and_others_no_check_hpa_data_C32009389(self):
        self.fc.close_app()
        self.fc.launch_app()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.fd["settings"].click_privacy_tab()
        self.fc.fd["settings"].click_hp_privacy_settings()
        time.sleep(2)
        self.fc.fd["settings"].click_yes_to_all()
        time.sleep(2)
        warranty_status = self.driver.wait_for_object("warranty_consent_yes_button").get_attribute("SelectionItem.IsSelected")
        assert warranty_status == "true"
        time.sleep(2)
        self.fc.fd["settings"].click_sysinfo_no_button()
        sysinfo_status = self.driver.wait_for_object("sysinfo_consent_no_button").get_attribute("SelectionItem.IsSelected")
        assert sysinfo_status == "true"
        time.sleep(2)
        self.fc.fd["settings"].click_marketing_no_button()
        marketing_status = self.driver.wait_for_object("marketing_consent_no_button").get_attribute("SelectionItem.IsSelected")
        assert marketing_status == "true"
        time.sleep(2)
        self.fc.fd["settings"].click_done_button()
        time.sleep(2)
        initial_file_size = self.fc.get_analytics_file_size()
        logging.info("File Size of HPA :: {}".format(initial_file_size))

        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        time.sleep(2)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(2)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(2)
        audio_control_text = self.fc.fd["devices"].verify_audio_control()
        self.fc.fd["devices"].click_audio_control()
        self.fc.fd["devices"].click_pc_device_title_from_audio_title()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()

        file_size = self.fc.get_analytics_file_size()
        logging.info("File Size of HPA is updating as valid expected results :: {}".format(file_size))
        assert file_size > initial_file_size,"HPA data file is not updating"

    def test_02_set_country_to_us_and_two_consent_to_yes_and_others_no_check_hpa_data_C32021505(self):      
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.fd["settings"].click_privacy_tab()
        self.fc.fd["settings"].click_hp_privacy_settings()

        time.sleep(2)
        self.fc.fd["settings"].click_yes_to_all()
        time.sleep(5)
        warranty_status = self.driver.wait_for_object("warranty_consent_yes_button").get_attribute("SelectionItem.IsSelected")
        assert warranty_status == "true"
        time.sleep(2)
        self.fc.fd["settings"].click_sysinfo_no_button()
        sysinfo_status = self.driver.wait_for_object("sysinfo_consent_no_button").get_attribute("SelectionItem.IsSelected")
        assert sysinfo_status == "true"
        time.sleep(2)
        self.fc.fd["settings"].click_marketing_yes_button()
        marketing_status = self.driver.wait_for_object("marketing_consent_yes_button").get_attribute("SelectionItem.IsSelected")
        assert marketing_status == "true"
        time.sleep(2)
        self.fc.fd["settings"].click_done_button()
        time.sleep(2)
        initial_file_size = self.fc.get_analytics_file_size()
        logging.info("File Size of HPA :: {}".format(initial_file_size))

        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        time.sleep(2)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(2)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()
        self.fc.fd["devices"].click_audio_control()
        self.fc.fd["devices"].click_pc_device_title_from_audio_title()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()

        file_size = self.fc.get_analytics_file_size()
        logging.info("File Size of HPA is updating as valid expected results :: {}".format(file_size))
        assert file_size > initial_file_size,"HPA data file is not updating"

    def test_03_set_country_to_us_and_all_consent_to_yes_check_hpa_data_C32021506(self): 
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.fd["settings"].click_privacy_tab()
        self.fc.fd["settings"].click_hp_privacy_settings()

        time.sleep(2)
        self.fc.fd["settings"].click_yes_to_all()
        assert self.fc.fd["settings"].verify_yes_to_all_btn() is True
        time.sleep(2)
        self.fc.fd["settings"].click_done_button()
        time.sleep(2)
        initial_file_size = self.fc.get_analytics_file_size()
        logging.info("File Size of HPA :: {}".format(initial_file_size))

        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        time.sleep(2)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(2)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()
        self.fc.fd["devices"].click_audio_control()
        self.fc.fd["devices"].click_pc_device_title_from_audio_title()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()

        file_size = self.fc.get_analytics_file_size()
        logging.info("File Size of HPA is updating as valid expected results :: {}".format(file_size))
        assert file_size > initial_file_size,"HPA data file is not updating"


    def test_04_set_country_to_us_and_all_consent_to_no_check_hpa_data_C32021524(self):    
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.fd["settings"].click_privacy_tab()
        self.fc.fd["settings"].click_hp_privacy_settings()

        time.sleep(2)
        self.fc.fd["settings"].click_no_to_all()
        assert self.fc.fd["settings"].verify_no_to_all_btn() is True
        time.sleep(2)
        self.fc.fd["settings"].click_done_button()
        time.sleep(2)
        initial_file_size = self.fc.get_analytics_file_size()
        logging.info("File Size of HPA :: {}".format(initial_file_size))

        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        time.sleep(2)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(2)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()
        self.fc.fd["devices"].click_audio_control()
        self.fc.fd["devices"].click_pc_device_title_from_audio_title()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()

        file_size = self.fc.get_analytics_file_size()
        logging.info("File Size of HPA is not updating as valid expected results :: {}".format(file_size))
        assert file_size == initial_file_size,"HPA data file is getting updated"


    def test_05_set_country_to_us_and_two_consent_to_no_and_others_to_unknown_check_hpa_data_C32021532(self):
        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Unknown") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Unknown")
        time.sleep(2)

        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Rejected") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Rejected")
        time.sleep(2)

        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Rejected")
        time.sleep(2)

        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.fd["settings"].click_privacy_tab()
        self.fc.fd["settings"].click_hp_privacy_settings()   
        time.sleep(2)
        self.fc.fd["settings"].click_done_button()
        time.sleep(2)
        initial_file_size = self.fc.get_analytics_file_size()
        logging.info("File Size of HPA :: {}".format(initial_file_size))

        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        time.sleep(2)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(2)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()
        self.fc.fd["devices"].click_audio_control()
        self.fc.fd["devices"].click_pc_device_title_from_audio_title()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()

        file_size = self.fc.get_analytics_file_size()
        logging.info("File Size of HPA is not updating as valid expected results :: {}".format(file_size))
        assert file_size == initial_file_size,"HPA data file is getting updated"


    def test_06_set_country_to_us_and_two_consent_to_yes_and_others_to_unknown_check_hpa_data_C32610045(self): 
        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Accepted") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Accepted")
        time.sleep(2)

        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Unknown") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Unknown")
        time.sleep(2)

        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        time.sleep(2)

        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.fd["settings"].click_privacy_tab()
        self.fc.fd["settings"].click_hp_privacy_settings()   
        time.sleep(2)
        self.fc.fd["settings"].click_done_button()
        time.sleep(2)
        initial_file_size = self.fc.get_analytics_file_size()
        logging.info("File Size of HPA :: {}".format(initial_file_size))

        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        time.sleep(2)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(2)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()
        self.fc.fd["devices"].click_audio_control()
        self.fc.fd["devices"].click_pc_device_title_from_audio_title()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()

        file_size = self.fc.get_analytics_file_size()
        logging.info("File Size of HPA is updating as valid expected results :: {}".format(file_size))
        assert file_size > initial_file_size,"HPA data file is not updating"
        self.fc.close_app()

    def test_07_set_country_to_china_and_transfer_consent_to_unknown_and_others_to_yes_check_hpa_data_C32021534(self):
        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowTransferOutOfCountry", "Unknown") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowTransferOutOfCountry", "Unknown")
        time.sleep(2)   

        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Accepted") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Accepted")
        time.sleep(2)

        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Accepted") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Accepted")
        time.sleep(2)

        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        time.sleep(2)

        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "TransferOutConsentRequired", "True") is False:
            logging.info("Updating TransferOutConsentRequired")
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "TransferOutConsentRequired", "True")

        self.fc.launch_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.fd["settings"].click_privacy_tab()
        self.fc.fd["settings"].click_hp_privacy_settings() 
        self.driver.swipe(direction="down", distance=3)  
        time.sleep(2)
        self.fc.fd["settings"].click_done_button()
        time.sleep(2)       

        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        time.sleep(2)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(2)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()

        self.fc.fd["devices"].click_audio_control()
        self.fc.fd["devices"].click_pc_device_title_from_audio_title()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()  
        logging.info("Is file Exist "+ self.fc.is_analytics_file_exist())      
        assert "False" in self.fc.is_analytics_file_exist(),"HPA data file is exist"


    def test_08_set_country_to_china_and_transfer_consent_to_no_and_others_to_yes_check_hpa_data_C32021536(self):  
        self.fc.close_app()
        time.sleep(2)
        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowTransferOutOfCountry", "Rejected") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowTransferOutOfCountry", "Rejected")
        time.sleep(2)   

        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Accepted") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Accepted")
        time.sleep(2)

        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Accepted") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Accepted")
        time.sleep(2)

        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        time.sleep(2)

        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "TransferOutConsentRequired", "True") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "TransferOutConsentRequired", "True")

        self.fc.launch_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.fd["settings"].click_privacy_tab()
        self.fc.fd["settings"].click_hp_privacy_settings() 
        self.driver.swipe(direction="down", distance=3)  
        time.sleep(2)
        self.fc.fd["settings"].click_done_button()
        time.sleep(2)   

        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        time.sleep(2)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(2)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()
        self.fc.fd["devices"].click_audio_control()
        self.fc.fd["devices"].click_pc_device_title_from_audio_title()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()        
        assert "False" in self.fc.is_analytics_file_exist(),"HPA data file is exist"

    def test_09_set_country_to_china_and_transfer_consent_to_yes_and_others_to_yes_check_hpa_data_C32021540(self):  
        self.fc.close_app()
        time.sleep(2)
        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowTransferOutOfCountry", "Accepted") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowTransferOutOfCountry", "Accepted")
        time.sleep(2)   

        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Accepted") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Accepted")
        time.sleep(2)

        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Accepted") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Accepted")
        time.sleep(2)

        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted")
        time.sleep(2)

        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "TransferOutConsentRequired", "True") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "TransferOutConsentRequired", "True")

        self.fc.launch_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.fd["settings"].click_privacy_tab()
        self.fc.fd["settings"].click_hp_privacy_settings()
        self.driver.swipe(direction="down", distance=3)   
        time.sleep(2)
        self.fc.fd["settings"].click_done_button()
        time.sleep(2)
        initial_file_size = self.fc.get_analytics_file_size()
        logging.info("File Size of HPA :: {}".format(initial_file_size))

        text = self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        time.sleep(2)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(2)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()
        self.fc.fd["devices"].click_audio_control()
        self.fc.fd["devices"].click_pc_device_title_from_audio_title()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()        

        file_size = self.fc.get_analytics_file_size()
        logging.info("File Size of HPA is updating as valid expected results :: {}".format(file_size))
        assert file_size > initial_file_size,"HPA data file is not updating"

        time.sleep(2)      
        if self.re.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "TransferOutConsentRequired", "False") is False:
            self.re.update_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "TransferOutConsentRequired", "False")
        self.fc.close_app()    

    def test_10_stop_fuison_service_and_verify_review_retrieving_error_C32629334(self):
        self.fc.stop_hpanalytics_fusion_services()
        self.fc.stop_hpsysinfo_fusion_services()
        time.sleep(15)
        self.fc.launch_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.fd["settings"].click_privacy_tab()
        self.fc.fd["settings"].click_hp_privacy_settings()
        self.fc.fd["settings"].click_error_ok_button()
        self.fc.start_hpsysinfo_fusion_services()
        time.sleep(15)
        self.fc.fd["settings"].click_hp_privacy_settings()
        self.fc.fd["settings"].click_yes_to_all()
        self.fc.stop_hpsysinfo_fusion_services()
        self.fc.fd["settings"].click_hp_privacy_settings()
        self.fc.fd["settings"].click_yes_to_all()
        time.sleep(15)
        self.fc.start_hpsysinfo_fusion_services()
        time.sleep(15)
        self.fc.fd["settings"].click_hp_privacy_settings()
        self.fc.fd["settings"].click_yes_to_all()
        self.fc.start_hpanalytics_fusion_services()
