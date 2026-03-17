import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const
import string
import random

pytest.app_info = "SMART"

class Test_Suite_01_Feedback:

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.profile = cls.fc.fd["profile"]
        cls.feedback = cls.fc.fd["feedback"]
        cls.fc.hpx = True

    def test_01_verify__redirection_on_tapping_feedback(self):
        """
        Description: C42423221
            Install and launch the app
            navigate to rootview 
            tap on avatar 
            tap on feedback observe
        Expected Result:
            Should be redirected to feedback page
        """
        self.fc.go_home(stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_avatar_btn()
        self.profile.click_profile_feedback_btn()
        self.feedback.verify_feedback_page_title()

    def test_02_empty_feedback_screen(self):
        """
        Description: C51926530
            Install and launch the app
            navigate to rootview 
            tap on avatar 
            tap on feedback observe
        Expected Result:
            Submit feedback button should be disabled
        """
        self.driver.swipe()
        assert not self.feedback.is_submit_feedback_btn_enabled()

    def test_03_feedback_form_submission_only_with_mandatory_fields_filled(self):
        """
        Description: C51926531
            Install and launch the app 
            Navigate to rootview 
            Tap avatar on top bar 
            Navigate user to global side layout 
            Tap on feedback button
            Navigate to Feedback form
            Input all the mandatory fields 
            Fill star rating 
            Tap on Send feedback button
        Expected Result:
            Verify user is able to submit the feedback form successfully.
        """
        self.driver.terminate_app(i_const.BUNDLE_ID.SMART)
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.home.click_avatar_btn()
        self.profile.click_profile_feedback_btn()
        self.feedback.click_feedback_five_star_rating_btn()
        self.feedback.click_why_did_you_open_the_app_today_dropdown()
        # Later, need to be implemented to select the list items. AIOI-27663
        self.driver.touch_action.long_press(x=330, y=443, duration=200).release().perform()
        self.feedback.click_whats_your_feedback_related_to_dropdown()
        self.driver.touch_action.long_press(x=330, y=576, duration=200).release().perform()
        self.driver.swipe()
        assert self.feedback.is_submit_feedback_btn_enabled()
        self.feedback.click_submit_btn()
        self.feedback.verify_successful_feedback_submission_text()

    def test_04_verify_user_is_able_to_submit_feedback_successfully_with_mandatory_and_optional_fields_filled(self):
        """
        Description: C42423222
            Install and launch the app 
            Navigate to rootview 
            Tap avatar on top bar and navigate user to global side layout 
            Tap on feedback button and navigate to Feedback form. 
            Input all the mandatory fields 
            Fill star rating 
            Observe Tap on Send feedback button
        Expected Result:
            Verify user is able to submit the feedback form successfully.
        """
        self.driver.terminate_app(i_const.BUNDLE_ID.SMART)
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.home.click_avatar_btn()
        self.profile.click_profile_feedback_btn()
        self.feedback.click_feedback_five_star_rating_btn()
        self.feedback.click_why_did_you_open_the_app_today_dropdown()
        # Later, need to be implemented to select the list items. AIOI-27663
        self.driver.touch_action.long_press(x=330, y=443, duration=200).release().perform()
        self.feedback.click_whats_your_feedback_related_to_dropdown()
        self.driver.touch_action.long_press(x=330, y=576, duration=200).release().perform()
        self.driver.swipe()
        self.feedback.type_in_feedback_help_us_improve_text_area(text="Sample feedback text for testing purpose")
        self.feedback.type_in_can_we_contact_you_text_box(text="sample_test@yopmail.com")
        self.feedback.click_submit_btn()
        self.feedback.verify_successful_feedback_submission_text()

    def test_05_help_us_improve_text_box_max_character_count_and_behaviour(self):
        """
        Description: C51926682
            Install and launch the app 
            Navigate to rootview 
            Tap on avatar 
            Tap on feedback and navigate to Feedback page. 
            Input all the mandatory fields 
            Start entering characters in optional field the 'Help us improve by ...." 
            Observe the behavior
        Expected Result:
            User should able to type 2000 characters in the text box not additional characters should be added.
        """
        self.driver.terminate_app(i_const.BUNDLE_ID.SMART)
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.home.click_avatar_btn()
        self.profile.click_profile_feedback_btn()
        self.feedback.click_feedback_five_star_rating_btn()
        self.feedback.click_why_did_you_open_the_app_today_dropdown()
        # Later, need to be implemented to select the list items. AIOI-27663
        self.driver.touch_action.long_press(x=330, y=443, duration=200).release().perform()
        self.feedback.click_whats_your_feedback_related_to_dropdown()
        self.driver.touch_action.long_press(x=330, y=576, duration=200).release().perform()
        self.driver.swipe()
        chars = string.ascii_letters + string.digits
        random_text = ''.join(random.choices(chars, k=2000))
        self.feedback.type_in_feedback_help_us_improve_text_area(text=random_text)
        self.feedback.click_submit_btn()
        self.feedback.verify_successful_feedback_submission_text()

    def test_06_verify_the_behavior_of_hp_privacy_statement_link(self):
        """
        Description: C51926721
            Install and launch the app 
            Navigate to rootview 
            Tap on avatar Tap on feedback and navigate to Feedback page. 
            Tap on 'HP Privacy Statement' link
        Expected Result:
            Verify HP Privacy page (URL https://www.hp.com/go/privacy) is opened in external browser
        """
        self.driver.terminate_app(i_const.BUNDLE_ID.SMART)
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.home.click_avatar_btn()
        self.profile.click_profile_feedback_btn()
        self.driver.swipe()
        self.feedback.click_hp_privacy_statement_link()
        assert "hp.com" in self.feedback.get_hp_privacy_statement_link_url(), "The expected URL contains 'hp.com' but the actual URL is: {}".format(self.feedback.get_hp_privacy_statement_link_url())

    def test_07_verify_the_error_message_when_an_invalid_email_id_entered(self):
        """
        Description: C51926767
            Install and launch the app 
            Navigate to rootview 
            Tap on avatar 
            Tap on feedback and navigate to Feedback page. 
            Input all the mandatory fields 
            Enter an invalid email address 
            Observe the behavior
        Expected Result:
            Verify the error message is displayed
        """
        self.driver.terminate_app(i_const.BUNDLE_ID.SMART)
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.home.click_avatar_btn()
        self.profile.click_profile_feedback_btn()
        self.feedback.click_feedback_five_star_rating_btn()
        self.feedback.click_why_did_you_open_the_app_today_dropdown()
        # Later, need to be implemented to select the list items. AIOI-27663
        self.driver.touch_action.long_press(x=330, y=443, duration=200).release().perform()
        self.feedback.click_whats_your_feedback_related_to_dropdown()
        self.driver.touch_action.long_press(x=330, y=576, duration=200).release().perform()
        self.driver.swipe()
        self.feedback.type_in_feedback_help_us_improve_text_area(text="Sample feedback text for testing purpose")
        self.feedback.type_in_can_we_contact_you_text_box(text="sample_test.com")
        self.feedback.click_submit_btn()
        self.feedback.is_invalid_email_error_message()
        assert not self.feedback.is_submit_feedback_btn_enabled()

    def test_08_verify_banner_when_feedback_is_submitted_successfully(self):
        """
        Description: C51926775
            Install and launch the app 
            Navigate to rootview 
            Tap on avatar 
            Tap on feedback and navigate to Feedback page. 
            Input all the mandatory fields 
            Fill star rating 
            Tap on Send feedback button
        Expected Result:
            Verify user is able to submit the feedback form successfully and the banner is displayed.
        """
        self.driver.terminate_app(i_const.BUNDLE_ID.SMART)
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.home.click_avatar_btn()
        self.profile.click_profile_feedback_btn()
        self.feedback.click_feedback_five_star_rating_btn()
        self.feedback.click_why_did_you_open_the_app_today_dropdown()
        # Later, need to be implemented to select the list items. AIOI-27663
        self.driver.touch_action.long_press(x=330, y=443, duration=200).release().perform()
        self.feedback.click_whats_your_feedback_related_to_dropdown()
        self.driver.touch_action.long_press(x=330, y=576, duration=200).release().perform()
        self.driver.swipe()
        assert self.feedback.is_submit_feedback_btn_enabled()
        self.feedback.click_submit_btn()
        self.feedback.verify_successful_feedback_submission_text()

    @pytest.mark.parametrize("iteration", range(5))
    def test_9_verify_the_max_submission_per_user_per_day(self, iteration):
        """
        Description: C51926768
            Install and launch the app 
            Navigate to rootview 
            Tap on avatar 
            Tap on feedback 
            Observe the tooltip
        Expected Result:
            Verify the tooltip is displayed
        """
        if iteration == 0:
            self.driver.terminate_app(i_const.BUNDLE_ID.SMART)
            self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.feedback.click_feedback_five_star_rating_btn()
        self.feedback.click_why_did_you_open_the_app_today_dropdown()
        # Later, need to be implemented to select the list items. AIOI-27663
        self.driver.touch_action.long_press(x=330, y=443, duration=200).release().perform()
        self.feedback.click_whats_your_feedback_related_to_dropdown()
        self.driver.touch_action.long_press(x=330, y=576, duration=200).release().perform()
        self.driver.swipe()
        self.feedback.click_submit_btn()
        self.feedback.verify_successful_feedback_submission_text()
        if iteration == 4:
            self.feedback.click_feedback_back_btn()
            self.profile.click_profile_feedback_btn()
            # User is able to submit more than 5 feedback forms so unable to verify the tooltip AIOI-27672

    def test_10_verify_user_is_able_to_navigate_back_from_feedback_form_screen(self):
        """
        Description: C42423223
            Install and launch the app 
            Navigate to rootview 
            Tap on avatar 
            Tap on feedback and navigate to Feedback page. 
            Tap on Menu button
        Expected Result:    
            Verify user is navigated back to Profile page
        """
        self.driver.terminate_app(i_const.BUNDLE_ID.SMART)
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.home.click_avatar_btn()
        self.profile.click_profile_feedback_btn()
        self.feedback.verify_feedback_page_title()
        self.feedback.click_feedback_back_btn()
        self.profile.verify_profile_close_btn()
        self.profile.verify_profile_subcription_link()
        self.profile.verify_hpx_profile_feedback_btn()