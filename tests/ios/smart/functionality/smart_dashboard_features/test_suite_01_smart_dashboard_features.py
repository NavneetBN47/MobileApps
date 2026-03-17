import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_01_Smart_Dashboard_Features(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    @pytest.fixture(scope="function", autouse="true")
    def go_to_dashboard_menu_and_expand_feature_menu(self, account_type):
        self.fc.load_account_and_go_to_smart_dashboard(stack=self.stack, account_type=account_type)
        self.fc.fd["hp_connect"].click_menu_toggle()
        self.fc.fd["hpc_features"].click_features_btn()

    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_01_feature_menu_items(self, account_type):
        '''
            C28353792: Verify menu items for Features (hp+)
            C28590357: Verify menu items for Features (ucde)
        '''
        if account_type == "hp+":
            self.fc.fd["hpc_features"].verify_features_screen()
        elif account_type == "ucde":
            self.fc.fd["hpc_features"].verify_features_screen()
    
    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_02_smart_security(self):
        '''
            C28590358: Verify Smart Security page (ucde)
        '''
        self.fc.fd["hpc_features"].click_smart_security_btn()
        self.fc.fd["hpc_features"].verify_smart_security_screen()
    
    @pytest.mark.parametrize("account_type", ["hp+"])
    def test_03_print_anywhere(self):
        '''
            C28353793: Verify Print Anywhere page (hp+)
        '''
        self.fc.fd["hpc_features"].click_print_anywhere_btn()
        self.fc.fd["hpc_features"].verify_print_anywhere_screen()
    
    @pytest.mark.parametrize("account_type", ["hp+"])
    def test_04_advance_page(self):
        '''
        C28353795 Verify HP Smart Advance page 
        '''
        self.fc.fd["hpc_features"].click_hp_smart_advance_btn()
        self.fc.fd["hpc_features"].verify_hp_smart_advance_screen()       