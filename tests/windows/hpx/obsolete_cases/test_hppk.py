from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time



pytest.app_info = "HPX"
class Test_Suite_HPPK(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.close_app()
        cls.fc.launch_app()

    @pytest.mark.require_platform(["abandoned_case"])
    def test_01_verify_Programmable_key_C33823225(self):
        self.fc.restart_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)

    @pytest.mark.require_platform(["abandoned_case"])
    def test_02_verify_assign_page_ui_C33823226(self):
        self.fc.restart_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        assert bool(self.fc.fd["hppk"].verify_assign_description()) is True
        assert bool(self.fc.fd["hppk"].verify_hppk_icon()) is True
        assert bool(self.fc.fd["hppk"].verify_add_action()) is True
        assert bool(self.fc.fd["hppk"].verify_add_another()) is True
        assert bool(self.fc.fd["hppk"].verify_save_button()) is True

    @pytest.mark.require_platform(["abandoned_case"])
    def test_03_verify_add_action_items_C33823227(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        assert bool(self.fc.fd["hppk"].verify_circular_1()) is True
        assert bool(self.fc.fd["hppk"].verify_add_action()) is True
        self.fc.fd["hppk"].click_add_action()
        time.sleep(5)
        assert bool(self.fc.fd["hppk"].verify_application()) is True
        assert bool(self.fc.fd["hppk"].verify_website()) is True
        assert bool(self.fc.fd["hppk"].verify_file()) is True
        assert bool(self.fc.fd["hppk"].verify_folder()) is True


    @pytest.mark.require_platform(["abandoned_case"])
    def test_04_verify_add_Application_C33823228(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        assert bool(self.fc.fd["hppk"].verify_add_action()) is True
        self.fc.fd["hppk"].click_add_action()
        assert bool(self.fc.fd["hppk"].verify_application()) is True
        self.fc.fd["hppk"].click_application()
        time.sleep(20)
        self.fc.fd["hppk"].click_applicationsearch()
        self.fc.fd["hppk"].search_application("calculator")
        assert bool(self.fc.fd["hppk"].verify_calculator()) is True
        self.fc.fd["hppk"].click_calculator()
        assert bool(self.fc.fd["hppk"].verify_add_app_button()) is True
        self.fc.fd["hppk"].click_add_app_button()
        time.sleep(5)
        assert bool(self.fc.fd["hppk"].verify_save_button()) is True
        self.fc.fd["hppk"].click_save_button()
        assert bool(self.fc.fd["hppk"].verify_delete1()) is True
        self.fc.fd["hppk"].click_delete1()
        assert bool(self.fc.fd["hppk"].verify_add_action()) is True

    def test_05_verify_add_website_url_C33823229(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        assert bool(self.fc.fd["hppk"].verify_add_action()) is True
        self.fc.fd["hppk"].click_add_action()
        assert bool(self.fc.fd["hppk"].verify_website()) is True
        self.fc.fd["hppk"].click_website()
        assert bool(self.fc.fd["hppk"].verify_website_input()) is True
        self.fc.fd["hppk"].input_url("www.google.com")
        time.sleep(3)
        self.fc.fd["hppk"].click_website_add()
        time.sleep(3)
        self.fc.fd["hppk"].click_save_button()
        assert bool(self.fc.fd["hppk"].verify_delete1()) is True
        self.fc.fd["hppk"].click_delete1()
        assert bool(self.fc.fd["hppk"].verify_add_action()) is True

    @pytest.mark.require_platform(["abandoned_case"])
    def test_06_verify_multiple_add_action_C33831698(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        self.fc.maximize_window()
        assert bool(self.fc.fd["hppk"].verify_add_action()) is True
        assert bool(self.fc.fd["hppk"].verify_circular_1()) is True
        self.fc.fd["hppk"].click_add_another()
        assert bool(self.fc.fd["hppk"].verify_add_action_2()) is True
        assert bool(self.fc.fd["hppk"].verify_circular_2()) is True
        self.fc.fd["hppk"].click_add_another()
        assert bool(self.fc.fd["hppk"].verify_add_action_3()) is True
        assert bool(self.fc.fd["hppk"].verify_circular_3()) is True
        self.fc.fd["hppk"].click_add_another()
        assert bool(self.fc.fd["hppk"].verify_add_action_4()) is True
        assert bool(self.fc.fd["hppk"].verify_circular_4()) is True
        self.fc.fd["hppk"].click_add_another()
        assert bool(self.fc.fd["hppk"].verify_add_action_5()) is True
        assert bool(self.fc.fd["hppk"].verify_circular_5()) is True
        assert bool(self.fc.fd["hppk"].verify_save_button()) is True

    @pytest.mark.require_sanity_check(["sanity"])
    def test_07_verify_website_popup_screen_functionality_C33831652(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        programmable_key_heading = self.fc.fd["hppk"].verify_programmable_key_heading()
        time.sleep(3)
        assert bool(self.fc.fd["hppk"].verify_add_action()) is True
        self.fc.fd["hppk"].click_add_action()
        assert bool(self.fc.fd["hppk"].verify_website()) is True
        self.fc.fd["hppk"].click_website()
        assert bool(self.fc.fd["hppk"].verify_website_close()) is True
        assert bool(self.fc.fd["hppk"].verify_website_add()) is True
        assert bool(self.fc.fd["hppk"].verify_website_cancel()) is True
        self.fc.fd["hppk"].input_url("www.google.com")
        self.fc.fd["hppk"].click_website_close()
        assert programmable_key_heading == "Create personalized shortcuts with the press of a button","Programmable Keyheading is not visible- {}".format(programmable_key_heading)
        self.fc.fd["hppk"].click_add_action()
        self.fc.fd["hppk"].click_website()
        self.fc.fd["hppk"].input_url("www.google.com")
        self.fc.fd["hppk"].click_website_cancel()
        assert programmable_key_heading == "Create personalized shortcuts with the press of a button","Programmable Keyheading is not visible- {}".format(programmable_key_heading)


    @pytest.mark.require_sanity_check(["sanity"])
    def test_08_verify_application_popup_screen_functionality_C33831695(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        programmable_key_heading = self.fc.fd["hppk"].verify_programmable_key_heading()
        time.sleep(3)
        assert bool(self.fc.fd["hppk"].verify_add_action()) is True
        self.fc.fd["hppk"].click_add_action()
        self.fc.fd["hppk"].click_application()
        time.sleep(15)
        self.fc.fd["hppk"].click_applicationsearch()
        self.fc.fd["hppk"].search_application("calculator")
        self.fc.fd["hppk"].click_calculator()
        self.fc.fd["hppk"].click_close_app_button()
        assert programmable_key_heading == "Create personalized shortcuts with the press of a button","Programmable Keyheading is not visible- {}".format(programmable_key_heading)
        self.fc.fd["hppk"].click_add_action()
        self.fc.fd["hppk"].click_application()
        self.fc.fd["hppk"].click_applicationsearch()
        self.fc.fd["hppk"].search_application("calculator")
        self.fc.fd["hppk"].click_calculator()
        self.fc.fd["hppk"].click_cancel_app_button
        assert programmable_key_heading == "Create personalized shortcuts with the press of a button","Programmable Keyheading is not visible- {}".format(programmable_key_heading)


    @pytest.mark.require_sanity_check(["sanity"])
    def test_09_verify_invalid_website_url_C33831609(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        time.sleep(3)
        self.fc.fd["hppk"].click_add_action()
        self.fc.fd["hppk"].click_website()
        self.fc.fd["hppk"].input_url("abcd")
        time.sleep(3)
        assert bool(self.fc.fd["hppk"].verify_website_invalid_url_warning_text()) is True

    def test_10_verify_saved_action_after_restart_C34178791(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(3)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(3)
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        programmable_key_heading = self.fc.fd["hppk"].verify_programmable_key_heading()
        assert programmable_key_heading == "Create personalized shortcuts with the press of a button","Programmable Keyheading is not visible- {}".format(programmable_key_heading)
        self.fc.fd["hppk"].click_add_action()
        self.fc.fd["hppk"].click_website()
        self.fc.fd["hppk"].input_url("www.google.com")
        self.fc.fd["hppk"].click_website_add()
        self.fc.fd["hppk"].click_save_button()
        assert bool(self.fc.fd["hppk"].verify_action_content_box()) is True
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(3)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(3)
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        assert bool(self.fc.fd["hppk"].verify_action_content_box()) is True
        self.fc.fd["hppk"].click_delete1()

    def test_11_verify_delete_functionality_C34180780(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(3)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(3)
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        programmable_key_heading = self.fc.fd["hppk"].verify_programmable_key_heading()
        assert programmable_key_heading == "Create personalized shortcuts with the press of a button","Programmable Keyheading is not visible- {}".format(programmable_key_heading)
        self.fc.fd["hppk"].click_add_action()
        self.fc.fd["hppk"].click_website()
        self.fc.fd["hppk"].input_url("www.google.com")
        self.fc.fd["hppk"].click_website_add()
        self.fc.fd["hppk"].click_save_button()
        self.fc.fd["hppk"].click_add_another()
        time.sleep(3)
        self.fc.fd["hppk"].click_add_action()
        self.fc.fd["hppk"].click_application()
        time.sleep(15)
        self.fc.fd["hppk"].click_applicationsearch()
        self.fc.fd["hppk"].search_application("calculator")
        self.fc.fd["hppk"].click_calculator()
        self.fc.fd["hppk"].click_add_app_button()
        self.fc.fd["hppk"].click_save_button()
        self.fc.fd["hppk"].click_add_another()
        self.fc.fd["hppk"].click_add_action()
        self.fc.fd["hppk"].click_website()
        self.fc.fd["hppk"].input_url("www.google.com")
        self.fc.fd["hppk"].click_website_add()
        self.fc.fd["hppk"].click_save_button()
        self.fc.fd["hppk"].click_add_another()
        self.fc.fd["hppk"].click_add_action()
        self.fc.fd["hppk"].click_website()
        self.fc.fd["hppk"].input_url("www.google.com")
        self.fc.fd["hppk"].click_website_add()
        self.driver.swipe(direction="down", distance=2)
        self.fc.fd["hppk"].click_save_button()
        self.fc.fd["hppk"].click_add_another()
        self.fc.fd["hppk"].click_add_action()
        self.fc.fd["hppk"].click_website()
        self.fc.fd["hppk"].input_url("www.google.com")
        self.fc.fd["hppk"].click_website_add()
        self.fc.fd["hppk"].click_save_button()
        assert bool(self.fc.fd["hppk"].verify_delete1()) is True
        assert bool(self.fc.fd["hppk"].verify_delete2()) is True
        assert bool(self.fc.fd["hppk"].verify_delete3()) is True
        assert bool(self.fc.fd["hppk"].verify_delete4()) is True
        assert bool(self.fc.fd["hppk"].verify_delete5()) is True
        self.fc.fd["hppk"].click_delete1()
        time.sleep(2)
        self.fc.fd["hppk"].click_delete1()
        time.sleep(2)
        self.fc.fd["hppk"].click_delete1()
        time.sleep(2)
        self.fc.fd["hppk"].click_delete1()
        time.sleep(2)
        self.fc.fd["hppk"].click_delete1()
        time.sleep(2)
        assert bool(self.fc.fd["hppk"].verify_add_action()) is True
        assert bool(self.fc.fd["hppk"].verify_add_action_2()) is False


    @pytest.mark.require_platform(["abandoned_case"])
    def test_12_verify_navigating_to_other_tab_before_saving_action_item_C34181375(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(3)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(3)
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        programmable_key_heading = self.fc.fd["hppk"].verify_programmable_key_heading()
        assert programmable_key_heading == "Create personalized shortcuts with the press of a button.","Programmable Keyheading is not visible- {}".format(programmable_key_heading)
        self.fc.fd["hppk"].click_add_action()
        self.fc.fd["hppk"].click_website()
        self.fc.fd["hppk"].input_url("www.google.com")
        self.fc.fd["hppk"].click_website_add()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        programmable_key_heading = self.fc.fd["hppk"].verify_programmable_key_heading()
        assert programmable_key_heading == "Create personalized shortcuts with the press of a button.","Programmable Keyheading is not visible- {}".format(programmable_key_heading)
        self.fc.fd["hppk"].click_add_action()
        assert bool(self.fc.fd["hppk"].verify_add_action()) is True

    @pytest.mark.require_platform(["abandoned_case"])
    def test_13_verify_navigating_to_other_tab_after_saving_action_item_C34181374(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(3)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(3)
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        programmable_key_heading = self.fc.fd["hppk"].verify_programmable_key_heading()
        assert programmable_key_heading == "Create personalized shortcuts with the press of a button.","Programmable Keyheading is not visible- {}".format(programmable_key_heading)
        self.fc.fd["hppk"].click_add_action()
        self.fc.fd["hppk"].click_website()
        self.fc.fd["hppk"].input_url("www.google.com")
        self.fc.fd["hppk"].click_website_add()
        self.fc.fd["hppk"].click_save_button()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        programmable_key_heading = self.fc.fd["hppk"].verify_programmable_key_heading()
        assert programmable_key_heading == "Create personalized shortcuts with the press of a button.","Programmable Keyheading is not visible- {}".format(programmable_key_heading)
        assert bool(self.fc.fd["hppk"].verify_action_content_box()) is True
        assert bool(self.fc.fd["hppk"].verify_add_action()) is False
        self.fc.fd["hppk"].click_delete1()
        assert bool(self.fc.fd["hppk"].verify_add_action()) is True


    @pytest.mark.require_platform(["abandoned_case"])
    def test_14_verify_support_key_icon_C34392561(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(3)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(3)
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        programmable_key_heading = self.fc.fd["hppk"].verify_programmable_key_heading()
        assert programmable_key_heading == "Create personalized shortcuts with the press of a button.","Programmable Keyheading is not visible- {}".format(programmable_key_heading)
        assert bool(self.fc.fd["hppk"].verify_hppk_icon()) is True
        assert bool(self.fc.fd["hppk"].verify_supportkey_icon()) is True

    @pytest.mark.require_platform(["abandoned_case"])
    def test_15_verify_default_support_page_added_C34392563(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(3)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(3)
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        programmable_key_heading = self.fc.fd["hppk"].verify_programmable_key_heading()
        assert programmable_key_heading == "Create personalized shortcuts with the press of a button.","Programmable Keyheading is not visible- {}".format(programmable_key_heading)
        assert bool(self.fc.fd["hppk"].verify_hppk_icon()) is True
        assert bool(self.fc.fd["hppk"].verify_supportkey_icon()) is True
        self.fc.fd["hppk"].click_supportkey_icon()
        time.sleep(3)
        assert bool(self.fc.fd["hppk"].verify_default_support_page()) is True


    @pytest.mark.require_platform(["abandoned_case"])
    def test_16_verify_deletion_of_default_support_page_added_C34392564(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(3)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(3)
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        programmable_key_heading = self.fc.fd["hppk"].verify_programmable_key_heading()
        assert programmable_key_heading == "Create personalized shortcuts with the press of a button.","Programmable Keyheading is not visible- {}".format(programmable_key_heading)
        assert bool(self.fc.fd["hppk"].verify_hppk_icon()) is True
        assert bool(self.fc.fd["hppk"].verify_supportkey_icon()) is True
        self.fc.fd["hppk"].click_supportkey_icon()
        time.sleep(3)
        assert bool(self.fc.fd["hppk"].verify_default_support_page()) is True
        self.fc.fd["hppk"].click_delete1()
        time.sleep(3)
        assert bool(self.fc.fd["hppk"].verify_circular_1()) is True
        assert bool(self.fc.fd["hppk"].verify_add_action()) is True


    @pytest.mark.require_platform(["abandoned_case"])
    def test_17_verify_default_support_page_added_after_deleting_and_navigate_back_to_supportpage_C34392565(self):
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(3)
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(3)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(3)
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        programmable_key_heading = self.fc.fd["hppk"].verify_programmable_key_heading()
        assert programmable_key_heading == "Create personalized shortcuts with the press of a button.","Programmable Keyheading is not visible- {}".format(programmable_key_heading)
        assert bool(self.fc.fd["hppk"].verify_hppk_icon()) is True
        assert bool(self.fc.fd["hppk"].verify_supportkey_icon()) is True
        self.fc.fd["hppk"].click_supportkey_icon()
        time.sleep(3)
        assert bool(self.fc.fd["hppk"].verify_default_support_page()) is True
        self.fc.fd["hppk"].click_delete1()
        time.sleep(3)
        assert bool(self.fc.fd["hppk"].verify_circular_1()) is True
        assert bool(self.fc.fd["hppk"].verify_add_action()) is True
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        self.fc.fd["hppk"].click_supportkey_icon()
        time.sleep(3)
        assert bool(self.fc.fd["hppk"].verify_default_support_page()) is True

