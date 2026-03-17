import pytest

from SAF.misc.ssh_utils import SSH

pytest.app_info = "GOTHAM"
class Test_Suite_01_Feedback_Links(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.ip_addr = request.config.getoption("--mobile-device")

        cls.home = cls.fc.fd["home"]
        cls.feedback = cls.fc.fd["feedback"]
        cls.printers = cls.fc.fd["printers"]

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        def tab_clean_up():
            self.web_driver.close_window(self.web_driver.current_window)
        request.addfinalizer(tab_clean_up)

    def test_01_users_guide_link(self):
        """
        Verify browser opens to HP Support after clicked "User's guide & FAQ" link.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541061
        """
        webpage = "FAQ"
        self.fc.go_home()
        self.home.select_app_settings_btn()
        self.home.select_send_feedback_listview()
        self.feedback.verify_feedback_screen()
        self.feedback.select_user_guide_faq_link()
        self.web_driver.add_window(webpage)
        
        if webpage not in self.web_driver.session_data["window_table"].keys():
            self.feedback.select_user_guide_faq_link()
            self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)

        current_url = self.web_driver.get_current_url()

        for sub_url in self.feedback.USER_GUIDE_FAQ:
            assert sub_url in current_url

    def test_02_visit_hp_smart_support_forum_link(self):
        """
        Verify browser opens to All support forum topics after clicked "Visit our HP Smart support forum" link.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541062
        """
        webpage = "SMART_FORUM"

        self.feedback.select_hp_support_forum_link()
        self.web_driver.add_window(webpage)

        if webpage not in self.web_driver.session_data["window_table"].keys():
            self.feedback.select_hp_support_forum_link()
            self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)

        current_url = self.web_driver.get_current_url()

        for sub_url in self.feedback.SMART_FORUM:
            assert sub_url in current_url

    def test_03_send_email_link(self):
        """
        Verify "Select Continue below..." dialog pops up with "Cancel" and "Continue" buttons
        after clicked "Send an email to our support team" link.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541063       
        """
        self.feedback.select_send_email_link()

        if self.feedback.verify_email_dialog_title(raise_e=False) is False:
            self.feedback.select_send_email_link()
            
        self.feedback.verify_email_dialog_title()
        self.feedback.verify_email_cancel_btn()
        self.feedback.verify_email_continue_btn()

    def test_04_send_email_cancel_btn(self):
        """
        Verify "Give us your feedback" screen shows after click "Cancel" button on the "Select Continue below..." dialog.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541066
        """
        self.feedback.select_email_cancel_btn()
        assert self.feedback.verify_email_dialog_title(raise_e=False) is False

    def test_05_send_email_continue_btn(self):
        """
        Verify OS default Mail is launched after click "Continue" button on the "Select Continue below..." dialog.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541067
        """
        self.feedback.select_send_email_link()
        self.feedback.select_email_continue_btn()

        ssh = SSH(self.ip_addr, "exec")
        task = ssh.send_command("tasklist /fi 'IMAGENAME eq HxOutlook.exe'")['stdout']
        task = task.split('\r\n')[3].split()[0]
        assert task == "HxOutlook.exe"
        ssh.send_command("taskkill /f /t /im HxOutlook.exe")