import pytest
from MobileApps.libs.ma_misc import ma_misc


pytest.app_info = "OWS"


class Test_OWS_Signin_Flow:
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ows_emulator_init):
        self = self.__class__
        self.driver, self.ows_emulator, self.config_option, self.hpid, self.account = ows_emulator_init


    def test_01_login(self):
        self.ows_emulator.select_dev_menu_list_item()
        self.ows_emulator.click_hpid_login_button()
        self.hpid.verify_hp_id_sign_up(timeout=20)
        self.hpid.handle_privacy_popup()
        self.hpid.click_sign_in_link_from_create_account()
        self.hpid.login(self.account["email"], self.account["password"])
        self.hpid.handle_privacy_popup()
        self.ows_emulator.verify_emulator_load()
        self.ows_emulator.dismiss_banner()
        assert True


if __name__ == "__main__":
    # This is just for developers to run debug with IDE
    pytest.main(
        [__file__,
        "--browser-type", "chrome",
        "--emu-version", "v8",
        "--stack", "stage"]
)