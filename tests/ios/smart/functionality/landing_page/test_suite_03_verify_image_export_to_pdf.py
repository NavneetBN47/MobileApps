import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_03_Verification_Image_Export_To_Pdf(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.share = cls.fc.fd["share"]
        cls.home = cls.fc.fd["home"]
        cls.files = cls.fc.fd["files"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        #Navigate to home
        cls.fc.go_home(button_index=1, stack=cls.stack)
        
        def clean_up_function():
            cls.fc.go_hp_smart_files_and_delete_all_files()
        request.addfinalizer(clean_up_function)

    def test_01_verify_image_export_to_different_size(self):
        """
        verify image export with Actual size - C27655346
        verify image export to Large size - C27655347
        verify image export with Medium size - C27655348
        verify image export to pdf with Small size - C27655349
        """
        self.fc.create_and_save_file_using_camera_scan_and_go_home(file_name="test_file")
        self.fc.select_a_file_and_go_to_preview_screen(file_name="test_file", file_type="jpg")
        file_size_list = ["small", "medium", "large", "actual"]
        file_names = []
        
        for file_size in file_size_list:
            if file_size == "small":
                scale = self.common_preview.FILE_SIZE_SMALL
            elif file_size == "medium":
                scale = self.common_preview.FILE_SIZE_MEDIUM
            elif file_size == "actual":
                scale = self.common_preview.FILE_SIZE_ACTUAL
            else:
                scale = self.common_preview.FILE_SIZE_LARGE
            # export image to pdf   
            self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
            file_name = f"test_file_{file_size}"
            self.common_preview.rename_file(file_name)
            file_names.append(f"{file_name}.pdf")
            self.common_preview.select_file_type(self.common_preview.BASIC_PDF)
            self.common_preview.verify_file_type_selected("Basic PDF", raise_e=True)
            self.common_preview.verify_an_element_and_click(self.common_preview.FILE_SIZE, click=True)
            self.common_preview.verify_an_element_and_click(scale, click=True)
            self.common_preview.select_navigate_back()
            self.common_preview.select_button(self.common_preview.SHARE_SAVE_BTN)
            self.share.verify_share_popup()
            self.fc.save_file_and_handle_pop_up()
        self.common_preview.select_navigate_back()
        self.home.select_cancel()
        self.fc.go_hp_smart_files_screen_from_home()
        for file_name in file_names:
            # Validate file saved with selected format
            self.files.verify_file_name_exists(file_name)