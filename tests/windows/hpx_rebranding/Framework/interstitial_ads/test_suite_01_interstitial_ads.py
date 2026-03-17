import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression","function_setup_myhp_launch")
class Test_Suite_01_Interstitial_Ads(object):

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.bell_icon = request.cls.fc.fd["bell_icon"]
        cls.for_you_page = request.cls.fc.fd["for_you_page"]
        request.cls.fc.web_password_credential_delete()

    @pytest.mark.regression
    def test_01_verify_whether_interstitial_ad_is_displayed_when_required_C57465790(self):
        self._verify_shop_page()
        assert self.for_you_page.verify_create_account(), "create account link invisible"
        assert self.for_you_page.verify_sign_in_btn(), "sign in button invisible"
        assert self.for_you_page.verify_unlock_more_with_your_hp_account(), "unlock more with your HP account heading invisible"
        assert self.for_you_page.verify_top_recommended_for_you(), "top recommended for you section invisible"
        assert self.for_you_page.verify_shortcuts_section(), "shortcuts section invisible"
        self.for_you_page.click_shortcuts_section()

    @pytest.mark.regression
    def test_02_verify_displayed_content_in_the_interstitial_page_is_relevant_to_the_ad_C57465791(self):
        self._verify_shop_page()
        assert self.for_you_page.verify_create_account(), "create account link invisible"
        assert self.for_you_page.verify_sign_in_btn(), "sign in button invisible"
        assert self.for_you_page.verify_unlock_more_with_your_hp_account(), "unlock more with your HP account heading invisible"
        assert self.for_you_page.verify_top_recommended_for_you(), "top recommended for you section invisible"
        assert self.for_you_page.verify_shortcuts_section(), "shortcuts section invisible"
        self.for_you_page.click_shortcuts_section()
        assert self.for_you_page.verify_try_feature()," try feature button invisible"
        assert self.for_you_page.verify_work_smarter_with_hp_shortcuts(), "work smarter with hp shortcuts text invisible"
        self._verify_shop_page()

    @pytest.mark.regression
    def test_03_verify_clicking_on_the_ad_correctly_navigates_to_destination_C57465792(self):
        self._verify_shop_page()
        assert self.for_you_page.verify_create_account(), "create account link invisible"
        assert self.for_you_page.verify_sign_in_btn(), "sign in button invisible"
        assert self.for_you_page.verify_unlock_more_with_your_hp_account(), "unlock more with your HP account heading invisible"
        assert self.for_you_page.verify_top_recommended_for_you(), "top recommended for you section invisible"
        assert self.for_you_page.verify_shortcuts_section(), "shortcuts section invisible"
        self.for_you_page.click_shortcuts_section()
        assert self.for_you_page.verify_work_smarter_with_hp_shortcuts(), "work smarter with hp shortcuts text invisible"
        assert self.for_you_page.verify_work_smarter_with_shortcuts_image(), "work smarter with shortcuts image invisible"
        self._verify_shop_page()

    @pytest.mark.regression
    def test_04_verify_back_and_close_button_closes_and_returns_back_to_the_main_ad_page_C57465793(self):
        self._verify_shop_page()
        assert self.for_you_page.verify_create_account(), "create account link invisible"
        assert self.for_you_page.verify_sign_in_btn(), "sign in button invisible"
        assert self.for_you_page.verify_unlock_more_with_your_hp_account(), "unlock more with your HP account heading invisible"
        assert self.for_you_page.verify_top_recommended_for_you(), "top recommended for you section invisible"
        self._verify_digital_buddy_section()
        assert self.for_you_page.verify_digital_buddy_close_btn()," digital buddy close button invisible"
        self.for_you_page.click_digital_buddy_close_btn()
        self._verify_shop_page()
        assert self.for_you_page.verify_your_digital_buddy(), "your digital buddy section invisible"
        self._verify_digital_buddy_section()
        assert self.device_card.verify_pc_devices_back_button(), "device back button invisible"
        self.device_card.click_pc_devices_back_button()
        self.device_card.click_pc_devices_back_button()
        assert self.for_you_page.verify_your_digital_buddy(), "your digital buddy section invisible"

    @pytest.mark.regression
    def test_05_verify_interstitial_page_handles_0_1_or_2_CTAs_C57465798(self):
        self._verify_shop_page()
        assert self.for_you_page.verify_create_account(), "create account link invisible"
        assert self.for_you_page.verify_sign_in_btn(), "sign in button invisible"
        assert self.for_you_page.verify_unlock_more_with_your_hp_account(), "unlock more with your HP account heading invisible"
        assert self.for_you_page.verify_top_recommended_for_you(), "top recommended for you section invisible"
        self._verify_digital_buddy_section()
        assert self.for_you_page.verify_digital_buddy_close_btn()," digital buddy close button invisible"
        assert self.device_card.verify_pc_devices_back_button(), "device back button invisible"

######################################################################
#                           PRIVATE FUNCTIONS                        #
######################################################################

    def _verify_shop_page(self):
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon invisible"
        assert self.devicesMFE.verify_profile_icon_show_up(), "profile icon invisible"
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button invisible"
        assert self.device_card.verify_pc_devices_back_button(), "device back button invisible"
        assert self.for_you_page.verify_hp_ai_assistant(), "HP AI Assistant invisible"
        assert self.for_you_page.verify_shop_nav_pill(), "shop nav pill invisible"
        self.for_you_page.click_shop_nav_pill()

    def _verify_digital_buddy_section(self):
        assert self.for_you_page.verify_your_digital_buddy(), "your digital buddy section invisible"
        self.for_you_page.click_your_digital_buddy_section()
        assert self.for_you_page.verify_digital_buddy_title(), "digital buddy title invisible"
        assert self.for_you_page.verify_digital_buddy_description(), "digital buddy description invisible"
        assert self.for_you_page.verify_digital_buddy_image(), "digital buddy image invisible"    
