import logging
import re
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
import pytest
import time
from MobileApps.libs.ma_misc import conftest_misc

pytest.app_info = "HPX"

language_list_path = ma_misc.get_abs_path("resources/test_data/hpx/locale/language_list.txt")
with open(language_list_path, "r+") as f:
    languages = f.read().split(',')

@pytest.fixture(params=languages)
def language(request):
    return request.param

@pytest.fixture(scope="session", params=["settings_screenshot"])
def screenshot_folder_name(request):
    return request.param


class Test_Suite_Localization(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, publish_hpx_localization_screenshot, screenshot_folder_name):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.close_app()
        cls.fc.launch_app()
        cls.attachment_path = conftest_misc.get_attachment_folder()


    def test_02_setting_module_C33045044(self, language):
        lang_settings = ma_misc.load_json_file("resources/test_data/hpx/settingLocalization.json")[language]["translation"]["Settings"]
        self.fc.myhp_login_startup_for_localization_scripts(language)
        
        # Settings (Header)
        self.fc.fd["navigation_panel"].navigate_to_settings()
        time.sleep(5)
        actual_setting_text = self.fc.fd["settings"].verify_settings_header()
        expected_setting_text = lang_settings["navItem"]
        assert actual_setting_text == expected_setting_text, "Settings text is not matched"
        assert bool(self.fc.fd["settings"].verify_privacy_tab_visible()) is True, "Privacy tab is not available"
        logging.info("setting module open now")
        
        # Privacy (Privacy tab)
        self.fc.fd["settings"].click_privacy_tab()
        actual_privacy_text = self.fc.fd["settings"].get_privacy_text()
        expected_privacy_text = lang_settings["privacy"]
        ma_misc.create_localization_screenshot_folder("settings_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "settings_screenshot/{}_privacy.png".format(language))
        assert actual_privacy_text == expected_privacy_text, "Privacy text is not matched"

        # Privacy (Review privacy options)
        actual_privacyReviewPolicy_text = self.fc.fd["settings"].get_privacyReviewPolicy_text()
        expected_privacyReviewPolicy_text = lang_settings["Privacy"]["reviewPrivacy"]
        assert actual_privacyReviewPolicy_text == expected_privacyReviewPolicy_text, "Review privacy options text is not matched"
 
        # Privacy (HP Privacy Statement)
        privacy_statement_link_text = self.fc.fd["settings"].get_hpPrivacyStatementLink_text()
        actual_privacy_statement_link_text = privacy_statement_link_text.lstrip()
        expected_privacy_statement_link_text = lang_settings["Privacy"]["hpPrivacyStatement"]
        assert actual_privacy_statement_link_text == expected_privacy_statement_link_text, "HP Privacy Statement text is not matched"

        # Privacy (The features in myHP are specifically...)        
        actual_detail_text = self.fc.fd["settings"].get_theFeature_text()
        expected_detail_text = lang_settings["Privacy"]["privacyContent"]
        assert actual_detail_text == expected_detail_text, "The features in myHP are specifically text is not matched"

        # Privacy (To learn more go to)        
        actual_learn_more_go_text = self.fc.fd["settings"].get_learn_more_go_text()
        expected_learn_more_go_text = lang_settings["Privacy"]["learnMore"]
        assert actual_learn_more_go_text == expected_learn_more_go_text, "To learn more go to text is not matched"
        
        # Privacy (HP System Information Data Collection)
        system_info_text = self.fc.fd["settings"].get_hpSystemLink_text()
        actual_system_info_text = system_info_text.replace("External Link", "")
        expected_system_info_text = lang_settings["Privacy"]["hpInformation"]
        assert actual_system_info_text == expected_system_info_text, "HP System Information Data Collection text is not matched"

        # Privacy (To review your privacy settings, )        
        actual_policy_setting = self.fc.fd["settings"].get_privacy_setting()
        expected_policy_setting = lang_settings["Privacy"]["reviewPrivacySettings"]
        assert actual_policy_setting == expected_policy_setting, "To review your privacy settings text is not matched"
        
        # Privacy (click here.)
        actual_hpPrivacySetting_text = self.fc.fd["settings"].get_hpPrivacySetting_text()
        expected_hpPrivacySetting_text = lang_settings["Privacy"]["clickHere"]
        assert actual_hpPrivacySetting_text == expected_hpPrivacySetting_text, "click here text is not matched"
               
        # Notifications (Notifications tab)
        self.fc.fd["settings"].click_notification_module()
        actual_notification_text = self.fc.fd["settings"].get_notification_text()
        expected_notification_text = lang_settings["notifications"]
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "settings_screenshot/{}_notification.png".format(language))
        assert actual_notification_text == expected_notification_text, "Notifications text is not matched"
        
        # Notifications (Manage notifications)
        actual_manage_notifications_text = self.fc.fd["settings"].get_manage_notifications()
        expected_manage_notifications_text = lang_settings["Notifications"]["title"]
        assert actual_manage_notifications_text == expected_manage_notifications_text, "Manage notifications text is not matched"

        # Notifications (Modify your notification preferences...)
        actual_modify_text = self.fc.fd["settings"].get_modify_notification()
        expected_modify_text = lang_settings["Notifications"]["description"]
        assert actual_modify_text == expected_modify_text, "Modify your notification preferences text is not matched"

        # Notifications (Desktop Notifications)
        actual_desktop_notifications_text = self.fc.fd["settings"].get_desktop_notification()
        expected_desktop_notifications_text = lang_settings["Notifications"]["desktop"]
        assert actual_desktop_notifications_text == expected_desktop_notifications_text, "Desktop Notifications text is not matched"
       
        # Notifications (Device and account)
        actual_device_account_title = self.fc.fd["settings"].get_device_account_title()
        expected_device_account_title = lang_settings["Notifications"]["device"]["title"]
        assert actual_device_account_title == expected_device_account_title, "Device and account text is not matched"

        # Notifications (Updates and support alerts...)
        actual_device_account_description = self.fc.fd["settings"].get_device_account_description()
        expected_device_account_description = lang_settings["Notifications"]["device"]["description"]
        assert actual_device_account_description == expected_device_account_description, "Updates and support alerts text is not matched"

        # Notifications (Tips and tutorials)
        actual_tips_tutorials_title = self.fc.fd["settings"].get_tips_tutorial_title()
        expected_tips_tutorials_title = lang_settings["Notifications"]["tips"]["title"]
        assert actual_tips_tutorials_title == expected_tips_tutorials_title, "Tips and tutorials text is not matched"

        # Notifications (Learn how to get the best...)
        actual_tips_tutorials_description = self.fc.fd["settings"].get_tips_tutorial_description()
        expected_tips_tutorials_description = lang_settings["Notifications"]["tips"]["description"]
        assert actual_tips_tutorials_description == expected_tips_tutorials_description, "Learn how to get the best text is not matched"

        # Notifications (News and offers)
        actual_news_offers_title = self.fc.fd["settings"].get_news_offers_title()
        expected_news_offers_title = lang_settings["Notifications"]["news"]["title"]
        assert actual_news_offers_title == expected_news_offers_title, "News and offers text is not matched"

        # Notifications (Information about new products, services...)
        actual_news_offers_description = self.fc.fd["settings"].get_news_offers_description()
        expected_news_offers_description = lang_settings["Notifications"]["news"]["description"]
        assert actual_news_offers_description == expected_news_offers_description, "Information about new products, services text is not matched"

        # Notifications (Share your feedback)
        actual_share_feedback_title = self.fc.fd["settings"].get_share_feedback_title()
        expected_share_feedback_title = lang_settings["Notifications"]["share"]["title"]
        assert actual_share_feedback_title == expected_share_feedback_title, "Share your feedback text is not matched"

        # Notifications (Help us improve your experience...)
        actual_share_feedback_description = self.fc.fd["settings"].get_share_feedback_description()
        expected_share_feedback_description = lang_settings["Notifications"]["share"]["description"]
        assert actual_share_feedback_description == expected_share_feedback_description, "Help us improve your experience text is not matched"

        # Feedback (Feedback tab)
        self.fc.fd["settings"].click_feedback_tab()
        actual_feedback_tab_text = self.fc.fd["settings"].get_feedback_tab()
        expected_feedback_tab_text = lang_settings["feedback"]
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "settings_screenshot/{}_feedback.png".format(language))
        assert actual_feedback_tab_text == expected_feedback_tab_text, "Feedback text is not matched"

        # Feedback (Share your feedback with us)
        actual_feedback_title = self.fc.fd["settings"].get_feedback_title()
        expected_feedback_title = lang_settings["Feedback"]["title"]
        assert actual_feedback_title == expected_feedback_title, "Share your feedback with us text is not matched"

        # Feedback (Please provide feedback to let us know how we're doing.)
        actual_feedback_description = self.fc.fd["settings"].get_feedback_description()
        expected_feedback_description = lang_settings["Feedback"]["description"]
        assert actual_feedback_description == expected_feedback_description, "Please provide feedback to let us know how we're doing text is not matched"

        # Feedback (Overall, how satisfied are you with your myHP experience?)
        rating_experience_text = self.fc.fd["settings"].get_rating_experience()
        actual_rating_experience = rating_experience_text.replace(" *", "")
        expected_rating_experience = lang_settings["Feedback"]["ratingExperience"]
        assert actual_rating_experience == expected_rating_experience, "Overall, how satisfied are you with your myHP experience? text is not matched"

        # Feedback ((1 Star = Very unsatisfied, 5 Stars = Very satisfied))
        actual_rating_disclaimer = self.fc.fd["settings"].get_rating_disclaimer()
        expected_rating_disclaimer = lang_settings["Feedback"]["ratingDisclaimer"]
        assert actual_rating_disclaimer == expected_rating_disclaimer, "(1 Star = Very unsatisfied, 5 Stars = Very satisfied) text is not matched"

        # Feedback (Provide any additional feedback)
        actual_additional_feedback = self.fc.fd["settings"].get_additional_feedback()
        expected_additional_feedback = lang_settings["Feedback"]["additionalFeedbackPlaceholder"]
        assert actual_additional_feedback == expected_additional_feedback, "Provide any additional feedback text is not matched"

        # Feedback (The purpose of this survey is to gather...)
        actual_feedback_disclaimer = self.fc.fd["settings"].get_feedback_disclaimer()
        expected_feedback_disclaimer = lang_settings["Feedback"]["feedbackDisclaimer"]
        assert actual_feedback_disclaimer == expected_feedback_disclaimer, "The purpose of this survey is to gather... text is not matched"

        # Feedback (Submit Feedback)
        actual_submit_feedback = self.fc.fd["settings"].get_submit_feedback()
        expected_submit_feedback = lang_settings["Feedback"]["submitFeedback"]
        assert actual_submit_feedback == expected_submit_feedback, "Submit Feedback text is not matched"

        # Feedback (Select a star rating before you submit.)
        self.fc.fd["settings"].click_submit_feedback()
        actual_required_field_error = self.fc.fd["settings"].get_required_field_error()
        expected_required_field_error = lang_settings["Feedback"]["requiredFieldError"]
        assert actual_required_field_error == expected_required_field_error, "Select a star rating before you submit. text is not matched"

        # Feedback (Thank you!)
        self.fc.fd["settings"].click_rating_star_5()
        self.fc.fd["settings"].click_submit_feedback()
        actual_feedback_thankyou = self.fc.fd["settings"].get_feedback_thankyou()
        expected_feedback_thankyou = lang_settings["Feedback"]["feedbackThankYou"]
        assert actual_feedback_thankyou == expected_feedback_thankyou, "Thank you! text is not matched"

        # Feedback (Your valuable feedback help us improve your experience.)
        actual_feedback_thankyou_disclaimer = self.fc.fd["settings"].get_feedback_thankyou_disclaimer()
        expected_feedback_thankyou_disclaimer = lang_settings["Feedback"]["thankYouDisclaimer"]
        assert actual_feedback_thankyou_disclaimer == expected_feedback_thankyou_disclaimer, "Your valuable feedback help us improve your experience. text is not matched"

        # About (About tab)
        self.fc.fd["settings"].click_about_tab_id()
        actual_about_text = self.fc.fd["settings"].get_about_text()
        expected_about_text = lang_settings["about"]
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "settings_screenshot/{}_about.png".format(language))
        assert actual_about_text == expected_about_text, "About text is not matched"
        
        # About (myHP)
        actual_about_myHPtext = self.fc.fd["settings"].verify_about_myHPtext()
        expected_about_myHPtext = lang_settings["About"]["myHP"]
        assert actual_about_myHPtext == expected_about_myHPtext, "myHP text is not matched"
        
        # About (Version)
        self.version_text = self.fc.fd["settings"].get_version_about()
        if language == "th-TH":
            actual_version_text = re.search("([\u0E00-\u0E7F]+)", self.version_text).group(1)
        else:
            actual_version_text = re.search("([\w]{1,10})", self.version_text).group(1)
        expected_version_text = lang_settings["About"]["version"]
        assert actual_version_text == expected_version_text, "Version text is not matched"

        # About (HP Privacy Policy)
        privacylink_text = self.fc.fd["settings"].get_privacyPolicy_text()
        actual_privacy_text = privacylink_text.replace(" External Link", "")
        expected_privacyLink_text = lang_settings["About"]["privacy"]
        assert actual_privacy_text == expected_privacyLink_text, "HP Privacy Policy text is not matched"
        
        # About (HP End User License Agreement)
        user_agreement_text = self.fc.fd["settings"].get_user_agreement_text()
        actual_user_agreement_text = user_agreement_text.replace(" External Link", "")
        expected_user_agreement_text = lang_settings["About"]["license"]
        assert actual_user_agreement_text == expected_user_agreement_text, "HP End User License Agreement text is not matched"
        
        # About (Copyright 2023 HP Development Company, L.P.")
        actual_copy_right_text = self.fc.fd["settings"].get_copr_right_txt_about()
        logging.info("get_copr_right_txt_about=" + str(actual_copy_right_text))
        expected_copy_right_text = lang_settings["About"]["copyright"]
        assert actual_copy_right_text == expected_copy_right_text,"Copyright 2023 HP Development Company, L.P."

        # ending test
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        self.fc.fd["devices"].restore_app()
