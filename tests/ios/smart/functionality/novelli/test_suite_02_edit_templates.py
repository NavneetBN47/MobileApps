import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_02_Edit_Templates(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()

        if "novelli" not in cls.p.p_obj.projectName:
            pytest.skip("Novelli printer is unavailable for testing this time")

        # Define the flows
        cls.home = cls.fc.fd["home"]
        cls.preview = cls.fc.fd["preview"]
        cls.photos = cls.fc.fd["photos"]
        cls.edit = cls.fc.fd["edit"]

        # Define variables
        cls.stack = request.config.getoption("--stack")
        cls.printer_info = cls.p.get_printer_information()
        login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=False, instant_ink=True)
        cls.username, cls.password = login_info["email"], login_info["password"]
        cls.fc.go_home(stack=cls.stack)

    @pytest.mark.parametrize("screen_type", ["front_btn", "back_btn"])
    def test_01_verify_edit_front_back_templates_screen(self, screen_type):
        """
        C29777675,  C29718804,  C29777772,  C29718798,  C29777773,  C29707845,  C29777666, C29777880
        Description:
         1. Load to Home screen with HP+ account login
         2. Click on View & Print button
         3. Click on My Photos, and select any photo from album
         4. Select 4x6 Two-Sided option from Print Size screen
         5. Click on 3 dot icon. If screen type == "back_btn", then choose Back button -> 3 dot icon -> Edit button
         6. CliCK on Edit button
         7. Click on Templates button
         8. Select any option from Templates button
         9. Click on Done button
         10. Click on Done button

        Expected Result:
         7. Verify Templates screen
         8. Templates can be selected success
         10. Verify Two-Sided Preview screen through:
            + Title
            + Front button
            + Back button
            + Print and Save button
        """
        self.fc.load_edit_screen_for_novelli(self.p, self.edit.TEMPLATE, is_back_screen=screen_type == "back_btn")
        current_image = self.edit.edit_img_screenshot()
        self.edit.select_template_type_by_index(index=2)
        new_image = self.edit.edit_img_screenshot()
        assert(saf_misc.img_comp(current_image, new_image) != 0.0), "template doesn't choose success"
        for _ in range(3):
            self.edit.select_edit_done()
        self.preview.verify_two_sided_preview_screen()

    def test_02_verify_edit_front_templates_replace_function(self):
        """
         C29718799
         Description:
         1. Load to Home screen with HP+ account login
         2. Click on View & Print button
         3. Click on My Photos, and select any photo from album
         4. Select 4x6 Two-Sided option from Print Size screen
         5. Click on 3 dot icon
         6. CliCK on Edit button
         7. Click on Templates button
         8. Select any option from Templates button
         9. Click on Done button
         10. Click on Replace button
         11. Select another option from Templates screen

         Expected Result:
         11. Templates can be changed success
        """
        self.fc.load_edit_screen_for_novelli(self.p, self.edit.TEMPLATE, is_back_screen=False)
        self.edit.select_template_type_by_index(index=2)
        self.edit.select_edit_done()
        current_image = self.edit.edit_img_screenshot()
        self.edit.select_edit_done()
        self.edit.select_edit_done()
        self.preview.verify_two_sided_preview_screen()
        self.preview.select_delete_page_icon()
        self.preview.select_edit(change_check={"wait_obj": "print_size_screen_title", "invisible": True})
        self.edit.dismiss_template_coachmark()
        self.edit.verify_edit_page_title()
        self.edit.select_edit_main_option(self.edit.TEMPLATE)
        self.edit.select_replace_btn()
        self.edit.select_template_type_by_index(index=3)
        self.edit.select_edit_done()
        new_image = self.edit.edit_img_screenshot()
        assert(saf_misc.img_comp(current_image, new_image) != 0.0), "template doesn't replace success"

    def test_03_verify_edit_front_templates_exit_function(self):
        """
         C29718803
         Description:
         1. Load to Home screen with HP+ account login
         2. Click on View & Print button
         3. Click on My Photos, and select any photo from album
         4. Select 4x6 Two-Sided option from Print Size screen
         5. Click on 3 dot icon
         6. CliCK on Edit button
         7. Click on Templates button
         8. Select any option from Templates button
         9. Click on X button

         Expected Result:
         9. Template doesn't change success
        """
        self.fc.load_edit_screen_for_novelli(self.p, self.edit.TEMPLATE, is_back_screen=False)
        current_image = self.edit.edit_img_screenshot()
        self.edit.select_template_type_by_index(index=2)
        self.edit.select_undo()
        new_image = self.edit.edit_img_screenshot()
        assert(saf_misc.img_comp(current_image, new_image) == 0.0), "template doesn't undo success"

    def test_04_verify_edit_front_markup_function(self):
        """
         C29870953
         Description:
         1. Load to Home screen with HP+ account login
         2. Click on View & Print button
         3. Click on My Photos, and select any photo from album
         4. Select 4x6 Two-Sided option from Print Size screen
         5. Click on 3 dot icon
         6. CliCK on Edit button
         7. Click on Markup item
         8. Select any option from Markup screen
         9. Click on Done button
         10. Click on Done button

         Expected Result:
         10. Verify Two-Sided Preview screen through:
            + Title
            + Front button
            + Back button
            + Print and Save button
        """
        self.fc.load_edit_screen_for_novelli(self.p, self.edit.MARKUP, is_back_screen=False)
        self.edit.select_highlight_btn()
        self.edit.select_edit_done()
        self.edit.select_edit_done()
        self.preview.verify_two_sided_preview_screen()