import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_07_Scan_Auto_Rotation(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.camera = cls.fc.fd["camera"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.stack = request.config.getoption("--stack")
        cls.fc.go_home(stack=cls.stack)
        cls.p = load_printers_session

    def test_01_rotate_btn(self):
        """
        C31299365: "Rotate" button on Preview
        C31299366: Rotate button behavior available on the Preview screen
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.fc.capture_image_and_go_to_preview(verify_messages=False)
        self.common_preview.verify_rotate_btn()
        self.common_preview.select_transform_options(self.common_preview.TRANSFORM_ROTATE_BTN)
        self.common_preview.verify_title(self.common_preview.ROTATE_TITLE)
    
    def test_02_discard_changes(self):
        """
        C31299368: Cancel button behavior on Rotate screen after change
        C31299379: "Yes" button behavior on 'Discard changes' pop up
        C31299380: "No" button behavior on 'Discard changes' pop up
        C31299369: Verify tray popup when user select an item on Rotate screen
        C31299384: Verify tray popup disappear when user deselects all the items on Rotate screen
        C31299370: Select image and tap on "Rotate" on Rotate screen
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.fc.capture_image_and_go_to_preview(verify_messages=False)
        self.common_preview.select_transform_options(self.common_preview.TRANSFORM_ROTATE_BTN)
        self.common_preview.verify_title(self.common_preview.ROTATE_TITLE)
        self.common_preview.verify_auto_rotate_reset_btn()
        self.common_preview.select_auto_rotate_image(index=1)
        self.common_preview.verify_rotate_btn()
        self.common_preview.select_rotate_btn()
        self.common_preview.select_cancel()
        self.common_preview.verify_discard_changes_popup()
        self.common_preview.select_no()
        # get discard changes popup
        self.common_preview.select_cancel()
        self.common_preview.verify_discard_changes_popup()
        # verify "yes" button
        self.common_preview.select_yes()
        self.common_preview.verify_preview_screen()

    def test_03_multiple_image_rotate(self):
        """
        C31299371: Select multiple images and tap on Rotate on "Rotate" screen
        C31299372: Select image and tap on Delete button
        C31299373: Reset button behavior after Rotate was done
        C31299374: Reset button behavior after Rotate action
        C31299375: Reset button behavior after one file was deleted
        C31299376: Done button after tapping on Rotate without making a change
        C31299385: Rotate action E2E - Camera Scan
        """
        no_pages = 4
        self.__scan_multiple_photos_and_go_to_preview(no_pages)
        self.common_preview.verify_preview_screen()
        self.common_preview.select_transform_options(self.common_preview.TRANSFORM_ROTATE_BTN)
        self.common_preview.verify_title(self.common_preview.ROTATE_TITLE)
        # delete one page
        pages = self.common_preview.get_image_count_on_rotate_screen()
        assert pages == 4
        self.common_preview.select_auto_rotate_image(1)
        self.common_preview.verify_rotate_screen_tray_options()
        self.common_preview.select_auto_rotate_delete_btn()
        pages = self.common_preview.get_image_count_on_rotate_screen()
        assert pages == 3
        # reset
        self.common_preview.verify_auto_rotate_reset_btn()
        self.common_preview.select_auto_rotate_reset_button()
        pages = self.common_preview.get_image_count_on_rotate_screen()
        assert pages == 4
        # rotate multiple pages
        cell_img_1 = self.common_preview.verify_auto_rotate_image(1)
        cell_img_2 = self.common_preview.verify_auto_rotate_image(2)
        self.common_preview.select_multiple_images_on_rotate_screen([1,2])
        self.common_preview.select_rotate_btn()
        sleep(10)
        rotated_cell_img_1 = self.common_preview.verify_auto_rotate_image(1)
        rotated_cell_img_2 = self.common_preview.verify_auto_rotate_image(2)
        assert saf_misc.img_comp(cell_img_1, rotated_cell_img_1) > 0.06, "Init and rotated image should not match"
        assert saf_misc.img_comp(cell_img_2, rotated_cell_img_2) > 0.06, "Init and rotated image should not match"
        # reset pages
        self.common_preview.select_multiple_images_on_rotate_screen([1,2])
        self.common_preview.verify_auto_rotate_reset_btn()
        self.common_preview.select_auto_rotate_reset_button()
        sleep(10)
        reset_cell_img_1 = self.common_preview.verify_auto_rotate_image(1)
        reset_cell_img_2 = self.common_preview.verify_auto_rotate_image(2)
        assert saf_misc.img_comp(cell_img_1, reset_cell_img_1) == 0, "Init and reset image should match"
        assert saf_misc.img_comp(cell_img_2, reset_cell_img_2) == 0, "Init and reset image should match"
        self.common_preview.select_done()
        self.common_preview.verify_preview_screen()
    
    def test_04_rotation_screen_bottom_bar(self):
        """
        C31299378 - Pull bottom slide bar down to be back to Rotate screen
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.fc.capture_image_and_go_to_preview()
        self.common_preview.select_transform_options(self.common_preview.TRANSFORM_ROTATE_BTN)
        self.common_preview.select_auto_rotate_image(index=1)
        self.common_preview.drag_bottom_navbar_down()
        assert not self.common_preview.verify_an_element_and_click(self.common_preview.TF_COLLECTION_VIEW, click=False), "Bottom bar should not be displayed"
        assert not self.common_preview.verify_is_image_selected(raise_e=False), "Image should not be selected"

    def test_05_rotate_btn(self):
        """
        C31299225 - Rotate Button behavior
        C31299227 - Verify "Rotate" button and "3 Vertical Dots" button disappear while rotation takes place
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.fc.capture_image_and_go_to_preview()
        self.common_preview.select_transform_options(self.common_preview.TRANSFORM_ROTATE_BTN)
        assert not self.common_preview.verify_delete_page_x_icon(), "Delete page icon should not be displayed"
        self.common_preview.select_auto_rotate_image(index=1)
        init_img = self.common_preview.verify_preview_img()
        for i in range(4):
            prerotated_img = init_img if i == 0 else self.common_preview.verify_preview_img()
            self.common_preview.select_rotate_btn()
            rotated_img = self.common_preview.verify_preview_img()
            if i == 3:
                assert saf_misc.img_comp(init_img, rotated_img) < 0.06, "Image should match initial image after full rotation"
            else:
                assert saf_misc.img_comp(prerotated_img, rotated_img) > 0.06, "Image should change after rotation"

    def __scan_multiple_photos_and_go_to_preview(self, no_pages):
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.add_multi_pages_scan(no_pages)
        self.common_preview.verify_preview_screen()