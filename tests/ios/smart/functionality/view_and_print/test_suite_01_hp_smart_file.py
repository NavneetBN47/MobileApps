import pytest
import datetime
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_01_HP_Smart_Files(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.files = cls.fc.fd["files"]
        cls.stack = request.config.getoption("--stack")
        cls.sys_config = ma_misc.load_system_config_file()
        cls.fc.go_home(stack=cls.stack)
        cls.fc.dismiss_tap_here_to_start()

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        self.fc.go_hp_smart_files_screen_from_home()

        def clean_up_class():
            self.fc.go_hp_smart_files_and_delete_all_files()
        request.addfinalizer(clean_up_class)

    def test_01_create_folder(self):
        """
        C27655015
        """
        folder_name = "{}_{:%m%d%H%M}".format("test_01_create_folder", datetime.datetime.now())
        self.files.create_a_folder(folder_name)
        self.files.verify_static_text(f"{folder_name}(0)", raise_e=True)

    def test_02_validate_sort_functionality(self):
        """
        C27655016 sort by name and sort by date
        """
        self.files.create_a_folder(folder_name="z")
        self.files.create_a_folder(folder_name="a")
        self.files.create_a_folder(folder_name="s")
        self.files.create_a_folder(folder_name="b")
        # sort by name
        self.files.select_hp_smart_files_3dot_button()
        self.files.verify_more_options_door()
        self.files.select_sort_by_name_option()
        self.files.verify_folder_order(folder_names=["a", "b", "s", "z"])
        # sort by date
        self.files.select_hp_smart_files_3dot_button()
        self.files.verify_more_options_door()
        self.files.select_sort_by_date_option()
        self.files.verify_folder_order(folder_names=["b", "s", "a", "z"])

    def test_03_validate_search_functionality(self):
        """
        C27655014 verify no search results and happy path search
        """
        folder_name = "{}_{:%m%d%H%M}".format("test_03_validate_search_functionality", datetime.datetime.now())
        self.files.create_a_folder(folder_name=folder_name)
        self.files.enter_search_item_in_search_box("randomfoldername123")
        self.files.verify_no_search_results()
        self.files.my_files_select_search_cancel()
        self.files.enter_search_item_in_search_box(folder_name)
        self.files.verify_static_text(f"{folder_name}(0)", raise_e=True)
    
    def test_04_verify_edit_files_options(self):
        """
        C27655017
        """
        folder_name = "{}_{:%m%d%H%M}".format("test_04_verify_edit_files_options", datetime.datetime.now())
        self.files.create_a_folder(folder_name=folder_name)
        self.files.enter_search_item_in_search_box(folder_name)
        self.files.verify_static_text(f"{folder_name}(0)", raise_e=True)
        self.files.select_dropdown_options_button()
        self.files.verify_menu_door_from_down()
        self.files.verify_ui_options_elements_menu_door_from_down()
    
    def test_05_rename(self):
        """
        C27655018 tap on rename and cancel, then rename the file and verify new name
        """
        folder_name = "{}_{:%m%d%H%M}".format("test_05_rename", datetime.datetime.now())
        self.files.create_a_folder(folder_name=folder_name)
        self.files.find_and_rename_file(folder_name, f"{folder_name}(0)", cancel_rename=True)
        new_name = "{}_{:%m%d%H%M}".format("new_name", datetime.datetime.now())
        self.files.select_clear_text()
        self.files.find_and_rename_file(folder_name, f"{folder_name}(0)", new_name=new_name)
        self.files.select_clear_text()
        self.files.enter_search_item_in_search_box(new_name)
        self.files.verify_static_text(f"{new_name}(0)", raise_e=True)
    
    def test_06_delete_file(self):
        """
        C27655020
        """
        folder_name = "{}_{:%m%d%H%M}".format("test_06_delete_file", datetime.datetime.now())
        self.files.create_a_folder(folder_name=folder_name)
        self.files.delete_a_file(folder_name, cancel_delete=True)
        self.files.select_clear_text()
        self.files.enter_search_item_in_search_box(folder_name)
        self.files.verify_static_text(f"{folder_name}(0)", raise_e=True)
        self.files.select_clear_text()
        self.files.delete_a_file(folder_name)
        assert self.files.is_empty_screen()
    
    def test_07_edit_files_cancel(self):
        """
        C27655021
        """
        folder_name = "{}_{:%m%d%H%M}".format("test_07_edit_files_cancel", datetime.datetime.now())
        self.files.create_a_folder(folder_name=folder_name)
        self.files.enter_search_item_in_search_box(folder_name)
        self.files.select_dropdown_options_button()
        self.files.verify_menu_door_from_down()
        self.files.select_edit_options_cancel_btn()