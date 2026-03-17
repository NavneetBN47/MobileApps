import logging
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
import pytest
import time
from MobileApps.libs.ma_misc import conftest_misc

pytest.app_info = "HPX"

language_list_path = ma_misc.get_abs_path("resources/test_data/hpx/locale/language_list.txt")
with open(language_list_path, "r+") as f:
    languages = f.read().split(',')


@pytest.fixture(params=languages)
def language(request):
    return request.param

@pytest.fixture(scope="session", params=["hp_privacy_screenshot"])
def screenshot_folder_name(request):
    return request.param


class Test_Suite_Localization(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.attachment_path = conftest_misc.get_attachment_folder()

    # Privacy policy screen  
    def test_01_HP_Privacy_module_C33555624(self, language, publish_hpx_localization_screenshot, screenshot_folder_name):
        self.fc.turn_on_hp_privacy_page(self.driver.ssh)
        lang_settings = ma_misc.load_json_file("resources/test_data/hpx/hpprivacy.json")[language]["translation"][
            "privacy"]
        self.fc.uninstall_app()
        self.fc.install_app(self.driver.session_data["installer_path"])
        time.sleep(30)
        self.fc.update_properties(language)
        self.fc.launch_app()
        time.sleep(5)
        self.fc.launch_app()

        assert self.fc.fd["hp_privacy_setting"].verify_manage_options_show() is True, "Manage options not available"
        actual_header_text = self.fc.fd["hp_privacy_setting"].check_localization_privacy_header_title()
        ma_misc.create_localization_screenshot_folder("hp_privacy_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "hp_privacy_screenshot/{}_hp_privacy.png".format(language))
        expected_header_text = lang_settings["header"]
        assert actual_header_text == expected_header_text, "Header text is not matched"

        # desc all text
        actual_desc_customer_support = self.fc.fd["hp_privacy_setting"].check_localization_desc_customer_support()
        expected_desc_customer_support = lang_settings["body_section_1"]
        assert actual_desc_customer_support == expected_desc_customer_support, "Desc customer support text is not matched"

        actual_desc_news_offers = self.fc.fd["hp_privacy_setting"].check_localization_desc_news_offers()
        expected_desc_news_offers = lang_settings["body_section_3"]
        assert actual_desc_news_offers == expected_desc_news_offers, "Desc news offers text is not matched"

        actual_desc_learn_more= self.fc.fd["hp_privacy_setting"].check_localization_desc_learn_more().strip()
        expected_desc_learn_more=lang_settings["body_section_2_link"]
        expected_desc_learn_more = expected_desc_learn_more.replace("]({{}})", "")
        expected_desc_learn_more = expected_desc_learn_more.replace("[", "").strip()
        assert actual_desc_learn_more==expected_desc_learn_more, "Desc learn more text is not matched"

        # Accept All/Decline All/ Manage options localization
        actual_btn_accept_all = self.fc.fd["hp_privacy_setting"].check_localization_btn_accept_all()
        expected_btn_accept_all = lang_settings["btn_accept"]
        assert actual_btn_accept_all == expected_btn_accept_all, "Accept all button text is not matched"

        actual_btn_decline_all = self.fc.fd["hp_privacy_setting"].check_localization_btn_decline_all()
        expected_btn_decline_all = lang_settings["btn_decline"]
        assert actual_btn_decline_all == expected_btn_decline_all, "Decline all button text is not matched"

        actual_btn_manage_options = self.fc.fd["hp_privacy_setting"].check_localization_btn_manage_options()
        expected_btn_manage_options = lang_settings["btn_manage"]
        assert actual_btn_manage_options == expected_btn_manage_options, "Manage options button text is not matched"
