import time
import re
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Installation(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.request = request
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session        
        cls.fc = FlowContainer(cls.driver)  
        cls.sf = SystemFlow(cls.driver) 
        cls.wmi = WmiUtilities(cls.driver.ssh)
        cls.sp = cls.sf.sp

        cls.navigation_panel = cls.fc.fd["navigation_panel"]
        cls.support_home = cls.fc.fd["support_home"] 
        cls.support_device = cls.fc.fd["support_device"]
        cls.stack = request.config.getoption("--stack")
        cls.app_env = request.config.getoption("--app-env")

        cls.file_path = ma_misc.get_abs_path(
            w_const.TEST_DATA.HPX_SUPPORT_SIMU_PATH + "speak.json")

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        self.fc.initial_hpx_support_env()
        def closeapp():
            self.navigation_panel.click_close_btn()
        request.addfinalizer(closeapp)   

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production"]) 
    @pytest.mark.testrail("S57581.C32455394")  
    def test_01_verify_hpx_support_folder_generate_after_installation(self):
        """
        verify C:/Program Files (x86)/HP/HPX Support created

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32455394
        """
        #.\PsExec.exe -i -s cmd.exe
        #rmdir /s "xxxxxx"
        self.fc.close_app()
        self.fc.uninstall_app()
        self.fc.remove_file("C:/Users/exec/AppData/Local/Packages/AD2F1837.myHP_v10z8vjag6ke6")
        self.fc.remove_file("C:/Program Files (x86)/HP/HPX Support")
        if self.request.config.getoption("--local-build") is not None:
            local_build = self.request.config.getoption("--local-build")
            if self.request.config.getoption("--appbundle-install") is not None:
                self.fc.install_bundle(local_build)
            else:
                self.fc.install_app(local_build + "\\Install.ps1 -Force")
        self.fc.launch_myHP()
        if not self.wmi.is_grogu():
            assert self.fc.fd["hp_registration"].verify_skip_button_show() is True
            self.fc.fd["hp_registration"].click_skip_button()
        else:
            self.fc.fd["hp_registration"].click_hpone_skip_button()
        if self.fc.fd["hp_registration"].verify_continue_button():
            self.fc.fd["hp_registration"].click_continue_button() 
            print("click continue button.")    
        time.sleep(30)
        self.fc.verify_hpx_support_folder()

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production"]) 
    @pytest.mark.testrail("S57581.C32243354")  
    def test_02_verify_hpx_support_folder_regenerate_if_no_support_folder_when_upgrade(self):
        """
        When there was no folder, verify HPX Support folder can be copied after upgrade , add --app-update "xxxx" in run command to test this case

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/33517819
        """
        self.fc.close_app()
        self.fc.uninstall_app()
        self.fc.remove_file("C:/Users/exec/AppData/Local/Packages/AD2F1837.myHP_v10z8vjag6ke6")
        self.fc.remove_file("C:/Program Files (x86)/HP/HPX Support")
        if self.request.config.getoption("--app-update") is not None:
            upgrade_before_ver = self.request.config.getoption("--app-update")
            if self.request.config.getoption("--appbundle-install") is not None:
                self.fc.install_bundle(upgrade_before_ver)
            else:
                self.fc.install_app(upgrade_before_ver + "\\Install.ps1 -Force")
        time.sleep(5)
        self.fc.launch_myHP()
        time.sleep(5)
        if not self.wmi.is_grogu():
            self.fc.fd["hp_registration"].click_skip_button()
            print('click skip button.')
        else:
            self.fc.fd["hp_registration"].click_hpone_skip_button()
        time.sleep(30)
        self.fc.verify_hpx_support_folder()
        self.fc.close_myHP()

        self.fc.remove_file("C:/Program Files (x86)/HP/HPX Support")
        if self.request.config.getoption("--local-build") is not None:
            local_build = self.request.config.getoption("--local-build")
            if self.request.config.getoption("--appbundle-install") is not None:
                self.fc.install_bundle(local_build)
            else:
                self.fc.install_app(local_build + "\\Install.ps1 -Force")
        time.sleep(5)
        self.fc.launch_myHP()
        if self.fc.fd["hp_registration"].verify_continue_button():
            self.fc.fd["hp_registration"].click_continue_button()  
            print ("click continue button.")  
        time.sleep(30)
        self.fc.verify_hpx_support_folder()

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production"]) 
    @pytest.mark.testrail("S57581.C33517733")         
    def test_03_compare_hpx_support_folder_all_files_version_difference_when_upgrade(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33517733         
        """
        file_version_b_dict = {}
        file_version_a_dict = {}
        file_higher_version_dict = {}
        file_lower_version_dict = {}

        self.fc.close_app()
        self.fc.uninstall_app()
        self.fc.remove_file("C:/Users/exec/AppData/Local/Packages/AD2F1837.myHP_v10z8vjag6ke6")
        self.fc.remove_file("C:/Program Files (x86)/HP/HPX Support")
        if self.request.config.getoption("--app-update") is not None:
            upgrade_before_ver = self.request.config.getoption("--app-update")
            if self.request.config.getoption("--appbundle-install") is not None:
                self.fc.install_bundle(upgrade_before_ver)
            else:
                self.fc.install_app(upgrade_before_ver + "\\Install.ps1 -Force")

        self.fc.launch_myHP()
        if not self.wmi.is_grogu():
            self.fc.fd["hp_registration"].click_skip_button()
        else:
            self.fc.fd["hp_registration"].click_hpone_skip_button()
        time.sleep(30)
        self.fc.close_myHP()

        file_list_before = self.driver.ssh.list_all_files_in_remote_dir("C:/Program Files (x86)/HP/HPX Support/Resources")
        for file_name in file_list_before: 
            if file_name.endswith(".dll") or file_name.endswith(".exe"):
                print (file_name)
                file_version = self.fc.get_file_version(file_name)
                print (file_version)
            file_version_b_dict[file_name] = file_version
        if self.request.config.getoption("--local-build") is not None:
            local_build = self.request.config.getoption("--local-build")
            if self.request.config.getoption("--appbundle-install") is not None:
                self.fc.install_bundle(local_build)
            else:
                self.fc.install_app(local_build + "\\Install.ps1 -Force")

        self.fc.launch_myHP()
        if self.fc.fd["hp_registration"].verify_continue_button():
            self.fc.fd["hp_registration"].click_continue_button()    
        time.sleep(30)

        for file_name in file_list_before:
            if file_name.endswith(".dll") or file_name.endswith(".exe"):
                print (file_name)        
                file_version= self.fc.get_file_version(file_name)
                print (file_version)
                if file_version > file_version_b_dict[file_name]:
                    file_higher_version_dict[file_name] = file_version_b_dict[file_name] + '->' + file_version
                elif file_version < file_version_b_dict[file_name]:
                    file_lower_version_dict[file_name] = file_version_b_dict[file_name] + '->' + file_version
            file_version_a_dict[file_name] = file_version

        if file_higher_version_dict:
            print("Higher version files list:")
            for key in file_higher_version_dict:
                    print(key + ": " + file_higher_version_dict[key])

        if file_lower_version_dict:
            print("Lower version files list:")
            for key in file_lower_version_dict:
                    print(key + ": " + file_lower_version_dict[key])

        for key in file_version_b_dict:
            assert self.__version_cmp(file_version_a_dict[key], file_version_b_dict[key]) == 0   

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production"]) 
    @pytest.mark.testrail("S57581.C33517834")  
    def test_04_verify_files_can_be_copied_after_upgrade(self):
        """
        Verify if more files in new version, these files can be copied, use delete 2 files in old version to simulate more files in new version
        https://hp-testrail.external.hp.com/index.php?/cases/view/33517834
        """
        self.fc.close_app()
        self.fc.uninstall_app()
        self.fc.remove_file("C:/Users/exec/AppData/Local/Packages/AD2F1837.myHP_v10z8vjag6ke6")
        self.fc.remove_file("C:/Program Files (x86)/HP/HPX Support")
        if self.request.config.getoption("--app-update") is not None:
            upgrade_before_ver = self.request.config.getoption("--app-update")
            if self.request.config.getoption("--appbundle-install") is not None:
                self.fc.install_bundle(upgrade_before_ver)
            else:
                self.fc.install_app(upgrade_before_ver + "\\Install.ps1 -Force")
        time.sleep(5)
        self.fc.launch_myHP()
        if not self.wmi.is_grogu():
            self.fc.fd["hp_registration"].click_skip_button()
        else:
            self.fc.fd["hp_registration"].click_hpone_skip_button()
        time.sleep(30)
        self.navigation_panel.click_close_btn()

        self.fc.remove_file("C:/Program Files (x86)/HP/HPX Support/Resources/HPSACommand.dll")
        self.fc.remove_file("C:/Program Files (x86)/HP/HPX Support/Resources/OCChat/OCChat.exe")        
    
        if self.request.config.getoption("--local-build") is not None:
            local_build = self.request.config.getoption("--local-build")
            if self.request.config.getoption("--appbundle-install") is not None:
                self.fc.install_bundle(local_build)
            else:
                self.fc.install_app(local_build + "\\Install.ps1 -Force")

        self.fc.launch_myHP()
        if self.fc.fd["hp_registration"].verify_continue_button():
            self.fc.fd["hp_registration"].click_continue_button()    
        time.sleep(30)

        assert self.driver.ssh.check_file("C:/Program Files (x86)/HP/HPX Support/Resources/HPSACommand.dll")
        assert self.driver.ssh.check_file("C:/Program Files (x86)/HP/HPX Support/Resources/OCChat/OCChat.exe")
   
    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production"]) 
    @pytest.mark.testrail("S57581.C33517834")  
    def test_05_compare_hpx_support_folder_all_files_difference_when_upgrade(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/34219100
        """
        self.fc.close_app()
        self.fc.uninstall_app()
        self.fc.remove_file("C:/Users/exec/AppData/Local/Packages/AD2F1837.myHP_v10z8vjag6ke6")
        self.fc.remove_file("C:/Program Files (x86)/HP/HPX Support")
        if self.request.config.getoption("--app-update") is not None:
            upgrade_before_ver = self.request.config.getoption("--app-update")
            if self.request.config.getoption("--appbundle-install") is not None:
                self.fc.install_bundle(upgrade_before_ver)
            else:
                self.fc.install_app(upgrade_before_ver + "\\Install.ps1 -Force")

        self.fc.launch_myHP()
        if not self.wmi.is_grogu():
            self.fc.fd["hp_registration"].click_skip_button()
        else:
            self.fc.fd["hp_registration"].click_hpone_skip_button()
        time.sleep(30)
        self.navigation_panel.click_close_btn()
   
        file_list_b = self.driver.ssh.list_all_files_in_remote_dir("C:/Program Files (x86)/HP/HPX Support/Resources")
        file_count_b = len(file_list_b)
        print('file_count_b=' + str(file_count_b))       

        if self.request.config.getoption("--local-build") is not None:
            local_build = self.request.config.getoption("--local-build")
            if self.request.config.getoption("--appbundle-install") is not None:
                self.fc.install_bundle(local_build)
            else:
                self.fc.install_app(local_build + "\\Install.ps1 -Force")

        self.fc.launch_myHP()
        if self.fc.fd["hp_registration"].verify_continue_button():
            self.fc.fd["hp_registration"].click_continue_button()    
        time.sleep(30)

        file_list_a = self.driver.ssh.list_all_files_in_remote_dir("C:/Program Files (x86)/HP/HPX Support/Resources")
        file_count_a = len(file_list_a)
        print ('file_count_a=' + str(file_count_a))

        diff_ab = set(file_list_a).difference(set(file_list_b))
        diff_ba = set(file_list_b).difference(set(file_list_a))

        if len(diff_ab) > 0:
            print("Added files:")
            for fname in diff_ab:
                print(fname)

        if len(diff_ba) > 0:
            print("Removed file:")
            for fname in diff_ba:
                print (fname)

        assert len(diff_ab) == 0
        assert len(diff_ba) == 0

    @pytest.mark.require_priority(["High", "BVT"])
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production"]) 
    @pytest.mark.testrail("S57581.C32603273")      
    def test_06_fresh_action(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32603273
        """
        # self.fc.launch_hotkey("hpx://support/device")
        # self.web_driver.close()
        self.fc.close_app()
        time.sleep(5)
        self.fc.launch_myHP()
        if self.fc.fd["hp_registration"].verify_continue_button():
            self.fc.fd["hp_registration"].click_continue_button()  
        # self.fc.sign_out(self.web_driver)
        self.fc.uninstall_app()
        self.fc.remove_file("C:/Users/exec/AppData/Local/Packages/AD2F1837.myHP_v10z8vjag6ke6")
        time.sleep(120)
        if self.request.config.getoption("--local-build") is not None:
            local_build = self.request.config.getoption("--local-build")
            if self.request.config.getoption("--appbundle-install") is not None:
                self.fc.install_bundle(local_build)
            else:
                self.fc.install_app(local_build + "\\Install.ps1 -Force")
        time.sleep(30)
        self.fc.launch_hotkey("hpx://support/device")
        if not self.wmi.is_grogu():
            self.fc.fd["hp_registration"].click_skip_button()
        else:
            self.fc.fd["hp_registration"].click_hpone_skip_button()
        if self.fc.fd["hp_registration"].verify_continue_button():
            self.fc.fd["hp_registration"].click_continue_button()  
        time.sleep(15)
        assert self.fc.fd["support_device"].verify_support_device_page() is True

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production"]) 
    @pytest.mark.testrail("S57581.C33517834")  
    def test_07_upgrade(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32243354
        """
        self.__upgrade_hpx()
        time.sleep(5)
        self.fc.launch_myHP()
        if self.fc.fd["hp_registration"].verify_continue_button():
            self.fc.fd["hp_registration"].click_continue_button()  
            print ("click continue button.")
        time.sleep(30)
        self.fc.verify_hpx_support_folder()     

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production"]) 
    @pytest.mark.testrail("S57581.C32595953")  
    def test_08_click_getphonenumber(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/32595953
        """    
        self.__reinstall_hpx()
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack) 
        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        
        self.support_device.click_speak_to_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.verify_get_phone_number_btn_state() == "false"
            self.support_device.click_category_cbx()
            self.support_device.click_category_opt(3)
            self.support_device.edit_problem("auto test")
            self.support_device.click_privacy_checkbox()
            self.support_device.verify_get_phone_number_btn_state() == "true"
        else:
            self.support_device.click_close_btn()

    @pytest.mark.require_priority(["High"])  
    @pytest.mark.require_stack(["stage_NA", "pie_NA", "production"]) 
    @pytest.mark.testrail("S57581.C33495854")  
    def test_09_click_getphonenumber(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/33495854
        """ 
        self.fc.initial_simulate_file(self.file_path, "C33443483", self.app_env, self.stack) 
        
        self.__upgrade_hpx()

        self.__select_device_card(self.fc.load_simulate_file(self.file_path)["C33443483"][self.app_env]["@hp-support/deviceInfo"]["serialNumber"])
        
        self.support_device.click_speak_to_agent()

        if not self.support_device.verify_outside_hours_popup_display():
            self.support_device.verify_get_phone_number_btn_state() == "false"
            self.support_device.click_category_cbx()
            self.support_device.click_category_opt(3)
            self.support_device.edit_problem("auto test")
            self.support_device.click_privacy_checkbox()
            self.support_device.verify_get_phone_number_btn_state() == "true"
        else:
            self.support_device.click_close_btn()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __version_cmp(self, version1, version2):
        def normalize(v):
            if not v:
                return []
            return [int(x) for x in re.sub(r'(\.0+)*$','', v).split(".")]
        return self.__cmp(normalize(version1), normalize(version2))

    def __cmp(self, a, b):
        return (a > b) - (a < b) 
    
    def __upgrade_hpx(self):
        if self.request.config.getoption("--local-build") is not None:
            local_build = self.request.config.getoption("--local-build")
            if self.request.config.getoption("--appbundle-install") is not None:
                self.fc.install_bundle(local_build)
            else:
                self.fc.install_app(local_build + "\\Install.ps1 -Force")
    
    def __reinstall_hpx(self):
        self.fc.close_app()
        self.fc.uninstall_app()
        self.fc.remove_file("C:/Users/exec/AppData/Local/Packages/AD2F1837.myHP_v10z8vjag6ke6")
        self.fc.remove_file("C:/Program Files (x86)/HP/HPX Support")
        if self.request.config.getoption("--local-build") is not None:
            upgrade_before_ver = self.request.config.getoption("--local-build")
            if self.request.config.getoption("--appbundle-install") is not None:
                self.fc.install_bundle(upgrade_before_ver)
            else:
                self.fc.install_app(upgrade_before_ver + "\\Install.ps1 -Force")
        time.sleep(5)
        self.fc.launch_myHP()
        if not self.wmi.is_grogu():
            self.fc.fd["hp_registration"].click_skip_button()
        else:
            self.fc.fd["hp_registration"].click_hpone_skip_button()
        if self.fc.fd["hp_registration"].verify_continue_button():
            self.fc.fd["hp_registration"].click_continue_button()  
        time.sleep(30)
        self.navigation_panel.click_close_btn()
    
    def __select_device_card(self, serial_number=None, user_name="shhpxtest005@outlook.com", pass_word="hpsa@rocks_335"):
        self.fc.launch_myHP()
        if self.fc.fd["hp_registration"].verify_continue_button():
            self.fc.fd["hp_registration"].click_continue_button()  
        # self.fc.sign_out(self.web_driver)
        time.sleep(3)
        self.fc.navigate_to_support()
        time.sleep(3)
        self.fc.sign_in(user_name, pass_word, self.web_driver)
        time.sleep(3)
        self.fc.select_country("US")
