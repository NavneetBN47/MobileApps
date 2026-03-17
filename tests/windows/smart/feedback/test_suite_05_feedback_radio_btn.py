import pytest


pytest.app_info = "GOTHAM"
class Test_Suite_05_Feedback_Radio_Button(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.feedback = cls.fc.fd["feedback"]


    def test_01_radio_btn_selectable(self):
        """
        Verify the radio option under 
        "How likely are you to recommend HP Smart to a friend or co-worker?" string 
        can be selected.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15142462        
        """
        self.fc.go_home()
        self.home.select_app_settings_btn()
        self.home.select_send_feedback_listview()
        self.feedback.verify_feedback_screen()
        for idx in range(11):
            el = self.feedback.verify_recommendation_radio_btn(idx)

            assert el.get_attribute("IsEnabled").lower() == 'true'
