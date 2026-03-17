import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_04_Send_Feedback(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.css = request.cls.fc.fd["css"]
        cls.feedback = request.cls.fc.fd["feedback"]

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    def test_01_verify_content_in_feedback_with_figma_C53681223(self):
        self.devicesMFE.click_profile_button()
        self.profile.click_feedback_btn()
        self.feedback.verify_feedback_slide_title()
        self.feedback.verify_stars_present()
        assert self.feedback.verify_why_did_you_open_app_today_title(), "verify why did you open app today title missing"
        assert self.feedback.verify_whats_your_feedback_related_to_title(), "verify what's your feedback related to missing "
        assert self.feedback.verify_tell_your_experience(), "tell your experience missing"
        assert self.feedback.verify_edit_feedback(), "edit feedback missing"
        assert self.feedback.veify_hp_privacy_statement_link(), "hp privacy statement link missing"

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    def test_02_select_stars_select_deselect_individually_C53681225(self):
        self.devicesMFE.click_profile_button()
        self.profile.verify_feedback_btn()
        self.profile.click_feedback_btn()
        assert self.feedback.verify_rating_star_field(), "rating star field is missing"
        self.feedback.select_and_unselect_star_rating(5)

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    def test_03_verify_alignment_of_submit_button_C53681236(self):
        self.devicesMFE.click_profile_button()
        self.profile.verify_sign_in_from_avatar_sideflyout()
        self.profile.verify_support_device_btn()
        self.profile.verify_profile_settings_btn()
        self.profile.verify_feedback_btn()
        self.profile.click_feedback_btn()
        assert self.feedback.verify_submit_btn_position(), "Submit button is not positioned correctly on the feedback form"

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    def test_04_verify_feedback_from_avater_panel_C67872420(self):
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_feedback_btn(), "feedback button invisible"
        self.profile.click_feedback_btn()