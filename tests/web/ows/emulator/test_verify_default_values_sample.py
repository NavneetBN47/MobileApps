import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.web.const import TEST_DATA


pytest.app_info = "OWS"


class Test_verify_defaults_DEV:
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ows_emulator_init):
        self = self.__class__
        self.driver, self.ows_emulator, self.config_option, *_ = ows_emulator_init
        # TODO populate self.default_ui_values from source TBD, put in resource json file for now
        self.default_ui_values = ma_misc.load_json_file(TEST_DATA.OWS_DEFAULT_VALUES)


    def get_ui_default(self, keys, default_value = ''):
        dv = self.default_ui_values
        for key in keys.split('.'):
            if type(dv) == dict:
                dv = dv.get(key, default_value)
            else:
                return default_value
        
        if type(dv) == dict:
            return dv.get(self.config_option.stack, default_value)
        else:
            return dv


    # def test_01_verify_Device(self):
    #     # TODO Loop through Quick Options for all product families Taiji, Palermo, Taccola etc.
    #     # This function will be huge, consider to split in sub classes or functions
    #     assert True


    # def test_02_verify_APAF(self):
    #     # APAF = App/Post-OOBE/Agreements/Features
    #     assert True


    def test_03_verify_DEV(self):
        # Section DEV > Virtual Devices
        # <Relevant code goes here>

        # Section DEV > DEV
        self.ows_emulator.select_dev_menu_list_item()
        assert self.driver.get_text("dev_gemini_moobe_url_textbox") == self.get_ui_default('DEV.dev_gemini_moobe_url_textbox')
        assert self.driver.get_text("dev_oss_url_textbox") == self.get_ui_default('DEV.dev_oss_url_textbox')
        assert self.driver.check_box("dev_fresh_install_checkbox") == self.get_ui_default('DEV.dev_fresh_install_checkbox')
        
        # Section DEV > Stubbed Services
        # <Relevant code goes here>
        
        # Section DEV > Setup Complete
        # <Relevant code goes here>


if __name__ == "__main__":
    # This is just for developers to run debug with IDE
    pytest.main(
        [__file__,
        "--browser-type", "chrome",
        "--emu-version", "v8",
        "--stack", "stage"]
    )