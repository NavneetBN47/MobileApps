import pytest
from time import sleep
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_34_Sanity_Searchable_PDF(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session
       
        cls.printer_name=cls.p.get_printer_information()["model name"]
        
    @pytest.mark.smoke
    def test_01_login_with_adv_account(self):
        """
        Login with adv account to test scribble function in scan.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.hpx_sign_in_advanced_account(web_driver=self.web_driver)
        self.fc.add_a_printer(self.p)
    
    @pytest.mark.smoke
    def test_02_verify_searchable_pdf_file_C50476502_C49496657(self):
        """
        Check if "Searchable PDF" is listed in the dropdown or not.
        The document is successfully scanned and saved as a searchable PDF. 
        The text within the PDF is searchable, and search results are accurate.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/49496657
                     https://hp-testrail.external.hp.com/index.php?/cases/view/50476502
        """
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
        self.fc.fd["scan"].select_import_text()
        self.fc.fd["scan"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.INVERTED_JPG, w_const.TEST_DATA.INVERTED_JPG_PATH)
        self.fc.fd["scan"].input_file_name(w_const.TEST_DATA.INVERTED_JPG)
        self.fc.fd["scan"].verify_import_screen()
        self.fc.fd["scan"].click_import_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].verify_save_dialog()
        sleep(1)
        self.fc.fd["scan"].select_file_type_listitem(self.fc.fd["scan"].SEARCHABLE_PDF)
        file_name = self.fc.fd["scan"].get_current_file_name()
        self.fc.fd["scan"].click_dialog_save_btn()
        sleep(1)
        self.fc.fd["scan"].click_save_as_dialog_save_btn()
        self.fc.fd["scan"].verify_file_saved_dialog()
        # verify the saved searchable pdf file is saved.
        file_path = self.fc.fd["scan"].verify_the_saved_file_name_is_correct(file_name)
        
        # Disable Edge restore pages notification (use user-level registry)
        disable_edge_restore = """
        Stop-Process -Name msedge -Force -ErrorAction SilentlyContinue;
        Start-Sleep -Seconds 2;
        $userPolicyPath = 'HKCU:\\Software\\Policies\\Microsoft\\Edge';
        if (-not (Test-Path $userPolicyPath)) {
            New-Item -Path $userPolicyPath -Force | Out-Null
        };
        Set-ItemProperty -Path $userPolicyPath -Name 'RestoreOnStartup' -Value 5 -Force;
        $prefPath = 'HKCU:\\Software\\Microsoft\\Edge\\Main';
        if (-not (Test-Path $prefPath)) {
            New-Item -Path $prefPath -Force | Out-Null
        };
        Set-ItemProperty -Path $prefPath -Name 'ExitTypeNormal' -Value 1 -PropertyType DWORD -Force;
        Remove-Item '$env:LOCALAPPDATA\\Microsoft\\Edge\\User Data\\Default\\Sessions\\*' -Force -ErrorAction SilentlyContinue;
        Remove-Item '$env:LOCALAPPDATA\\Microsoft\\Edge\\User Data\\Default\\Session Storage\\*' -Recurse -Force -ErrorAction SilentlyContinue;
        Remove-Item '$env:LOCALAPPDATA\\Microsoft\\Edge\\User Data\\Default\\Preferences' -Force -ErrorAction SilentlyContinue
        """
        self.driver.ssh.send_command(f"powershell -Command \"{disable_edge_restore}\"", raise_e=False)
        sleep(3)
        
        self.fc.fd["scan"].click_open_file_btn()
        sleep(2)
        self.fc.fd["scan"].verify_searchable_pdf_content(expected_text="dn")
        #delete file
        self.driver.ssh.send_command("del " + file_path)

    @pytest.mark.smoke
    def test_03_logout_adv_account(self):
        """
        Logout adv account after test complete.
        """
        self.fc.restart_hpx()
        self.fc.sign_out(hpx_logout=True)

