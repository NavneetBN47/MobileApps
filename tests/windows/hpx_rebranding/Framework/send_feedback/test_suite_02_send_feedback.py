import pytest
import random
import string
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_02_Send_Feedback(object):
    @pytest.fixture(scope="class", autouse=True)
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
        yield
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.uninstall_app()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.skip_in_prod
    def test_01_verify_user_input_text_box_C53681232(self):
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_feedback_btn()
        self.profile.click_feedback_btn()
        self.feedback.verify_edit_feedback()
        random_text = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + ' ', k=2010))
        logging.info(f"Length of text entered into feedback textbox is '{len(random_text)}'")
        self.feedback.input_tell_your_experience(random_text)
        logging.info(f"Length of text taken by feedback textbox is '{len(self.feedback.get_entered_text())}'")
        assert len(self.feedback.get_entered_text()) <= 2000, "Text box accepts not more than 2000 characters"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.skip_in_prod
    def test_02_verify_why_did_you_open_app_today_list_C53681228(self):
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_feedback_btn()
        self.profile.click_feedback_btn()
        assert self.feedback.verify_why_did_you_open_app_today_title(), "verify why did you open app today title missing"
        self.feedback.verify_why_did_you_open_app_today_list()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.skip_in_prod
    def test_03_verify_whats_you_feedback_related_to_list_C42631135(self):
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        self.profile.verify_feedback_btn()
        self.profile.click_feedback_btn()
        assert self.feedback.verify_whats_your_feedback_related_to_title(), "verify what's your feedback related to missing "
        self.feedback.verify_whats_your_feedback_related_to_list()