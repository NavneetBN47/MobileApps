import pytest
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "POOBE"

class Test_01_Create_Account_Page(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup, request):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.stack = request.config.getoption("--stack")
        self.key_name = self.biz_model+"_"+self.stack
        self.file_path = ma_misc.get_abs_path("resources/test_data/poobe/accounts.json")

    def test_01_create_account_and_save_credentials(self):
        self.fc.landing_page(biz = self.biz_model)
        self.p_oobe.click_continue_btn()
        self.hpid.verify_hp_id_sign_in()
        self.hpid.click_create_account_link()
        self.hpid.create_account_and_save_credentials(self.key_name, self.file_path)