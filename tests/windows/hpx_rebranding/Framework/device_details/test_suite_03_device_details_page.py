import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_03_Device_Details(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.profile = request.cls.fc.fd["profile"]
        cls.css = request.cls.fc.fd["css"]
        cls.hpx_support = request.cls.fc.fd["hpx_support"]

    @pytest.mark.regression
    def test_01_verify_options_in_get_help_card_C53303947(self):
        assert self.device_card.verify_device_details_page(), "device details page invisible"
        device_details_back_btn_text = self.device_card.verify_devices_back_button()
        assert device_details_back_btn_text == "Devices", "Text on the back button of device details page is incorrect"
        assert self.device_card.verify_get_help_card_options(), "get help card invisible"

    @pytest.mark.regression
    def test_02_verify_links_in_get_help_card_C53303948(self):
        self.device_card.click_pc_devices_back_button()
        self.devicesMFE.click_device_card()
        assert self.device_card.verify_device_details_page(), "device details page invisible"
        assert self.device_card.verify_get_help_card_options(), "get help card invisible"

        self.device_card.click_get_help_manuals_guides()
        self.hpx_support.verify_browser_pane()
        tab_name = self.hpx_support.get_browser_tab_name()
        logging.info(f"Get help manuals guide Browser tab name is: {tab_name}")
        self.profile.minimize_chrome()

        self.device_card.click_get_help_find_repair()
        self.hpx_support.verify_browser_pane()
        tab_name = self.hpx_support.get_browser_tab_name()
        logging.info(f"Get help find repair Browser tab name is: {tab_name}")
        self.profile.minimize_chrome()

        self.device_card.click_get_help_more_help_website()
        self.hpx_support.verify_browser_pane()
        tab_name = self.hpx_support.get_browser_tab_name()
        logging.info(f"Get help more help website Browser tab name is: {tab_name}")
        self.profile.minimize_chrome()

        self.device_card.click_start_repair_link()
        self.hpx_support.verify_browser_pane()
        tab_name = self.hpx_support.get_browser_tab_name()
        logging.info(f"Get help more help website Browser tab name is: {tab_name}")
        self.profile.minimize_chrome()

    @pytest.mark.regression
    def test_03_verify_product_information_card_sections_C57082197(self):
        assert self.device_card.verify_device_details_page(), "device details page invisible"
        self.driver.swipe("product_information")
        assert self.device_card.verify_product_information(), "product information invisible"
        assert self.device_card.verify_warrenty_status(), "warranty status invisible"
        product_number = self.device_card.get_copyproduct_number_text()
        logging.info(f"Product Number: '{product_number}'")
        serial_number = self.device_card.get_copyserial_number_text()
        logging.info(f"Device Serial Number: '{serial_number}'")

    @pytest.mark.regression
    def test_04_verify_all_sections_in_device_details_page_displayed_C53527000(self):
        self.device_card.click_pc_devices_back_button()
        self.devicesMFE.click_device_card()
        assert self.device_card.verify_device_details_page(), "device details page invisible"
        self.driver.swipe(distance=5)
        campaign_ad_1_text = self.device_card.get_campaign_ads_num_1()
        logging.info(f"1st Campaign Ad name: '{campaign_ad_1_text}'")
        campaign_ad_2_text = self.device_card.get_campaign_ads_num_2()
        logging.info(f"1st Campaign Ad name: '{campaign_ad_2_text}'")
        self.driver.swipe("get_help_card_title")
        assert self.device_card.verify_get_help_card_options(), "get help card invisible"
        self.driver.swipe("product_information")
        assert self.device_card.verify_product_information(), "product information invisible"

    @pytest.mark.regression
    def test_05_check_supported_modules_C53303936(self):
        assert self.device_card.verify_device_details_page(), "device details page invisible"
        self.driver.swipe("get_help_card_title")
        assert self.device_card.verify_get_help_card_options(), "get help card invisible"
        self.driver.swipe("product_information")
        assert self.device_card.verify_product_information(), "product information invisible"
        assert self.device_card.verify_warrenty_status(), "warranty status invisible"
        for i in range(15):
            self.driver.swipe(direction="up", distance=i)
        device_type_name = self.device_card.verify_device_type()
        assert device_type_name == "My Computer", "Text of My 'Device Type' is incorrect"
        assert self.profile.verify_devicepage_avatar_btn(), "device page avatar button invisible"
        assert self.device_card.verify_bell_icon_present(), "bell icon invisible"
        assert self.device_card.verify_device_details_page(), "device details page invisible"

    @pytest.mark.regression
    def test_06_validate_app_window_resize_C53303692(self):
        self.devicesMFE.restore_app()
        assert self.device_card.click_pc_devices_back_button(), "device back button not clickable"
        assert self.devicesMFE.click_device_card(), "device card is not present"
        assert self.device_card.verify_device_details_page(), "device details page invisible"
        assert self.device_card.verify_bell_icon_present(), "bell icon is not present"
        self.devicesMFE.verify_profile_icon_show_up()
        assert self.css.verify_sign_in_button_show_up(), "sign-in button not present"
        self.css.click_sign_in_button()
        self.devicesMFE.verify_browser_webview_pane()
        assert self.hpx_support.verify_browser_login_page(), "login page invisible"

    @pytest.mark.regression
    def test_07_check_background_hp_logo_C53303944(self):
        self.device_card.click_pc_devices_back_button()
        self.devicesMFE.click_device_card()
        assert self.profile.verify_myhp_logo(), "hp logo is not present"
        self.fc.close_myHP()
