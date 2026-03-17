import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_05_Send_Feedback(object):
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

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.skip_in_prod
    def test_01_verify_functionality_of_first_dropdown_menu_C53681229(self):
        self.devicesMFE.verify_profile_icon_show_up()
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_feedback_btn(), "feedback button invisible"
        self.profile.click_feedback_btn()
        self.feedback.verify_why_did_you_open_app_today_list()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        self.feedback.select_each_option_from_first_dropdown_menu()
        self.feedback.click_why_did_you_open_today_options()
    
    @pytest.mark.regression
    def test_02_verify_text_box_accepts_and_displays_user_input_C62132636(self):
        self.devicesMFE.click_profile_button()
        self.profile.verify_feedback_btn()
        self.profile.click_feedback_btn()
        chars_2001_length_for_testing = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789
        `~!@#$%^&*()-_=+[]{}|\;:'",<.>/? ABCDEFGHIJKLMNOPQRSTUVWXYZabc
        defghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+[]{}|\;:'",<.>/?
        ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!
        @#$%^&*()-_=+[]{}|\;:'",<.>/? ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijkl
        mnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+[]{}|\;:'",<.>/? ABCDEFGHIJK
        LMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+[]
        {}|\;:'",<.>/? ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01
        23456789`~!@#$%^&*()-_=+[]{}|\;:'",<.>/? ABCDEFGHIJKLMNOPQRSTUVWXYZab
        cdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+[]{}|\;:'",<.>/? AB
        CDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&
        *()-_=+[]{}|\;:'",<.>/? ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrs
        tuvwxyz0123456789`~!@#$%^&*()-_=+[]{}|\;:'",<.>/? ABCDEFGHIJKLMNOPQRST
        UVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+[]{}|\;:'",<
        .>/? ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!
        @#$%^&*()-_=+[]{}|\;:'",<.>/? ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn
        opqrstuvwxyz0123456789`~!@#$%^&*()-_=+[]{}|\;:'",<.>/? ABCDEFGHIJKLMNO
        PQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+[]{}|\;
        :'",<.>/? ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz012345678
        9`~!@#$%^&*()-_=+[]{}|\;:'",<.>/? ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk
        lmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+[]{}|\;:'",<.>/? ABCDEFGHIJKLM
        NOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+[]{}|\lo
        ;:'",<.>/? ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789
        `~!@#$%^&*()-_=+[]{}|\;:'",<.>/? ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn
        opqrstuvwxyz0123456789`~!@#$%^&*()-_=+[]{}|\;:'",<.>/? ABCDEFGHIJKLMNOPQR
        STUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+[]{}|\;:'",<.
        >/? ABCDEFGHIJKLMNOPQR"""
        self.feedback.input_tell_your_experience(chars_2001_length_for_testing)
        logging.info("Length of chars_2001_length_for_testing is: {}".format(len(chars_2001_length_for_testing)))
        char_count_text = self.feedback.get_feedback_text_char_count() # Characters used: 0 / 2000
        assert "Characters used: 2000 / 2000" == char_count_text, "Character count text is mismatching/wrong"