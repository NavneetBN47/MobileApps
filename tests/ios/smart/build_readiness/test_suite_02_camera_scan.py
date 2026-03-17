import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_02_Camera_Scan:

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

        # Initializing Printer
        cls.p = load_printers_session
        cls.printer_name = cls.p.get_printer_information()["bonjour name"]
        cls.home = cls.fc.fd["home"]
        cls.camera = cls.fc.fd["camera"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.scan = cls.fc.fd["scan"]

    def test_01_verify_camera_scan_with_photo_preset(self):
        """
        Description:C50698990
            Camera scan with 'Photo' preset
                Launch the app.
                Tap on camera Scan tile and select 'Photo' preset.
                Capture a photo and go to preview screen.
        Expected Result:
            Verifiy the 'Auto' option is "Off" by default.
            The scan job with 'Photo' preset can be captured successfully.
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.select_preset_mode(self.camera.PHOTO)
        self.camera.verify_manual_capture_mode()
        self.camera.select_capture_btn()
        self.common_preview.nav_detect_edges_screen()
        self.common_preview.verify_preview_screen()

    def test_02_verify_camera_scan_and_print(self):
        """ Description: C50698991
                E2E - camera scan and print
                    Launch the app
                    Sign in to your account
                    Navigate to app home screen
                    Add printer to carousal
                    Tap on Camera Scan tile
                    Select 'Batch' option
                    Scan the files
                    Navigate to landing page
                    tap on Save
            Expected Result:
                Verify the scan job can be completed successfully.
                The scanned files can be saved successfully.
        """
        self.fc.go_home()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.select_preset_mode(self.camera.BATCH)
        self.camera.verify_auto_btn()
        assert self.camera.verify_auto_capture_mode()
        self.scan.select_scan_job_button()

    def test_03_verify_input_source(self):
        """
        C50698992: E2E - ADF scan and share (Document Feeder)
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_source_button()
        self.camera.select_source_option(self.camera.OPTION_SCANNER, self.printer_name)
        self.scan.verify_scanner_screen()
        self.scan.select_scan_settings_wheel()
        self.scan.select_input_source()
        self.scan.verify_input_source_options()
        self.scan.select_input_source_option(self.scan.DOCUMENT_FEEDER)
        self.scan.select_navigate_back()
        self.scan.select_done()
        self.scan.select_preview_on_scanner_screen()
        self.scan.verify_preview_not_supported_message()
        self.scan.select_scan_job_button(verify_messages=False)
        self.scan.verify_document_feeder_scan()