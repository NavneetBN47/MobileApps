import pytest

pytest.app_info = "GOTHAM"
class Test_Suite_04_Feedback_Input_Character(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup


        cls.home = cls.fc.fd["home"]
        cls.feedback = cls.fc.fd["feedback"]

    def test_01_input_all_character_printer_model(self):
        """
        TextBox: Printer model

        Input single byte(English char), double byte(Chinese char), and special char(~!@#$%^&*()_+{}|":?><,) in both text/input fields.
        Verify all characters can be input.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29964365
        """
        english_char = "Thisisatest"
        chinese_char = "這是一個測試"
        special_char = "~!@#$%^&*()_+{|}\":?><,"
        input_char = english_char + chinese_char + special_char
        self.fc.go_home()
        self.home.select_app_settings_btn()
        self.home.select_send_feedback_listview()
        self.feedback.verify_feedback_screen()
        self.feedback.select_dropdown_listitem(self.feedback.MODEL, "Other")
        model_textbox = self.feedback.write_printer_model(input_char)

        assert english_char in model_textbox.text
        assert chinese_char in model_textbox.text
        assert special_char in model_textbox.text

    def test_01_input_all_character_additional_feedback(self):
        """
        TextBox: Additional feedback

        Input single byte(English char), double byte(Chinese char), and special char(~!@#$%^&*()_+{}|":?><,) in both text/input fields.
        Verify all characters can be input.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29964365
        """
        english_char = "Thisisatest"
        chinese_char = "這是一個測試"
        special_char = "~!@#$%^&*()_+{|}\":?><,"
        input_char = english_char + chinese_char + special_char

        additional_feedback = self.feedback.write_additional_opinion(input_char)

        assert english_char in additional_feedback.text
        assert chinese_char in additional_feedback.text
        assert special_char in additional_feedback.text

    # def test_02_invalid_email_address(self):
    #     """
    #     Verify red text shows under the "What is your email address?" text/input field
    #     after clicking submit button with an invalid email address.
        
    #     TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29889372
    #     """
        # It can input invalid email address now.
        # Need to wait for the defect fixed.
        self.driver.swipe()
        self.feedback.select_email_back(0)
        self.feedback.input_email_address("test")
        self.feedback.click_submit_btn_for_invalid_email_test()
        self.feedback.verify_invalid_address_text()
    