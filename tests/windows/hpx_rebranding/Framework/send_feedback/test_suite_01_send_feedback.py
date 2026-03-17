import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_01_Send_Feedback(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.feedback = request.cls.fc.fd["feedback"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]

        yield
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.uninstall_app()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.skip_in_prod
    def test_01_verify_send_feedback_is_present_C53681220(self):
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        feedback_btn_text = self.profile.verify_feedback_btn()
        assert feedback_btn_text == "Send feedback", "Text on feedback button is incorrect/changed"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.skip_in_prod
    def test_02_verify_send_feedback_slide_out_C53681222(self):
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_feedback_btn()
        self.profile.click_feedback_btn()
        feedback_title = self.feedback.verify_hpx_feedback_page_title()
        assert feedback_title == "We'd love your feedback!", "feedback page title is incorrect/updated"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.skip_in_prod
    def test_03_verify_feedback_slide_back_btn_C53681224(self):
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.click_feedback_btn()
        self.feedback.verify_rating_star_field()
        self.feedback.verify_menu_btn_from_feedback()
        feedback_title = self.feedback.verify_hpx_feedback_page_title()
        assert feedback_title == "We'd love your feedback!", "feedback page title is incorrect/updated"
        self.feedback.verify_menu_btn_from_feedback()
        self.feedback.click_menu_btn_from_feedback()
        self.profile.verify_profile_side_panel()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.skip_in_prod
    def test_04_verify_rating_star_field_C53681226(self):
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.click_feedback_btn()
        assert self.feedback.verify_rating_star_field(), "rating star field is missing"
        self.feedback.select_star_rating(5)
        self.feedback.unselect_star_rating(5)

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.skip_in_prod
    def test_05_verify_functionality_of_2nd_drop_down_menu_C53681231(self):
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_feedback_btn()
        self.profile.click_feedback_btn()
        assert self.feedback.verify_whats_your_feedback_related_to_title(), "verify what's your feedback related to is missing"
        self.feedback.verify_whats_your_feedback_related_to_list()
        self.feedback.select_each_option_from_second_dropdown_menu()