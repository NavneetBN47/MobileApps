import pytest
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import time


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
soft_assertion = SoftAssert()

class Test_Suite_Context_Aware(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()

    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_01_adding_application_C36331665(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        self.fc.fd["context_aware"].click_add_application()
        self.fc.fd["context_aware"].click_add_application_search_box()
        self.fc.fd["context_aware"].search_application("calculator")
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_application("calculator")), True, "Calculator is not present")
        self.fc.fd["context_aware"].click_application("calculator")
        self.fc.fd["context_aware"].click_add_application_add_button()
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_application_icon("calculator"), "Calculator", "Calculator is not added")
        soft_assertion.raise_assertion_errors()
    

    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_02_adding_multiple_applications_C36331666(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(3)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        self.fc.fd["context_aware"].click_add_application()
        self.fc.fd["context_aware"].click_add_application_search_box()
        self.fc.fd["context_aware"].search_application("calendar")
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_application("calendar")), True, "Calendar is not present")
        self.fc.fd["context_aware"].click_application("calendar")
        self.fc.fd["context_aware"].click_add_application_add_button()
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_application_icon("calendar"), "Calendar", "Calendar is not added")
        self.fc.fd["context_aware"].click_add_application()
        self.fc.fd["context_aware"].click_add_application_search_box()
        self.fc.fd["context_aware"].search_application("camera")
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_application("camera")), True, "Camera is not present")
        self.fc.fd["context_aware"].click_application("camera")
        self.fc.fd["context_aware"].click_add_application_add_button()
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_application_icon("camera"), "Camera", "Camera is not added")
        soft_assertion.raise_assertion_errors()
    
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_03_no_left_right_arrow_C36331667(self):
        time.sleep(3)
        self.fc.reset_myhp_app()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        soft_assertion.assert_equal(self.fc.fd["devices"].verify_display_control(), "Display Control Action Item", "Display Control is not visible at PC Device")
        self.fc.fd["devices"].click_display_control()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        time.sleep(2)

        count = 0
        if self.fc.fd["context_aware"].verify_disney_plus_app_show():
            count +=1
        if self.fc.fd["context_aware"].verify_iqiyi_app_show():
            count +=1
        if self.fc.fd["context_aware"].verify_tencent_video_app_show():
            count +=1

        if count ==0:
            software_list = ["calculator", "calendar", "camera", "notepad", "paint"]
            for software in software_list:
                self.fc.fd["context_aware"].click_add_application()
                self.fc.fd["context_aware"].click_add_application_search_box()
                self.fc.fd["context_aware"].search_application(software)
                self.fc.fd["context_aware"].click_application(software)
                self.fc.fd["context_aware"].click_add_application_add_button()
        elif count ==1:
            software_list = ["calendar", "camera", "notepad", "paint"]
            for software in software_list:
                self.fc.fd["context_aware"].click_add_application()
                self.fc.fd["context_aware"].click_add_application_search_box()
                self.fc.fd["context_aware"].search_application(software)
                self.fc.fd["context_aware"].click_application(software)
                self.fc.fd["context_aware"].click_add_application_add_button()
        elif count ==2:
            software_list = ["camera", "notepad", "paint"]
            for software in software_list:
                self.fc.fd["context_aware"].click_add_application()
                self.fc.fd["context_aware"].click_add_application_search_box()
                self.fc.fd["context_aware"].search_application(software)
                self.fc.fd["context_aware"].click_application(software)
                self.fc.fd["context_aware"].click_add_application_add_button()
        elif count ==3:
            software_list = ["notepad", "paint"]
            for software in software_list:
                self.fc.fd["context_aware"].click_add_application()
                self.fc.fd["context_aware"].click_add_application_search_box()
                self.fc.fd["context_aware"].search_application(software)
                self.fc.fd["context_aware"].click_application(software)
                self.fc.fd["context_aware"].click_add_application_add_button()

        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_left_arrow()), False, "Left arrow is present")
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_right_arrow()), False, "Right arrow is present")
        soft_assertion.raise_assertion_errors()
    
    @pytest.mark.ota
    def test_04_left_right_arrow_C36331668(self):
        time.sleep(3)
        self.fc.reset_myhp_app()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        soft_assertion.assert_equal(self.fc.fd["devices"].verify_display_control(), "Display Control Action Item", "Display Control is not visible at PC Device")
        self.fc.fd["devices"].click_display_control()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        time.sleep(2)
        count = 0
        if self.fc.fd["context_aware"].verify_disney_plus_app_show():
            count +=1
        if self.fc.fd["context_aware"].verify_iqiyi_app_show():
            count +=1
        if self.fc.fd["context_aware"].verify_tencent_video_app_show():
            count +=1

        if count ==0:
            software_list = ["calculator", "calendar", "camera", "notepad", "paint", "access"]
            for software in software_list:
                self.fc.fd["context_aware"].click_add_application()
                self.fc.fd["context_aware"].click_add_application_search_box()
                self.fc.fd["context_aware"].search_application(software)
                self.fc.fd["context_aware"].click_application(software)
                self.fc.fd["context_aware"].click_add_application_add_button()
        elif count ==1:
            software_list = ["calculator", "calendar", "camera", "notepad", "paint"]
            for software in software_list:
                self.fc.fd["context_aware"].click_add_application()
                self.fc.fd["context_aware"].click_add_application_search_box()
                self.fc.fd["context_aware"].search_application(software)
                self.fc.fd["context_aware"].click_application(software)
                self.fc.fd["context_aware"].click_add_application_add_button()
        elif count ==2:
            software_list = ["calendar", "camera", "notepad", "paint"]
            for software in software_list:
                self.fc.fd["context_aware"].click_add_application()
                self.fc.fd["context_aware"].click_add_application_search_box()
                self.fc.fd["context_aware"].search_application(software)
                self.fc.fd["context_aware"].click_application(software)
                self.fc.fd["context_aware"].click_add_application_add_button()
        elif count ==3:
            software_list = ["camera", "notepad", "paint"]
            for software in software_list:
                self.fc.fd["context_aware"].click_add_application()
                self.fc.fd["context_aware"].click_add_application_search_box()
                self.fc.fd["context_aware"].search_application(software)
                self.fc.fd["context_aware"].click_application(software)
                self.fc.fd["context_aware"].click_add_application_add_button()

        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_left_arrow()), True, "Left arrow is not present")
        self.fc.fd["context_aware"].click_left_arrow()
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_right_arrow()), True, "Right arrow is not present")
        self.fc.fd["context_aware"].click_right_arrow()
        soft_assertion.raise_assertion_errors()
    
    @pytest.mark.ota
    def test_05_select_application_C36331669(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        soft_assertion.assert_equal(self.fc.fd["devices"].verify_display_control(), "Display Control Action Item", "Display Control is not visible at PC Device")
        self.fc.fd["devices"].click_display_control()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        software_list = ["notepad", "narrator"]
        for software in software_list:
                self.fc.fd["context_aware"].click_add_application()
                self.fc.fd["context_aware"].click_add_application_search_box()
                self.fc.fd["context_aware"].search_application(software)
                self.fc.fd["context_aware"].click_application(software)
                self.fc.fd["context_aware"].click_add_application_add_button()
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_application_icon("notepad"), "Notepad", "Notepad is not added")
        self.fc.fd["context_aware"].click_application("notepad")
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_application_icon("narrator"), "Narrator", "Narrator is not added")
        self.fc.fd["context_aware"].click_application("narrator")
        soft_assertion.raise_assertion_errors()
    
    @pytest.mark.ota
    def test_06_delete_application_C36766919(self):
        time.sleep(2)
        self.fc.reset_myhp_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        soft_assertion.assert_equal(self.fc.fd["devices"].verify_display_control(), "Display Control Action Item", "Display Control is not visible at PC Device")
        time.sleep(3)
        self.fc.fd["devices"].click_display_control()
        time.sleep(3)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        time.sleep(3)
        self.fc.fd["context_aware"].click_all_applications()
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        software_list = ["calculator", "calendar", "camera"]
        for software in software_list:
            self.fc.fd["context_aware"].click_add_application()
            self.fc.fd["context_aware"].click_add_application_search_box()
            self.fc.fd["context_aware"].search_application(software)
            self.fc.fd["context_aware"].click_application(software)
            self.fc.fd["context_aware"].click_add_application_add_button()
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_application_icon("calculator"), "Calculator", "Calculator is not added")
        self.fc.fd["context_aware"].click_application("calculator")
        self.fc.fd["context_aware"].click_delete_application_button("calculator")
        self.fc.fd["context_aware"].click_delete_continue_application_button()
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_application("calculator")), False, "Calculator is deleted")
        soft_assertion.raise_assertion_errors()
    
    @pytest.mark.ota
    def test_07_cancel_delete_application_C36766920(self):
        time.sleep(2)
        self.fc.reset_myhp_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        soft_assertion.assert_equal(self.fc.fd["devices"].verify_display_control(), "Display Control Action Item", "Display Control is not visible at PC Device")
        self.fc.fd["devices"].click_display_control()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        self.fc.fd["context_aware"].click_add_application()
        self.fc.fd["context_aware"].click_add_application_search_box()
        self.fc.fd["context_aware"].search_application("calculator")
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_application("calculator")), True, "Calculator is not present")
        self.fc.fd["context_aware"].click_application("calculator")
        self.fc.fd["context_aware"].click_add_application_add_button()
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_application_icon("calculator"), "Calculator", "Calculator is not added")
        self.fc.fd["context_aware"].click_application("calculator")
        self.fc.fd["context_aware"].click_delete_application_button("calculator")
        self.fc.fd["context_aware"].click_delete_cancel_application_button()
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_application("calculator")), True, "Calculator is deleted")
        soft_assertion.raise_assertion_errors()


    @pytest.mark.ota
    def test_10_checkbox_check_in_deleting_application_page_C36766923(self):
        time.sleep(2)
        self.fc.reset_myhp_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        soft_assertion.assert_equal(self.fc.fd["devices"].verify_display_control(), "Display Control Action Item", "Display Control is not visible at PC Device")
        self.fc.fd["devices"].click_display_control()

        time.sleep(5)
        self.fc.fd["context_aware"].click_add_application()
        self.fc.fd["context_aware"].click_add_application_search_box()
        self.fc.fd["context_aware"].search_application("calculator")
        self.fc.fd["context_aware"].click_application("calculator")
        self.fc.fd["context_aware"].click_add_application_add_button()
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_application_icon("calculator"), "Calculator", "Calculator is not added")

        time.sleep(5)
        self.fc.fd["context_aware"].click_add_application()
        self.fc.fd["context_aware"].click_add_application_search_box()
        self.fc.fd["context_aware"].search_application("camera")
        self.fc.fd["context_aware"].click_application("camera")
        self.fc.fd["context_aware"].click_add_application_add_button()
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_application_icon("camera"), "camera", "Camera is not added")

        time.sleep(5)
        self.fc.fd["context_aware"].click_calculator_icon()
        time.sleep(2)
        self.fc.fd["context_aware"].click_calculator_delete_icon()

        time.sleep(2)
        self.fc.fd["context_aware"].click_do_not_show_checkbox()
        time.sleep(2)
        self.fc.fd["context_aware"].click_delete_continue_application_button()

        time.sleep(2)
        self.fc.fd["context_aware"].click_camera_icon()
        time.sleep(2)
        self.fc.fd["context_aware"].click_camera_delete_icon()

        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_delete_do_not_show_checkbox()), False)
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_camera_icon_show()), False)


    @pytest.mark.ota
    def test_11_application_state_C36766918(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        soft_assertion.assert_equal(self.fc.fd["devices"].verify_display_control(), "Display Control Action Item", "Display Control is not visible at PC Device")
        self.fc.fd["devices"].click_display_control()

        time.sleep(5)
        self.fc.fd["context_aware"].click_add_application()
        self.fc.fd["context_aware"].click_add_application_search_box()
        self.fc.fd["context_aware"].search_application("calculator")
        self.fc.fd["context_aware"].click_application("calculator")
        self.fc.fd["context_aware"].click_add_application_add_button()
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_application_icon("calculator"), "Calculator", "Calculator is not added")
        time.sleep(3)
        self.fc.fd["context_aware"].click_calculator_icon()
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_calculator_delete_icon_show()), True)