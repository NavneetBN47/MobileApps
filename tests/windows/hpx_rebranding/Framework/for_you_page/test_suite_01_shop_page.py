import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_01_Shop_Page(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.for_you_page = request.cls.fc.fd["for_you_page"]
        request.cls.fc.web_password_credential_delete()

    @pytest.mark.regression
    def test_01_verify_user_able_to_scroll_recommended_for_you_C60534015(self):
        assert self.devicesMFE.verify_device_mfe_panel_show_up(), "Device MFE panel not visible"
        assert self.device_card.verify_pc_devices_back_button(), "device back button invisible"
        assert self.for_you_page.verify_shop_nav_pill(), "shop nav pill invisible"
        self.for_you_page.click_shop_nav_pill()
        assert self.for_you_page.verify_top_recommended_for_you(), "top recommended for you section invisible"
        assert self.for_you_page.verify_shop_now(), "shop now link invisible"

    @pytest.mark.regression
    def test_02_verify_whether_shop_page_UI_without_sign_in_C60534017(self):
        assert self.devicesMFE.verify_device_mfe_panel_show_up(), "Device MFE panel not visible"
        assert self.device_card.verify_pc_devices_back_button(), "device back button invisible"
        assert self.for_you_page.verify_shop_nav_pill(), "shop nav pill invisible"
        self.for_you_page.click_shop_nav_pill()
        assert self.for_you_page.verify_create_account(), "create account link invisible"
        assert self.for_you_page.verify_sign_in_btn(), "sign in button invisible"
        assert self.for_you_page.verify_unlock_more_with_your_hp_account(), "unlock more with your HP account heading invisible"
        assert self.for_you_page.verify_top_recommended_for_you(), "top recommended for you section invisible"
        assert self.for_you_page.verify_shop_now(), "shop now link invisible"

    @pytest.mark.regression
    def test_03_verify_shop_page_consist_all_sections_C60534018(self):
        assert self.devicesMFE.verify_device_mfe_panel_show_up(), "Device MFE panel not visible"
        assert self.device_card.verify_pc_devices_back_button(), "device back button invisible"
        assert self.for_you_page.verify_shop_nav_pill(), "shop nav pill invisible"
        self.for_you_page.click_shop_nav_pill()
        assert self.for_you_page.verify_create_account(), "create account link invisible"
        assert self.for_you_page.verify_sign_in_btn(), "sign in button invisible"
        assert self.for_you_page.verify_unlock_more_with_your_hp_account(), "unlock more with your HP account heading invisible"
        assert self.for_you_page.verify_top_recommended_for_you(), "top recommended for you section invisible"
        assert self.for_you_page.verify_shop_now(), "shop now link invisible"
        assert self.for_you_page.verify_featured_offers(), "featured offers section not visible"
        assert self.for_you_page.verify_shop_by_product(), "Shop by product section not visible"

    @pytest.mark.regression
    def test_04_verify_ads_in_shop_page_are_clickable_C60534019(self):
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon invisible"
        assert self.devicesMFE.verify_profile_icon_show_up(), "profile icon invisible"
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button invisible"
        assert self.device_card.verify_pc_devices_back_button(), "device back button invisible"
        assert self.for_you_page.verify_shop_nav_pill(), "shop nav pill invisible"
        self.for_you_page.click_shop_nav_pill()
        assert self.for_you_page.verify_create_account(), "create account link invisible"
        assert self.for_you_page.verify_sign_in_btn(), "sign in button invisible"
        assert self.for_you_page.verify_unlock_more_with_your_hp_account(), "unlock more with your HP account heading invisible"
        assert self.for_you_page.verify_top_recommended_for_you(), "top recommended for you section invisible"
        assert self.for_you_page.verify_shop_now(), "shop now link invisible"
        self.for_you_page.click_shop_now()
        assert self.for_you_page.verify_shop_now_webview_title(), "shop now link is not clickable"
        self.fc.kill_chrome_process()

    @pytest.mark.regression
    def test_05_verify_ads_in_shop_page_have_relevant_images_C60534020(self):
        assert self.devicesMFE.verify_device_mfe_panel_show_up(), "Device MFE panel not visible"
        assert self.device_card.verify_pc_devices_back_button(), "device back button invisible"
        assert self.for_you_page.verify_shop_nav_pill(), "shop nav pill invisible"
        self.for_you_page.click_shop_nav_pill()
        assert self.for_you_page.verify_create_account(), "create account link invisible"
        assert self.for_you_page.verify_sign_in_btn(), "sign in button invisible"
        assert self.for_you_page.verify_unlock_more_with_your_hp_account(), "unlock more with your HP account heading invisible"
        assert self.for_you_page.verify_shop_by_product(), "Shop by product section not visible"
        assert self.for_you_page.verify_laptops_image_show_up(), "laptops image invisible"
        assert self.for_you_page.verify_printers_image_show_up(), "printers image invisible"
        assert self.for_you_page.verify_accessories_image_show_up(), "accessories image invisible"
        assert self.for_you_page.verify_monitors_image_show_up(), "monitors image invisible"

    @pytest.mark.regression
    def test_06_verify_ordernow_learnmore_navigate_externallink_on_click_C60534021(self):
        assert self.devicesMFE.verify_device_mfe_panel_show_up(), "Device MFE panel not visible"
        assert self.device_card.verify_pc_devices_back_button(), "device back button invisible"
        assert self.for_you_page.verify_shop_nav_pill(), "shop nav pill invisible"
        self.for_you_page.click_shop_nav_pill()
        assert self.for_you_page.verify_create_account(), "create account link invisible"
        assert self.for_you_page.verify_sign_in_btn(), "sign in button invisible"
        assert self.for_you_page.verify_unlock_more_with_your_hp_account(), "unlock more with your HP account heading invisible"
        assert self.for_you_page.verify_top_recommended_for_you(), "top recommended for you section invisible"
        assert self.for_you_page.verify_shop_now(), "shop now link invisible"
        assert self.for_you_page.verify_featured_offers(), "featured offers section not visible"
        assert self.for_you_page.verify_learn_more_link(), "Learn More link not visible"
        self.for_you_page.click_learn_more_link()
        assert self.for_you_page.verify_learn_more_webview_page(), "Learn More link is not clickable"
        self.fc.kill_chrome_process()
        assert self.for_you_page.verify_order_yours_today_link(), "Order Yours Today link is not clickable"
        self.for_you_page.click_order_yours_today_link()
        assert self.for_you_page.verify_order_yours_today_webview_page(), "Order Yours Today webview title is not correct"
        self.fc.kill_chrome_process()

    @pytest.mark.regression
    def test_07_verify_shop_by_product_section_cards_C60534022(self):
        assert self.devicesMFE.verify_device_mfe_panel_show_up(), "Device MFE panel not visible"
        assert self.device_card.verify_pc_devices_back_button(), "device back button invisible"
        assert self.for_you_page.verify_shop_nav_pill(), "shop nav pill invisible"
        self.for_you_page.click_shop_nav_pill()
        assert self.for_you_page.verify_create_account(), "create account link invisible"
        assert self.for_you_page.verify_sign_in_btn(), "sign in button invisible"
        assert self.for_you_page.verify_unlock_more_with_your_hp_account(), "unlock more with your HP account heading invisible"
        assert self.for_you_page.verify_top_recommended_for_you(), "top recommended for you section invisible"
        assert self.for_you_page.verify_shop_by_product(), "Shop by product section not visible"
        assert self.for_you_page.verify_printers(), "Printers card not visible"
        assert self.for_you_page.verify_accessories(), "Accessories card not visible"
        assert self.for_you_page.verify_laptops(), "Laptops card not visible"
        assert self.for_you_page.verify_monitors(), "Monitors card not visible"

    @pytest.mark.regression
    def test_08_verify_looking_for_more_and_visit_hpcom_links_C60534023(self):
        assert self.devicesMFE.verify_device_mfe_panel_show_up(), "Device MFE panel not visible"
        assert self.device_card.verify_pc_devices_back_button(), "device back button invisible"
        assert self.for_you_page.verify_shop_nav_pill(), "shop nav pill invisible"
        self.for_you_page.click_shop_nav_pill()
        assert self.for_you_page.verify_looking_for_more(), "looking for more section invisible"
        assert self.for_you_page.verify_visit_hpcom(), "visit hp.com invisible"

    @pytest.mark.regression
    def test_09_verify_visit_hpcom_link_navigates_to_external_page_C60534024(self):
        assert self.devicesMFE.verify_device_mfe_panel_show_up(), "Device MFE panel not visible"
        assert self.device_card.verify_pc_devices_back_button(), "device back button invisible"
        assert self.for_you_page.verify_shop_nav_pill(), "shop nav pill invisible"
        self.for_you_page.click_shop_nav_pill()
        assert self.for_you_page.verify_looking_for_more(), "looking for more section invisible"
        assert self.for_you_page.verify_visit_hpcom(), "visit hp.com invisible"
        self.for_you_page.click_visit_hpcom()
        assert self.for_you_page.verify_visit_hpcom_webview_page(), "visit hp.com link is not clickable"
        self.fc.kill_chrome_process()
