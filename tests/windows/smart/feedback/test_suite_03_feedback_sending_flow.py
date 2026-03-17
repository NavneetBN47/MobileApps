import pytest


pytest.app_info = "GOTHAM"
class Test_Suite_03_Feedback_Sending_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup


        cls.home = cls.fc.fd["home"]
        cls.feedback = cls.fc.fd["feedback"]


    def test_01_verify_thank_you_screen(self):
        """
        Verify "Thank you for your feedback!" screen shows after clicking submit btn.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541025
        """
        self.fc.go_home()
        self.home.select_app_settings_btn()
        self.home.select_send_feedback_listview()
        self.feedback.verify_feedback_screen()
        self.feedback.select_satisfication_stars(3)
        self.feedback.select_dropdown_listitem(self.feedback.REASON, "Scan documents")
        self.feedback.select_recommendation(8)
        self.feedback.select_dropdown_listitem(self.feedback.MODEL, "Other")
        self.feedback.write_printer_model("test")
        self.feedback.select_dropdown_listitem(self.feedback.GENDER, "Female")
        self.feedback.select_dropdown_listitem(self.feedback.AGE, "25-34 years")
        self.feedback.select_email_back(0)
        self.feedback.input_email_address("test@test.com")
        self.feedback.write_additional_opinion("This is a test.")
        self.feedback.select_submit_btn()

        self.feedback.verify_thank_you_feedback_screen()

    def test_02_verify_land_on_home_page(self):
        """
        Verify main UI shows after clicking "Done" button on "Thank you for your feedback!" screen

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541028
        """
        self.feedback.select_done_btn()
        self.home.verify_home_screen()
