import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_10_Printing_File_Formats(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)

        # Initializing Printer
        cls.p = load_printers_session
        cls.sys_config = ma_misc.load_system_config_file()

        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.common_preview = cls.fc.fd["common_preview"]

        # Define variables
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", instant_ink=True, smart_advance=True)
        cls.username, cls.password = cls.login_info["email"], cls.login_info["password"]
        def clean_up_class():
            cls.fc.go_hp_smart_files_and_delete_all_files()
        request.addfinalizer(clean_up_class)

    @pytest.mark.parametrize("file_format", ["jpg", "png", "heif", "tif", "pdf", "txt", "docx"])
    def test_01_verify_printing_different_file_formats(self, file_format):
        """
        IOS & MAC:
        Description: C31297402 - JPG, C31297403 - PNG, C39048788 - HEIF, C31297405 - TIFF, C31297397 - PDF, C31297398 - TXT, C31297399 - DOC
         1. Load Home screen
         2. Connect to target printer
         3. At Home screen, Scan and save a file by file format(JPG, PNG, HEIF, TIF, .PDF, .TXT, .DOC format)
         4. Click on View & Print folder
         5. Select a file from HP Smart files folder
         6. Click on Print Preview button
         7. Click on Print button

         Expected Results:
         7. Verifying the printing job is completed
        """
        file_types = {
            "jpg": "jpg",
            "png": "PNG",
            "heif": "HEIF",
            "tif": "TIF",
            "pdf": "PDF",
            "txt": "txt",
            "docx": "docx"
        }
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.scan_and_save_file_in_hp_smart_files(self.p, file_name=file_types[file_format], no_of_pages=1, file_type=file_types[file_format])
        self.fc.select_a_file_and_go_to_print_preview(file_name=file_types[file_format], file_type=file_format)
        self.fc.select_print_button_and_verify_print_job(self.p)
        self.common_preview.select_done()  # after print job we are clicking done button to go back to home screen, so that we can delete the file
