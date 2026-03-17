import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_09_Remote_Print(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup,load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.home= cls.fc.fd["home"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.p = load_printers_session

    @pytest.fixture(scope="function", autouse="true")
    def go_to_dashboard_menu_and_expand_feature_menu(self, account_type):
        self.fc.load_account_and_go_to_smart_dashboard(stack=self.stack, account_type=account_type)
        self.fc.fd["hp_connect"].click_menu_toggle()
        self.fc.fd["hpc_features"].click_solutions_btn()
    
    @pytest.mark.parametrize("account_type", ["hp+"])
    def test_01_remote_print(self):
        '''
        Description: C50699005
            Remote print job
        Pre-Conditions:
            User should have Print Anywhere option enabled.
            Private Pick up is Off in UCDE portal
        Steps:
            Initiate a remote print job
        Expected Result:
            Make sure the remote print job can be finished with default settings and changed settings.
            Check the printout.
        '''
        self.fc.fd["hpc_features"].click_print_anywhere_btn()
        self.fc.fd["hpc_features"].verify_print_anywhere_screen()
        self.fc.fd["hpc_features"].click_close_btn()
        self.home.verify_home()
        self.fc.add_printer_by_ip(self.p.get_printer_information()["ip address"])
        file_name= "test_pdf_file"
        self.fc.scan_and_save_file_in_hp_smart_files(self.p, file_name)
        self.fc.select_a_file_and_go_to_print_preview(file_name)
        self.fc.select_print_button_and_verify_print_job(self.p)
        self.common_preview.select_done()  
        self.fc.go_hp_smart_files_and_delete_all_files()
        