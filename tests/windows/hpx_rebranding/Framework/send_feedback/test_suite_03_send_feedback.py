import pytest
import re
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_03_Send_Feedback(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):  
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.profile = request.cls.fc.fd["profile"]
        cls.feedback = request.cls.fc.fd["feedback"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.device_card = request.cls.fc.fd["device_card"]
        yield
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.uninstall_app()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.skip_in_prod
    def test_01_verify_email_adress_is_optional_C53681233(self):
        self.devicesMFE.click_profile_button()
        self.profile.click_feedback_btn()
        assert "We'd love your feedback!" == self.feedback.verify_hpx_feedback_page_title()
        self.feedback.select_star_rating(5)
        self.feedback.click_why_did_you_open_today_options()
        self.feedback.select_configure_my_devices()
        self.feedback.click_whats_your_feedback_related_to_options()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.feedback.select_load_time()
        self.feedback.verify_tell_your_experience()
        self.feedback.input_tell_your_experience("for Internal testing")
        self.feedback.verify_send_feedback_submit_btn()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.feedback.click_submit_feedback()
        feedback_thanks_text = self.feedback.verify_feedback_submission_success_message()
        actual_thanks_text = "Thanks for your feedback. It's great to know you're enjoying our app!"
        assert feedback_thanks_text == actual_thanks_text, "Feedback Thank You message is mismatching/wrong"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.skip_in_prod
    def test_02_verify_feedback_submission_C53681237(self):
        self.devicesMFE.verify_profile_icon_show_up()
        self.device_card.click_pc_devices_back_button()
        self.devicesMFE.click_device_card()
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_feedback_btn()
        self.profile.click_feedback_btn()
        self.feedback.verify_feedback_slide_title()
        self.feedback.select_star_rating(3)
        self.feedback.click_why_did_you_open_today_options()
        self.feedback.select_get_tech_support()
        self.feedback.click_whats_your_feedback_related_to_options()
        self.feedback.select_load_time()
        self.feedback.verify_tell_your_experience()
        self.feedback.input_tell_your_experience("for Internal testing")
        assert self.feedback.verify_send_feedback_submit_btn(), "Submit feeback button missing "
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.feedback.click_submit_feedback()
        
    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.skip_in_prod
    def test_03_verify_confirmation_message_after_submtting_feedback_C53681238(self):
        self.devicesMFE.verify_profile_icon_show_up()
        self.device_card.click_pc_devices_back_button()
        self.devicesMFE.click_device_card()
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_feedback_btn()
        self.profile.click_feedback_btn()
        self.feedback.verify_feedback_slide_title()
        self.feedback.select_star_rating(2)
        self.feedback.click_why_did_you_open_today_options()
        self.feedback.select_configure_my_devices()
        self.feedback.click_whats_your_feedback_related_to_options()
        self.feedback.select_erase_of_use()
        self.feedback.verify_tell_your_experience()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.feedback.click_submit_feedback()
        feedback_thanks_text = self.feedback.verify_feedback_submission_success_message()
        actual_thanks_text = "We appreciate your feedback and will use it to improve our app."
        assert feedback_thanks_text == actual_thanks_text, "Feedback Thank You message is mismatching/wrong"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.skip_in_prod
    def test_04_verify_input_fields_cleared_after_feedback_submission_C53681239(self):
        self.devicesMFE.verify_profile_icon_show_up()
        self.device_card.click_pc_devices_back_button()
        self.devicesMFE.click_device_card()
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_feedback_btn()
        self.profile.click_feedback_btn()
        self.feedback.verify_feedback_slide_title()
        self.feedback.select_star_rating(3)
        self.feedback.click_why_did_you_open_today_options()
        self.feedback.select_configure_my_devices()
        self.feedback.click_whats_your_feedback_related_to_options()
        self.feedback.select_erase_of_use()
        self.feedback.verify_tell_your_experience()
        self.feedback.input_tell_your_experience("for Internal testing")
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.feedback.click_submit_feedback()
        feedback_thanks_text = self.feedback.verify_feedback_submission_success_message()
        actual_thanks_text = "We appreciate your feedback and will use it to improve our app."
        assert feedback_thanks_text == actual_thanks_text, "Feedback Thank You message is mismatching/wrong"
        self.feedback.verify_after_submission_inputs_cleared()