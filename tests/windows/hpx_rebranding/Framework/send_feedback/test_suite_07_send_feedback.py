import pytest

from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression","function_setup_myhp_launch")
class Test_Suite_07_Send_Feedback(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.feedback = request.cls.fc.fd["feedback"]

    @pytest.mark.regression
    def test_01_verify_invalid_email_error_message_displayed_C53681234(self):
        self.profile.click_devicepage_avatar_btn()
        assert self.profile.verify_feedback_btn(), "Feedback button is not displayed"
        self.profile.click_feedback_btn()
        assert self.feedback.verify_feedback_slide_title(), "Feedback slide title is not visible"
        self.driver.swipe(direction="down", distance=6)
        assert self.feedback.verify_contacting_email(), "Contacting email field is not visible"
        self.feedback.input_contacting_email("kujyhdiuym")
        actual_invalid_msg = self.feedback.get_invalid_email_message()
        expected_invalid_msg = "Please enter a valid email address."
        assert expected_invalid_msg == actual_invalid_msg, "Invalid message text is mismatching"

    @pytest.mark.regression
    def test_02_verify_feedback_button_disabled_after_submissions_C62132638(self):
        assert self.profile.verify_devicepage_avatar_btn(), "Device page avatar button not found"
        self.profile.click_devicepage_avatar_btn()
        assert self.profile.verify_profile_side_panel(), "Profile side panel is not displayed"
        self.profile.verify_feedback_btn()
        self.profile.click_feedback_btn()
        for _ in range(5):
            assert self.feedback.verify_feedback_slide_title(), "Feedback slide title is not visible"
            self.feedback.select_star_rating(5)
            self.feedback.click_why_did_you_open_today_options()
            self.feedback.select_configure_my_devices()
            self.feedback.click_whats_your_feedback_related_to_options()
            self.feedback.select_load_time()
            assert self.feedback.verify_tell_your_experience(), "Tell your experience text box is not visible"
            self.feedback.input_tell_your_experience("Testing successful feedback submission")
            assert self.feedback.verify_contacting_email(), "Contacting email field is not visible"   
            self.feedback.input_contacting_email("clearfields@testmail.com")
            assert self.feedback.verify_send_feedback_submit_btn(), "Submit feedback button is not visible"
            self.feedback.click_submit_feedback()
            assert self.feedback.verify_feedback_submission_success_message(), "Feedback submission success message is not displayed"
        assert self.feedback.verify_menu_btn_from_feedback(), "Menu button from feedback is not visible"
        self.feedback.click_menu_btn_from_feedback()
        assert self.profile.verify_feedback_is_disabled("feedback_btn"), "Feedback button is not disabled"
        self.fc.close_myHP()
 