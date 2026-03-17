import pytest
import random
import string
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression","function_setup_myhp_launch")
class Test_Suite_06_Feedback_Enhancements(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(cls.driver)
        request.cls.profile = cls.fc.fd["profile"]
        request.cls.feedback = cls.fc.fd["feedback"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.fc.kill_hpx_process()
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.uninstall_app()

    @pytest.mark.regression
    def test_01_verify_options_in_second_dropdown_C53681230(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_feedback_btn(), "Feedback button missing"
        self.profile.click_feedback_btn()
        assert self.feedback.verify_whats_your_feedback_related_to_title(), "verify what's your feedback related to is missing"
        assert self.feedback.verify_whats_your_feedback_related_to_list(), "verify what's your feedback related to list is missing"

    @pytest.mark.regression
    def test_02_verify_email_address_field_accepts_only_valid_email_address_C53681235(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_feedback_btn(), "Feedback button missing"
        self.profile.click_feedback_btn()
        assert self.feedback.verify_feedback_slide_title(), "Feedback slide title is not visible"
        self.feedback.select_star_rating(5)
        self.feedback.click_why_did_you_open_today_options()
        self.feedback.select_configure_my_devices()
        self.feedback.click_whats_your_feedback_related_to_options()
        self.feedback.select_load_time()
        assert self.feedback.verify_tell_your_experience(), "Tell your experience text area is not visible"
        self.feedback.input_tell_your_experience("Testing successful feedback submission")
        assert self.feedback.verify_contacting_email(), "Contacting email textbox is not visible"    
        self.feedback.input_contacting_email(".kujyhd.@testmail.com")
        assert self.feedback.verify_invalid_email_message(), "Invalid email error message not shown after interaction"
        assert not self.feedback.verify_send_feedback_submit_is_clickbale(), "Submit button is clickable even with invalid email"
        self.feedback.input_contacting_email("clearfields@testmail.com")
        assert self.feedback.verify_send_feedback_submit_is_clickbale(), "Submit button is not clickable"