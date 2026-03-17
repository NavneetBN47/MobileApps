import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_14_Sanity_Printer_Card(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]
        cls.build_version = cls.driver.session_data["app_info"][pytest.app_info].split('_')[1]


    @pytest.mark.smoke
    def test_01_check_printer_on_printer_weight_C43994039(self):
        """
        Verify when user launch the application 'Added device' should be displayed in the widget.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43994039
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)

    @pytest.mark.smoke
    def test_02_check_printer_model_name_C43994396(self):
        """
        Verify the 'Printer model name' in the widget.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43994396
        """
        #Can't locate the model name element from HPX, so use friend name instead this test. Model name checked on verify_windows_dummy_printer
        assert self.printer_name in self.fc.fd["devicesMFE"].verify_printer_friend_name()

    @pytest.mark.smoke
    def test_03_verify_printer_widget_position_C43994392(self):
        """
        Verify the 'Printer widget' position. 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43994392
        """
        printer_info = self.fc.fd["devicesMFE"].get_first_printer_device_card_info()
        assert self.printer_name in printer_info

    @pytest.mark.smoke
    def test_04_click_printer_card_C43994442(self):
        """
        Verify the 'Printer device page' when user click on 'Pinter Card'. 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43994442
        """
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)