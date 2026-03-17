import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const
pytest.app_info = "SMART"


class Test_Suite_01_Scan_Preview_Under_Shortcuts(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_ip = cls.p.get_printer_information()["ip address"]
        cls.fc.hpx = True
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.scan = cls.fc.fd["scan"]
        cls.welcome_web = cls.fc.fd["welcome_web"]
        cls.notifications = cls.fc.fd["notifications"]
        cls.camera = cls.fc.fd["camera"]
        cls.support = cls.fc.fd["support"]
        cls.profile = cls.fc.fd["profile"]
        cls.preview = cls.fc.fd["preview"]

    def test_1_verify_Scan_Preview_under_Shortcuts(self):
        """
        C51953890
        Description : Verify the behavior of Scan preview button

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Tap on "Shortcuts.
        Observe the Preview page
        Expected Result: The text in the textbox for naming the document in the Document Name section should be aligned to the left.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        self.preview.select_shortcuts_on_preview_screen()
        assert self.driver.wait_for_object("swipe_up_documents_btn")

    def test_2_verify_i_information_under_Shortcuts(self):
        """
        C51953891
        Description : Verify the behavior of the "i" (Information) button on the Shortcuts preview page during the Scan First flow(Ex : Start save test)

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Tap on "Shortcuts.
        Swipe up to view the shortcuts list.
        Tap on the "i" button on any shortcut.
        Observe the behavior
        Expected Result: The user is able to see the details or Information (Save to) about the selected shortcut.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        self.preview.select_shortcuts_on_preview_screen()
        self.preview.select_swipe_up_documents_on_shortcuts()
        self.preview.select_first_document_to_preview_on_shortcuts()

    def test_3_verify_threedots_on_preview_page(self):
        """
        C51953892
        Description : Verify the 3 dots(...) in preview page

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on 3 dots
        Observe the behavior
        Expected Result: User able to see options as Edit, Replace and Delete
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        self.preview.select_three_dots_icon()
        assert self.driver.wait_for_object("edit_on_three_dots")

    def test_4_verify_delete_option_on_preview_page(self):
        """
        C51953893
        Description : Verify the Delete option on preview page

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on 3 dots
        Click on Delete
        Observe the behavior
        Expected Result: The user is able to see the message "Are you sure you want to delete this document?" with options as Cancel and Delete
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        self.preview.select_three_dots_icon()
        assert self.driver.wait_for_objects("delete_on_three_dots")

    def test_5_verify_edit_option_on_preview_page(self):
        """
        C51953894
        Description : Verify the Edit functionality in the preview page for capture image

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on 3 dots
        Click on Edit
        Observe the behavior
        Expected Result: User able to Edit screen with options (Crop,Adjust,Filters,Text and Markup)
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        import pdb
        pdb.set_trace()
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        self.preview.select_three_dots_icon()
        self.preview.select_edit_on_three_dots()

    def test_6_verify_click_edit_on_threedots(self):
        """
        C51953895
        Description : Verify the Edit functionality in the preview page for capture image

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on 3 dots
        Click on Edit
        Select crop button Observe the behavior.
        Expected Result: User able to Edit screen with options (Crop,Adjust,Filters,Text and Markup)
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.support.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        self.preview.select_three_dots_icon()
        self.preview.select_edit_on_three_dots()
        self.preview.select_crop_btn_on_edit()

    def test_7_verify_click_adjust_on_threedots(self):
        """
        C51953896
        Description : Verify the Adjust functionality in the preview page for capture image

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on 3 dots
        Click on Edit
        Select adjust button Observe the behavior.
        Expected Result: User able to Edit screen with options (Crop,Adjust,Filters,Text and Markup)
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        self.preview.select_three_dots_icon()
        self.preview.select_edit_on_three_dots()
        self.preview.select_adjust_btn_on_edit()

    def test_8_verify_click_filters_on_threedots(self):
        """
        C51953897 
        Description : Verify the Filters functionality in the preview page for capture image
        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on 3 dots
        Click on Edit
        Select filters button Observe the behavior.
        Expected Result: User able to Edit screen with options (Crop,Adjust,Filters,Text and Markup)
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        self.preview.select_three_dots_icon()
        self.preview.select_edit_on_three_dots()
        self.preview.select_filters_btn_on_edit()

    def test_9_verify_click_text_on_threedots(self):
        """
        C51953898
        Description : Verify the Text functionality in the preview page for capture image

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on 3 dots
        Click on Edit
        Select text button Observe the behavior.
        Expected Result: User able to Edit screen with options (Crop,Adjust,Filters,Text and Markup)
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        self.preview.select_three_dots_icon()
        self.preview.select_edit_on_three_dots()
        self.preview.select_text_btn_on_edit()

    def test_10_verify_click_markup_on_threedots(self):
        """
        C51953899
        Description : Verify the Markup functionality in the preview page for capture image

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on 3 dots
        Click on Edit
        Select markup button Observe the behavior.
        Expected Result: User able to Edit screen with options (Crop,Adjust,Filters,Text and Markup)
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        self.preview.select_three_dots_icon()
        self.preview.select_edit_on_three_dots()
        self.preview.select_markup_btn_on_edit()

    def test_11_verify_auto_btn_on_edit_page(self):
        """
        C51953900
        Description : Verify the Auto button functionality in the preview page for capture image

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on 3 dots
        Click on Edit
        Select Auto button Observe the behavior.
        Expected Result: User able to Edit screen with options (Crop,Adjust,Filters,Text and Markup)
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        self.preview.select_three_dots_icon()
        self.preview.select_edit_on_three_dots()
        self.preview.select_auto_btn_on_edit()

    def test_12_verify_cancel_btn_on_edit_page(self):
        """
        C51953901
        Description : Verify the Cancel button functionality in the preview page for capture image

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on 3 dots
        Click on Edit
        Select Cancel button Observe the behavior.
        Expected Result: User able to Edit screen with options (Crop,Adjust,Filters,Text and Markup)
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        self.preview.select_three_dots_icon()
        self.preview.select_edit_on_three_dots()
        self.preview.select_cancel_btn_on_edit()

    def test_13_verify_discard_btn_on_edit_page(self):
        """
        C51953902
        Description : Verify the Discard button functionality in the preview page for capture image

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on 3 dots
        Click on Edit
        Select Discard button Observe the behavior.
        Expected Result: User able to Edit screen with options (Crop,Adjust,Filters,Text and Markup)
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        self.preview.select_three_dots_icon()
        self.preview.select_edit_on_three_dots()
        self.preview.select_discard_btn_on_edit()

    def test_14_verify_replace_btn(self):
        """
        C51953903
        Description : Verify the Replace button functionality in the preview page for capture image

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on 3 dots
        Click on Replace
        Observe the behavior.
        Expected Result: User able to Edit screen with options (Crop,Adjust,Filters,Text and Markup)
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        self.preview.select_three_dots_icon()
        assert self.driver.wait_for_object("replace_on_three_dots")
        self.preview.select_replace_on_three_dots()

    def test_15_verify_cancel_btn_on_delete_screen(self):
        """
        C51953904
        Description : Verify the Cancel button functionality in the delete screen for capture image

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on 3 dots
        Click on Delete
        Select Cancel button Observe the behavior.
        Expected Result: User able to Edit screen with options (Crop,Adjust,Filters,Text and Markup)
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        self.preview.select_three_dots_icon()
        self.preview.select_delete_on_three_dots()
        self.preview.select_cancel_btn_on_delete()

    def test_16_verify_delete_btn_on_delete_screen(self):
        """
        C51953905
        Description : Verify the Delete button functionality in the delete screen for capture image

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on 3 dots
        Click on Delete
        Select Delete button Observe the behavior.
        Expected Result: User able to Edit screen with options (Crop,Adjust,Filters,Text and Markup)
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        self.preview.select_three_dots_icon()
        self.preview.select_delete_on_three_dots()
        self.preview.select_delete_btn_on_delete()

    def test_17_verify_print_preview(self):
        """
        C51953906
        Description : Verify the Print preview functionality in the preview page for capture image

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on 3 dots
        Click on Print
        Observe the behavior.
        Expected Result: User able to Edit screen with options (Crop,Adjust,Filters,Text and Markup)
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        assert self.driver.wait_for_object("print_preview_on_preview_page")

    def test_18_verify_share_save_preview(self):
        """
        C51953907
        Description : Verify the Share/Save preview functionality in the preview page for capture image

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on Share/Save
        Observe the behavior.
        Expected Result: User able to Edit screen with options (Crop,Adjust,Filters,Text and Markup)
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        assert self.driver.wait_for_object("share/save_on_preview_page")

    def test_19_verify_shortcuts_on_preview_page(self):
        """
        C51953908
        Description : Verify the Shortcuts functionality in the preview page for capture image

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on Shortcuts
        Observe the behavior.
        Expected Result: User able to Edit screen with options (Crop,Adjust,Filters,Text and Markup)
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        assert self.driver.wait_for_object("shortcuts_btn")

    def test_20_verify_mobile_fax_on_preview_page(self):
        """
        C51953909
        Description : Verify the Mobile Fax functionality in the preview page for capture image

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on Mobile Fax
        Observe the behavior.
        Expected Result: User able to Edit screen with options (Crop,Adjust,Filters,Text and Markup)
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        assert self.driver.wait_for_object("mobile_fax_on_preview_page")

    def test_21_verify_document_name_on_landing_page(self):
        """
        C51953910
        Description : Verify the Document Name on the landing page

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on Shortcuts
        Observe the behavior.
        Expected Result: The text in the textbox for naming the document in the Document Name section should be aligned to the left.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        self.preview.select_shortcuts_on_preview_screen()
        assert self.driver.wait_for_object("swipe_up_documents_btn")
        self.preview.select_swipe_up_documents_on_shortcuts()
        self.preview.select_first_document_to_preview_on_shortcuts()
        assert self.driver.wait_for_object("file_name_textfield")

    def test_22_verify_document_name_modification(self):
        """
        C51953911
        Description : Verify the Document Name modification

        Install and launch app.
        Sign in and add printer.
        Navigate to Printer detail page.
        Tap on the "Camera Scan" tile and capture a file.
        Tap on "Next" on the Adjust Boundaries screen.
        Navigate to the Preview page.
        Click on Shortcuts
        Change or edit the document name.
        Select the email or save to cloud shortcut.
        Go to the specified location (email or cloud location) and observe
        Observe the behavior.
        Expected Result: The changed document name is saved as per the modification.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.fc.add_printer_by_ip(
            printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.click_to_view_device_page_from_home()
        self.driver.click("_shared_str_ok")
        self.driver.swipe()
        self.driver.scroll("_shared_camera_scan_tile", click_obj=True)
        self.driver.click("_shared_str_ok")
        self.camera.clear_tips_pop_up()
        self.preview.select_shutter_card_btn()
        self.preview.select_preview_next_btn()
        self.preview.select_shortcuts_on_preview_screen()
        assert self.driver.wait_for_object("file_name_textfield")
        self.driver.click("file_name_textfield")
        self.driver.clear_text("file_name_textfield")
        self.driver.send_keys("file_name_textfield", "change_name_2025")
        self.preview.select_swipe_up_documents_on_shortcuts()
        self.preview.select_first_document_to_preview_on_shortcuts()
