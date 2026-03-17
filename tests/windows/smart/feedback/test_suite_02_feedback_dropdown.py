import pytest

pytest.app_info = "GOTHAM"
class Test_Suite_02_Feedback_Dropdown(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup


        cls.home = cls.fc.fd["home"]
        cls.feedback = cls.fc.fd["feedback"]

        
    def test_01_main_reason_dropdown(self):
        """
        "What was the main reason you used the HP Smart app today?"

        Verify "Please select option" string display in the box of the main reason.
        Verify below options display after clicking the dropdown box of the main reason.
        Verify the options can be selected.

            - Print business documents
            - Print personal documents
            - Print photos
            - Scan documents
            - Scan photos
            - Using Smart Tasks
            - Managing my supplies (e.g., Instant Ink)
            - Technical support
            - Other

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15142457
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/15142461    
        """
        self.fc.go_home()
        self.home.select_app_settings_btn()
        self.home.select_send_feedback_listview()
        self.feedback.verify_feedback_screen()
        self.feedback.select_reason_dropdown()

        reason = ["Print business documents", "Print personal documents", \
                "Print photos", "Scan documents", "Scan photos", \
                "Using Shortcuts", "Managing my supplies", "Technical support", \
                "Other"]

        for item in reason:
            el = self.feedback.verify_dropdown_listitem(item)
            assert el.get_attribute("IsEnabled").lower() == "true"

        self.feedback.click_feedback_page_title()

    def test_02_gender_dropdown(self):
        """
        "Please tell us more about yourself (optional):" / Gender

        Verify "Please select option" string display in the box of gender.
        Verify below options display after clicking the dropdown of gender.
        Verify the options can be selected.

            - Male
            - Female
            - Prefer not to answer
            - Not listed

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15142457
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/15142461 
        """
        self.feedback.select_gender_dropdown()

        gender = ["Male", "Female", "Prefer not to answer", "Not listed"]

        for item in gender:
            el = self.feedback.verify_dropdown_listitem(item)
            assert el.get_attribute("IsEnabled").lower() == "true"

        self.feedback.click_additional_opinion_title()

    def test_03_age_dropdown(self):
        """
        "Please tell us more about yourself (optional):" / Age Range

        Verify "Please select option" string display in the box of age.
        Verify below options display after clicking the dropdown of age.
        Verify the options can be selected.

            - Under 18
            - 18-24 years
            - 25-34 years
            - 35-50 years
            - 51-65 years
            - Over 65 years
            - Prefer not to answer

        TestRails-> https://hp-testrail.external.hp.com/index.php?/cases/view/15142457
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/15142461
        """
        self.feedback.select_age_range_dropdown()

        age = ["Under 18", "18-24 years", "25-34 years", "35-50 years", \
            "51-65 years", "Over 65 years", "Prefer not to answer"]

        for item in age:
            el = self.feedback.verify_dropdown_listitem(item)
            assert el.get_attribute("IsEnabled").lower() == "true"
