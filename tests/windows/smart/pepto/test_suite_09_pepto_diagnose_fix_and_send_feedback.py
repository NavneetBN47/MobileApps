import pytest
from time import sleep
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_09_Pepto_Diagnose_Fix_And_Send_Feedback(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.pepto = cls.fc.fd["pepto"]
        cls.home = cls.fc.fd["home"]
        cls.diagnose_fix = cls.fc.fd["diagnose_fix"]
        cls.feedback = cls.fc.fd["feedback"]
        cls.privacy_settings = cls.fc.fd["privacy_settings"]
        cls.privacy_preference = cls.fc.fd["privacy_preference"]

        cls.build_version = (cls.driver.session_data["app_info"])[pytest.app_info].split('-')[1]
        cls.model_name = cls.p.get_printer_information()["model name"].split('[')[0].strip()
        if 'HP' not in cls.model_name:
            cls.model_name = 'HP ' + cls.model_name

        cls.stack = request.config.getoption("--stack")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)
        
    def test_01_add_printer_and_enable_pepto(self):
        """
        Enable the Pepto log.
        Launch the app to Main UI
        """  
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        sleep(3)
        self.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

        self.pepto.enable_pepto_log(self.build_version)
        assert self.pepto.verify_pepto_log_file_created() == True

    def test_02_diagnose_and_fix(self): 
        """
        Click the "Diagnose & Fix" button from the navigation pane/Menu bar
        Click "Start" button on the diagnose and fix screen
        Finish the diagnose and fix the flow and come back to main UI
        Close the app
        Check pepto Pdsmq.Data.txt file
        """  
        self.home.select_diagnose_and_fix_btn()
        self.home.select_diagnose_and_fix_start_btn()
        self.diagnose_fix.verify_diagnosis_complete_screen()
        self.diagnose_fix.click_done_btn()
        self.home.verify_home_screen()

    def test_03_send_feedback_first_time(self): 
        """
        Go to send feedback option
        Send the Feedback
        Click the "Done" button on the Thank you for your feedback page
        Close the app
        Check pepto Pdsmq.Data.txt file
        """  
        self.home.select_app_settings_btn()
        self.home.select_send_feedback_listview()
        self.feedback.verify_feedback_screen()
        self.feedback.select_satisfication_stars(3)
        self.feedback.select_dropdown_listitem(self.feedback.REASON, "Scan documents")
        self.feedback.select_recommendation(8)
        self.feedback.select_dropdown_listitem(self.feedback.MODEL, "Other")
        self.feedback.select_submit_btn()
        self.feedback.select_done_btn()
        self.home.verify_home_screen()

        sleep(1)
        self.driver.terminate_app()

    def test_04_check_pepto_data(self):
        """
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24703200
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15961232
        """ 
        check_event_list = ['{"schema":"app_eventinfo/2.0.1","app_event_actor":"user","app_event_action":"clicked","app_event_object":"tile","app_event_object_label":"/GroupFunctions#CustomerFeedback"', '{"schema":"app_eventinfo/2.0.1","app_event_actor":"app","app_event_action":"displayed","app_event_object":"screen","app_event_object_label":"/CustomerFeedback.flow/CustomerFeedbackPage"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_05_disable_pepto(self):
        """
        Relaunch the app
        Disable the pepto via App improvement toggle under the privacy settings

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24703200
        """ 
        self.driver.launch_app()
        sleep(3)
        self.home.select_app_settings_btn()
        self.home.select_privacy_settings_listview()
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)
        self.privacy_preference.click_toggle(self.privacy_preference.APP_ANALYTICS)
        self.privacy_preference.click_toggle(self.privacy_preference.ADVERTISING)
        self.privacy_preference.click_toggle(self.privacy_preference.PERSONALIZED_SUGGESTIONS)
        self.privacy_preference.click_continue()
        self.home.verify_home_screen()

    def test_06_send_feedback_again(self):
        """
        Try to send the feedback again

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24703200
        """ 
        self.home.select_app_settings_btn()
        self.home.select_send_feedback_listview()
        self.feedback.verify_feedback_screen()
        self.feedback.select_satisfication_stars(3)
        self.feedback.select_dropdown_listitem(self.feedback.REASON, "Scan documents")
        self.feedback.select_recommendation(8)
        self.feedback.select_dropdown_listitem(self.feedback.MODEL, "Other")
        self.feedback.select_submit_btn()
        self.feedback.verify_thank_you_feedback_screen()
        self.feedback.select_done_btn()
        self.home.verify_home_screen()

        sleep(1)
        self.driver.terminate_app()

    def test_07_check_pepto_data(self):
        """
        Verify "x-cscr_gotham_form_customer_feedback" is available in pepto Pdsmq.Data.txt file

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24703200
        """ 
        check_event_list = ['x-cscr_gotham_form_customer_feedback'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_08_check_pepto_data(self):
        """
        Filled out all info on Send Feedback screen and then click Submit feedback button to go to Thank you... page.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15961233
        """ 
        check_event_list = ['"schema":"app_eventinfo/2.0.1","app_event_actor":"user","app_event_action":"submitted","app_event_object":"form","app_event_object_label":"form_generic"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_09_check_pepto_data(self):
        """
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17169883
        """ 
        check_event_list = [ '"schema":"app_eventinfo/2.0.1","app_event_actor":"user","app_event_action":"clicked","app_event_object":"tile","app_event_object_label":"/GroupFunctions#DiagnoseAndFix"', '"schema":"app_eventinfo/2.0.1","app_event_actor":"app","app_event_action":"displayed","app_event_object":"screen","app_event_object_label":"/DiagnoseAndFix.flow/DiagnoseAndFixStartPage"', '"_dev_modelname":"{0}"'.format(self.model_name), '"launch_from":"shell","action":null', '"drivercheck_result":"{.*}"', '"test_list":"drivercheck","cumulative_state":"StartDiagnose, IssueFoundAndFixed","result":" IssueFoundAndFixed"', '"moniker":"x-cscr_gotham_report_psdrdiagnose_summary/1.0","schema":"app_event_report_generic/1.0.0"}', '"app_event_details":{"launch_from":"diagnose","network_category":"Public"']


        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_10_check_pepto_data(self):
        """
        Start the PSDr via any available entry like Click on the print tiles/ Click on the Diagnose and fix button

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28044128
        """ 
        check_event_list = ['"schema":"app_eventinfo/2.0.1","app_event_actor":"user","app_event_action":"submitted","app_event_object":"form","app_event_object_label":"form_generic"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    